# Kraken-Exchange-DCA
A Python program to primarily assist in "Dollar Cost Averaging" cryptocurrency purchases on the Kraken cryptocurrency exchange via interacting with the Kraken API.
Can also be used to set up individual buy/ sell orders at users discretion. 
Previous transactions can be called and are saved into a local Excel sheet via Pandas for accessibility/ readability.
## Prerequisites
1. Python 3.0+
2. Kraken exchange personal API key and Secret key

## Kraken API set up
1. Create an account at https://www.kraken.com/en-gb/sign-up
2. Go to Account>Security>API>Add Key
3. Select desired permissions for your API (approve **Querey Funds** and **Create & Modify Orders** minimum).
4. Copy personal API KEY and API SECRET into: 
> api_key = 
> 
> api_sec =
5. Default currency is GBP/£ 

## Usages
The program can be used to:
1. Check current account balance of all available currencies
2. Give a precise value for the volume of currency being purchased for given fiat value (useful for purchasing small fractions of a coin)
3. Create a buy order for a given amount (**provided the account is funded**). If set to run passively, this automates the Dollar Cost Average buying strategy
4. Pull any number of past transactions from the users account. Data is then cleaned and saved to an excel file - useful for tax purposes/ general book keeping.

## How to
1. Enter your order amount as a floating point number in
> dca_amount = 
2. Enter your currency pair as a string in 
> pair = 
3. If necessary, use  the dca_volume() function to retrieve the volume to be purchased with your current order amount.
4. Use the dca() function to create an order. Change order_data parameters to suit your needs (see https://docs.kraken.com/rest/#operation/addOrder  for breakdown).
5. The "validate" key within order_data determines if the order is submitted ( True for simple validation, False for commiting and sending a live order).
6. Use a service such as Python Anywhere (https://www.pythonanywhere.com/) to automate your process and set up regular, reoccuring transactions (**requires account to be funded**).

## Saving transaction/ trade history
Cleaning and saving of past transactions is completed via the trade_history function.

"Offset" is a value used by the API for pagination, starting from a default of 0 and increasing by 50 each iteration.

The Pandas library is used to convert the Kraken response into a dataframe and then save it to excel.

The first time that the function is run, all previous transactions will be saved.

To avoid future replication or to only select the previous "x" transactions, use df.head(x) to retreive the x most recent transactions to be saved.

### Basic walkthrough example
> check_balance()
> 
> dca_volume() (if desired)
> 
> dca()
> 
> trade_history()


A successful varified by order response will look something like:
'''

Current price is: £25055.3
Amount purchased at current price is: 0.03991171528578784
{'error': [], 'result': {'descr': {'order': 'buy 0.03991171 XBTGBP @ market'}, 'txid': ['123456-ABCDE-123456']}}

'''

## Future improvements
1. Implementing functionality for adding / withdrawing funds from the account.
2. Adding profit/loss metrics for addition to the Trade History excel flie to assist with tax calculations. 
