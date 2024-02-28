from fastapi.testclient import TestClient
from main import (
    app,
    get_current_currency_values,
    convert_amount_to_currency
)
import requests

client = TestClient(app)


def test_get_currency_values(requests_mock):
    api_key = 'random-api-key'
    json_response = {
        'base': 'USD',
        'rates': {
            'USD': 1,
            'BRL': 2,
            'BTC': 0.00001,
            'ETH': 0.001,
            'EUR': 0.5,
            'RUB': 100,
            'SVC': 10
        }
    }
    url = f'https://api.currencybeacon.com/v1/latest?api_key={api_key}'
    requests_mock.get(url, json=json_response)

    currencies_response = get_current_currency_values(api_key)
    expected_response = json_response['rates']
    del expected_response['RUB']
    del expected_response['SVC']

    for key in currencies_response:
        assert currencies_response[key] == expected_response[key]


def test_convert_amount_to_usd(mocker):
    from_currency = 'BRL'
    to_currency = 'USD'
    amount = 10.0
    currencies = {
        'USD': 1,
        'BRL': 2,
        'BTC': 0.00001,
        'ETH': 0.001,
        'EUR': 0.5
    }
    mocker.patch('main.get_current_currency_values', return_value=currencies)

    converted_amount = convert_amount_to_currency(from_currency, to_currency, amount)
    assert converted_amount == amount / currencies[from_currency]


def test_convert_amount_from_usd(mocker):
    from_currency = 'USD'
    to_currency = 'BRL'
    amount = 10.0
    currencies = {
        'USD': 1,
        'BRL': 2,
        'BTC': 0.00001,
        'ETH': 0.001,
        'EUR': 0.5
    }
    mocker.patch('main.get_current_currency_values', return_value=currencies)

    converted_amount = convert_amount_to_currency(from_currency, to_currency, amount)
    assert converted_amount == amount * currencies[to_currency]


def test_convert_amount_with_other_currencies(mocker):
    from_currency = 'BRL'
    to_currency = 'ETH'
    amount = 2000.0
    currencies = {
        'USD': 1,
        'BRL': 2,
        'BTC': 0.00001,
        'ETH': 0.001,
        'EUR': 0.5
    }
    mocker.patch('main.get_current_currency_values', return_value=currencies)

    converted_amount = convert_amount_to_currency(from_currency, to_currency, amount)
    assert converted_amount == (amount / currencies[from_currency]) * currencies[to_currency]


def test_convert_currency():
    from_currency = 'BRL'
    to_currency = 'ETH'
    amount = 2000.0
    params = f'?from_currency={from_currency}&to_currency={to_currency}&amount={amount}'

    response = client.get(f'/convert{params}')
    assert response.status_code == 200
    
    converted_amount_json = response.json()
    assert isinstance(converted_amount_json['amount'], float)
    assert isinstance(converted_amount_json['currency'], str)
    assert converted_amount_json['currency'] == to_currency