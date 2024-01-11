'''
What works:
1. I can get the user to give me numbers for each money denomination aka moneyType, stored in benchtop
2. I can then access the values of moneyValues and store that in a list, as well as accessing benchtop values
3. I can take these two lists and zip them together to do a 'for f, b in zip(list1, list2)' in order to create a
new list. The actual code is below, where counter is counting each 'physical' coin or note, and v is a placeholder
for 'values' aka moneyValues (the float value of centage and dollar representation).

for amount, financialValue in zip(counter, v):
    x = amount * financialValue
    wallet.append(x)

What I'm trying to do now:
NOW I FINALLY KNOW HOW TO UPDATE THE WALLET! HUZZAH!
The next step is to finish the wallet.
I noticed that having 3 five cents results in 0.15000000000000002.
I will be testing the current state with values all 1, then 2, etc

Okay so multiples of 3, 6, and 7 do not work for 0.05, 0.10, and 0.20 centages.


HUZZAH! It is called precision handling using modulo %.
%5.4f % 3.14592 = 3.1416 because 5 = the # of numbers, 4 is # of numbers post-decimal, and it is rounded up?
'''
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

# REFERENCES FOR ACCESSING KEYS AND VALUES
'''
# Reference for printing each item in moneyTypes and values of moneyValues.values()

def playerWallet():
    for i in moneyTypes:
        print(i)
    for i in moneyValues.values():
        print(i)

# Reference for these two data sets into separate lists

def playerWallet():
    k = []
    v = []
    for i in moneyTypes:
        k.append(i)
    for i in moneyValues.values():
        v.append(i)
    print(k)
    print(v)


def checker():
    # Creating a list of all the values in moneyValues
    v = []
    for i in moneyValues.values():
        v.append(i)

    temp = []
    for i in benchtop:
        temp.append(i)
    
    print("\nHere is a list of all the values in moneyValues!\n" + str(v))
    print("And here are the frequencies of each value we have on the benchtop lol\n" + str(temp))
'''

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
