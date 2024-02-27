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


@app.get("/convert/")
async def convert_money(from_currency: str, to_currency: str, amount: float):
    if from_currency not in VALID_CURRENCIES or to_currency not in VALID_CURRENCIES:
        raise HTTPException(status_code=400, detail="Invalid currency!")

    return get_current_currency_values()