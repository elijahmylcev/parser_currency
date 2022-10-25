import requests
from bs4 import BeautifulSoup

from config import page, user_agent

page = page
headers = {'User-agent': user_agent}

full_page = requests.get(page, headers=headers)
soup = BeautifulSoup(full_page.content, 'lxml')

convert = soup.find_all('div', class_="fl")
c = convert[2]

almaty_tenge_currency = float(c.text)

print(almaty_tenge_currency)
