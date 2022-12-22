import requests
from bs4 import BeautifulSoup
import lxml
from pprint import pprint

url = 'https://www.binance.com/ru/trade/ETH_USDT'
HEADERS = {
    'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:100.0) Gecko/20100101 Firefox/100.0',
    "accept": "text/html, application/xhtml+xml, application/xml;q=0.9, */*;q=0.8"
}

response = requests.get(url, headers=HEADERS)
soup = BeautifulSoup(response.text, 'lxml')
item = soup.find_all('")
pprint(item)






# def extra_price():
#     url = 'https://fapi.binance.com/fapi/v1/trades?symbol=' + symbol + '&limit=' + '1'
#     data = requests.get(url).json()
#     # print(data)
#     price = data[-1]['price']
#     # print(price)
#     return price


