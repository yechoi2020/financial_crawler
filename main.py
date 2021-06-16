import time
import random
import pywinmacro as pw

search_location = (233,135)
historical_location = (309,538)
download_location = (618, 704)

stocks = ["AMZN", "AAPL", "GS", "MS"]


def price(ticker):
    pw.click(search_location)
    time.sleep(random.random())
    pw.type_in("https://finance.yahoo.com/quote/")
    time.sleep(random.random())
    pw.type_in(ticker)
    time.sleep(random.random())
    pw.type_in("/history")
    pw.key_press_once("enter")
    time.sleep(random.randint(1,4))
    pw.click(historical_location)
    time.sleep(random.randint(2,3))
    pw.click(download_location)
    time.sleep(random.randint(2,4))


def get_price_data(stocks):
    for stock in stocks:
        price(stock)
        time.sleep(random.randint(1,4))

def chrome():
    pw.key_on("window")
    pw.key_on("r")
    pw.key_off("window")
    pw.key_off("r")
    time.sleep(1)
    pw.type_in("chrome -incognito")
    pw.key_press_once("enter")
    time.sleep(random.randint(1,3))

chrome()

get_price_data()
