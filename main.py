from fastapi import FastAPI, HTTPException
from constants import API_KEY, VALID_CURRENCIES
import requests

app = FastAPI()


def get_current_currency_values():
    response = requests.get(f'https://api.currencybeacon.com/v1/latest?api_key={API_KEY}')
    response_body = response.json()
    currencies_with_values = {}
    
    for currency in VALID_CURRENCIES:
        currencies_with_values[currency] = response_body['rates'][currency]
    return currencies_with_values


def convert_amount_to_currency(from_currency, to_currency, amount):
    currency_values = get_current_currency_values()

    if from_currency == 'USD':
        converted_amount = amount * currency_values[to_currency]
    elif to_currency == 'USD':
        converted_amount = amount/currency_values[from_currency]
    else:
        dollars_amount = amount/currency_values[from_currency]
        converted_amount = dollars_amount * currency_values[to_currency]

    return round(converted_amount, 2)


@app.get("/convert/")
async def convert_money(from_currency: str, to_currency: str, amount: float):
    if from_currency not in VALID_CURRENCIES or to_currency not in VALID_CURRENCIES:
        raise HTTPException(status_code=400, detail="Invalid currency!")

    converted_amount = convert_amount_to_currency(from_currency, to_currency, amount)
    return {'amount': converted_amount, 'currency': to_currency}