import requests

symbol = 'BTCUSDT'


def extra_price():
    url = 'https://fapi.binance.com/fapi/v1/trades?symbol=' + symbol + '&limit=' + '1'
    data = requests.get(url).json()
    # print(data)
    price = data[-1]['price']
    # print(price)
    return price
