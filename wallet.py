# VERSION 1.0.4
import math, subprocess

# Clear function so I don't have to clear the terminal manually every time (obviously not going to work with Windows)
def clear():
    subprocess.call('clear', shell=True)

# named denomination of currencies in Australia
moneyTypes = ['five cents', 'ten cents', 'twenty cents', 'fifty cents', 'one dollar', 'two dollars', 'five dollars', 'ten dollars', 'twenty dollars', 'fifty dollars', 'one-hundred dollars']

# dictionary of each currency denomination's value 
moneyValues = {
    "fiveCents" : 0.05,
    "tenCents" : 0.10,
    "twentyCents" : 0.20,
    "fiftyCents" : 0.50,
    "oneDollar" : 1.0,
    "twoDollars" : 2.0,
    "fiveDollars" : 5.0,
    "tenDollars" : 10.0,
    "twentyDollars" : 20.0,
    "fiftyDollars" : 50.0,
    "oneHundredDollars" : 100.0 }

# the amount of each moneyType is dumped in the benchtop, named as such as if you were throwing your change on the shopkeeper's counter!
benchtop = []

# for loop input stored and typecasted as int to be dumped into collector
for i in moneyTypes:
    x = input(f'How many {i} do you have? ')
    x = int(x)
    benchtop.append(x)

# Create walletCount dict, which is a count of physical money denominations as values, with moneyTypes data as keys (used soley for checking) 
walletCount = {moneyTypes: benchtop for moneyTypes, benchtop in zip(moneyTypes, benchtop)}

def playerWallet():
    # Accessing values
    v = []
    for i in moneyValues.values():
        v.append(i)

    counter = []
    for i in benchtop:
        counter.append(i)

    # Calculating the values to create the translation of values
    wallet = []
    for amount, financialValue in zip(counter, v):
        x = amount * financialValue
        x = "%.2f" % x
        wallet.append(x)
        
    # Test printing result
    print(wallet)

clear()
playerWallet()
#print(walletCount)
