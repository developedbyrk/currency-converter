# 💱 Currency Converter (USD-Based)

This is a simple Python command-line tool that converts US Dollars (USD) into various other currencies using real-time exchange rates from the [ExchangeRate-API](https://www.exchangerate-api.com/).

---

## 🚀 Features

- Fetches **live exchange rates** with a base currency of USD.
- Lets users view available currencies.
- Converts a user-entered USD amount into the selected currency.
- Clean, readable user prompts and error handling.

---

## 📦 Requirements

- Python 3.x
- `requests` library

You can install the required package with:

```bash
pip install requests


Enter the amount in US Dollars (USD): 100

Available currencies:

['USD', 'AED', 'AFN', 'ALL', 'AMD', 'ANG', 'AOA', 'ARS', 'AUD', 'AWG',...]

Enter the currency code you want to convert to (or type 'q' to quit): AUD

100.0 USD = 153.27 AUD
