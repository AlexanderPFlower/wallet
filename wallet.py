import math

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

# FINALLY learnt how to iterate values of one list and store them as values in a key:value pair with another list!
# hashtag 'took me all day but I learnt how to do it!' It's so clean and simple, too!
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


playerWallet()
