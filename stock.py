import requests
import json
import csv
symbols = ["AAPL", "NFLX", "GOOGL", "META", "AMZN"]
token = "cdnrl5aad3i5o5okgudgcdnrl5aad3i5o5okgue0"
arr = []
header = ["stock_symbol", "percentage_change",
          "current_price", "last_close_price"]


def stock_Api():
    for symbol in symbols:
        # request to the endpoint
        r = requests.get('https://finnhub.io/api/v1/quote?',
                         params={'symbol': symbol, 'token': token})
        text = r.text
        rjson = json.loads(text)
        rjson['symbol'] = symbol
        arr.append(rjson)

    newarr = sorted(arr, key=lambda i: i['d'], reverse=True)

    most_volatile_stock = newarr[0]
    
    data = [most_volatile_stock['symbol'], most_volatile_stock['dp'],
            most_volatile_stock['c'], most_volatile_stock['pc']]
# write to the file the most volatile
    with open('stock.csv', 'w', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerow(data)


stock_Api()
