from time import sleep

import requests
from bs4 import BeautifulSoup
from config import page, user_agent
from selenium import webdriver


def get_data_with_selenium(page_url):
  options = webdriver.ChromeOptions()

  try:
    driver = webdriver.Chrome(
      executable_path='chromedriver.exe',
      options=options
    )
    driver.get(url=page_url)
    sleep(5)

    with open('index.html', 'w', encoding="utf-8") as file:
      file.write(driver.page_source)

  except Exception as ex:
    print(ex)
  finally:
    driver.close()
    driver.quit()


# def main():
# get_data_with_selenium(page_url=page)

with open('index.html', 'r', encoding="utf-8") as file:
  src = file.read()

soup = BeautifulSoup(src, 'lxml')

punkt_open_list = soup.find_all('tr', class_='punkt-open')

objects = []
for el in punkt_open_list:
  name = el.find('a', class_='tab').text
  addres = el.find('address').text
  time_update = el.find('div', class_='relativeTime').text
  rate = float(el.find('span', {'title': 'RUB - покупка'}).text)
  phone = el.find('a', class_='phone').text
  el_object = {
    'name': name,
    'address': addres,
    'time_update': time_update,
    'rate': rate,
    'phone': phone,
  }

  objects.append(el_object)


print(objects[0])

# maximum = max(result_values)

# print(maximum)


# if __name__ == '__main__':
#   main()
