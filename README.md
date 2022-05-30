# Kraken-Exchange-DCA
A Python program to assist in "Dollar Cost Averaging" cryptocurrency purchases on the Kraken cryptocurrency exchange via interacting with the Kraken API.
## Prerequisites
1. Python
2. Kraken exchange personal API key and Secret key

## Kraken API set up
1. Create an account at https://www.kraken.com/en-gb/sign-up
2. Go to Account>Security>API>Add Key
3. Select desired permissions for your API (approve **Querey Funds** and **Create & Modify Orders** minimum).
4. Copy personal API KEY and API SECRET into 
> api_key= 
> secret=

## Usage
The program can be used to:
1. Check current account balance of all available currencies
2. Give a precise value for the volume of currency being purchased for given fiat value (useful for purchasing small fractions of a coin)
3. Create a buy order for a given amount (**provided the account is funded**). If set to run passively, this automates the Dollar Cost Average buying strategy
4. Pull any number of past transactions from the users account. Data is then cleaned and saved to an excel file - useful for tax purposes/ general book keeping.

