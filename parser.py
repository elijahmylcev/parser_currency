import requests
from bs4 import BeautifulSoup
from config import page, user_agent


class Currency:
  page = page
  headers = {'User-agent': user_agent}

  currency_converted_price = 0

  def __init__(self):
    self.currency_converted_price = float(self.get_currency_price())

  def get_currency_price(self):
    full_page = requests.get(self.page, headers=self.headers)
    soup = BeautifulSoup(full_page.content, 'lxml')

    convert = soup.find_all('div', class_="fl")
    c = convert[2]
    return c

almaty_tenge_currency = float(c.text)

print(almaty_tenge_currency)
