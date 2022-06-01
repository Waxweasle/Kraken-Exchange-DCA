import requests
import pandas as pd
import base64
import hashlib
import hmac
import time
import urllib.parse
import openpyxl
from datetime import datetime


api_url = "https://api.kraken.com"
api_key = "YOUR PUBLIC API KEY HERE"
api_sec = "YOUR SECRET KEY HERE"
dca_amount = 1000.00
pair = "XXBTZGBP"


# AUTHENTICATION
def get_kraken_signature(urlpath, data, api_sec):

    postdata = urllib.parse.urlencode(data)
    encoded = (str(data['nonce']) + postdata).encode()
    message = urlpath.encode() + hashlib.sha256(encoded).digest()

    mac = hmac.new(base64.b64decode(api_sec), message, hashlib.sha512)
    sigdigest = base64.b64encode(mac.digest())
    return sigdigest.decode()


def kraken_request(uri_path, data, api_key, api_sec):
    headers = {
        'API-KEY': api_key,
        'API-SIGN': get_kraken_signature(uri_path, data, api_sec)
    }
    response = requests.post((api_url + uri_path), headers=headers, data=data)
    return response

# CHECK ACC BALANCE
def check_balance(api_key, api_sec):
    response = kraken_request('/0/private/Balance', {"nonce": str(int(1000*time.time()))}, api_key, api_sec)
    print(f"Your current account balance is : {response.json()}")

# GET VOLUME
def dca_volume(dca_amount,pair):
    resp = requests.get(f'https://api.kraken.com/0/public/Ticker?pair={pair}')
    live_price = float((resp.json()['result'][pair]['a'][0]))
    print(f"Current price is: £{live_price}")
    volume = float(dca_amount / live_price)
    print(f"Amount purchased at current price is: {volume}")
    return volume


# CREATE ORDER
def dca(api_key, api_sec):
    volume = dca_volume(dca_amount, pair)
    order_data = {
        "nonce": str(int(1000 * time.time())),
        "ordertype": "market",
        "pair": pair,
        "type": "buy",
        "volume": volume,
        "validate": True
    }
    response = kraken_request('/0/private/AddOrder', order_data, api_key, api_sec)
    print(response.json())


# CANCEL TRANSACTION
def cancel(txn_id, api_key, api_sec):
    cancel_data = {
        "nonce": str(int(1000 * time.time())),
        "txid": txn_id
    }
    response = kraken_request('/0/private/CancelOrder', cancel_data, api_key, api_sec)
    print(response.json())


# GET TRADE HISTORY, CLEAN DATA , SAVE TO EXCEL
def trade_history():
    offset = 0
    while True:
        try:
            data = {
                "nonce": str(int(1000 * time.time())),
                "trades": True,
                "ofs": offset,
            }
            response = kraken_request('/0/private/TradesHistory', data, api_key, api_sec)
            data = response.json()
            time.sleep(2)
            orders = data['result']['trades']
            df = pd.DataFrame.from_dict(orders)
            df = df.transpose()
            df = df.drop('postxid', axis=1)
            df['price'] = df.price.astype(float)
            df['cost'] = df.cost.astype(float)
            df['fee'] = df.fee.astype(float)
            df['margin'] = df.margin.astype(float)
            df = df.round(2)
            df['time'] = pd.to_datetime(df['time'], unit='s')
            offset += 50

            try:
                with pd.ExcelWriter('Trade History.xlsx', mode="a", engine="openpyxl", if_sheet_exists='overlay') \
                        as writer:
                    df.to_excel(writer, sheet_name='sheet1', startrow=writer.sheets['sheet1'].max_row, header=None)
            except FileNotFoundError:
                with pd.ExcelWriter('Trade History.xlsx') as writer:
                    df.to_excel(writer, sheet_name='sheet1')
            if orders == {}:
                print("All transactions processed.")
                break
        except KeyError:
            print("All transactions processed.")
            break
