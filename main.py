from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import os
import logging
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('CMC_API_KEY')
if not api_key:
    raise ValueError("CMC_API_KEY not found in environment variables.")

url = 'https://pro-api.coinmarketcap.com/v2/cryptocurrency/quotes/latest'
parameters = {
    'id': '1',
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': api_key,
}

try:
    session = Session()
    session.headers.update(headers)
    response = session.get(url, params=parameters)
    data = json.loads(response.text)

    bitcoin_data = data['data']['1']
    name = bitcoin_data['name']
    price = bitcoin_data['quote']['USD']['price']
    percentage_change = bitcoin_data['quote']['USD']['percent_change_24h']

    message = f"{name} is at ${price:.2f}, Daily change {percentage_change:.2f}%"
    print(message)

except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)

