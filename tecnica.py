
import requests
from selenium import webdriver
from bs4 import BeautifulSoup

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
options.add_argument('--headless')

driver = webdriver.Chrome("C:\\Users\\Tomás Estévez Lenz\\Downloads\\chromedriver_win32\\chromedriver", chrome_options=options)
#firefox_driver = webdriver.Firefox()
driver.get("https://simple.ripley.cl/tecno/computacion/notebooks?source=menu")
r = requests.get("https://simple.ripley.cl/tecno/computacion/notebooks?source=menu")

content = driver.page_source

print("---- Selenium ----")
print(content)

print("\n---- Request ----")
print(r.text)