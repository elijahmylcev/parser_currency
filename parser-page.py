from time import sleep

import requests
from bs4 import BeautifulSoup
from config import page, user_agent
from selenium import webdriver


# headers = {'User-agent': user_agent}
# full_page = requests.get(page, headers=headers)
# soup = BeautifulSoup(full_page.content, 'lxml')
#
# print(soup)

# def get_data_with_selenium(page_url):
#   options = webdriver.ChromeOptions()
#
#   try:
#     driver = webdriver.Chrome(
#       executable_path='chromedriver.exe',
#       options=options
#     )
#     driver.get(url=page_url)
#     sleep(10)
#
#     with open('index.html', 'w', encoding="utf-8") as file:
#       file.write(driver.page_source)
#
#   except Exception as ex:
#     print(ex)
#   finally:
#     driver.close()
#     driver.quit()
#
#
# # def main():
# get_data_with_selenium(page_url=page)

with open('index.html', 'r', encoding="utf-8") as file:
  src = file.read()

soup = BeautifulSoup(src, 'lxml')

elements = soup.find_all('span', {'title': 'RUB - покупка'})

result_values = []

for el in elements:
  result_values.append(float(el.text))

print(result_values)

maximum = max(result_values)

print(maximum)



# if __name__ == '__main__':
#   main()
