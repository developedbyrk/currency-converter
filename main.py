import requests

url = 'https://v6.exchangerate-api.com/v6/<API-Key>/latest/USD'

response = requests.get(url)

def currencyJson():
    text = response.json().get('conversion_rates', [])
    return text

currencyDict = currencyJson()

def getCurrencyKeys():
    lst = []
    print("\nAvailable currencies:\n")
    for key in currencyDict.keys():
        lst.append(key)

    print(lst)

while True:
    try:
        dollar = float(input("Enter the amount in US Dollars (USD): "))
        break
    except ValueError:
        print("Please enter a valid number.")

getCurrencyKeys()

def result(): 
    while True:
        targetCurrency = input("Enter the currency code you want to convert to (or type 'q' to quit): ").upper()

        if targetCurrency == 'Q':
            print("Exiting currency converter. Goodbye!")
            break

        if targetCurrency in currencyDict:
            print(f"{dollar} USD = {(currencyDict[targetCurrency] * dollar)} {targetCurrency}")
            break
        else: 
            print("Not matching key found in the list")

result()
