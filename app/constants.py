import os
from dotenv import load_dotenv

load_dotenv()

VALID_CURRENCIES = ['USD', 'BRL', 'EUR', 'BTC', 'ETH']
API_KEY = os.getenv('API_KEY')