# Kraken-Exchange-DCA
A Python program to primarily assist in "Dollar Cost Averaging" cryptocurrency purchases on the Kraken cryptocurrency exchange via interacting with the Kraken API.
Can also be used to set up individual buy/ sell orders at users discretion. 
Previous transactions can be pulled and are saved into a local Excel sheet for accessibility/ readability.
## Prerequisites
1. Python
2. Kraken exchange personal API key and Secret key

## Kraken API set up
1. Create an account at https://www.kraken.com/en-gb/sign-up
2. Go to Account>Security>API>Add Key
3. Select desired permissions for your API (approve **Querey Funds** and **Create & Modify Orders** minimum).
4. Copy personal API KEY and API SECRET into: 
> api_key = 
> 
> secret =

## Usages
The program can be used to:
1. Check current account balance of all available currencies
2. Give a precise value for the volume of currency being purchased for given fiat value (useful for purchasing small fractions of a coin)
3. Create a buy order for a given amount (**provided the account is funded**). If set to run passively, this automates the Dollar Cost Average buying strategy
4. Pull any number of past transactions from the users account. Data is then cleaned and saved to an excel file - useful for tax purposes/ general book keeping.

## How to
1. Enter your order amount as an integer in
> dca_amount = 
2. Enter your currency pair as a string in 
> pair = 
3. If necessary, use  the dca_volume() function to retrieve the volume to be purchased with your current order amount.
4. Use the currency pair and volume 

## Saving txn history
Cleaning and saving of past transactions is completed via the trade_history function.

"Offset" is a value used by the API for pagination, starting from a default of 0 and increasing by 50 each iteration.

The Pandas library is used to convert the Kraken response into a dataframe and then save it to excel.

The first time that the function is run, all previous transactions will be saved.

To avoid future repliction or to only select the previous "x" transactions, use df.head(x) to retreive the x most recent transactions to be saved.
