from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
s = Service('./chromedriver.exe')

browser = webdriver.Chrome(service=s)

url = 'https://zh.wikipedia.org/zh-tw/'
browser.get(url)

time.sleep(5)
search = browser.find_element(By.ID, 'searchInput')
search.send_keys('iphone')
search.submit()

time.sleep(5)
soup = BeautifulSoup(browser.page_source, 'html.parser')
table = soup.find('table', {'class': 'infobox hproduct vevent'})
imgs = table.find_all('img')
src = imgs[1].get('src')
url = 'https://'+src

browser.get(url)
