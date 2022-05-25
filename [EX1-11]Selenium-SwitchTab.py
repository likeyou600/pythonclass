from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
s = Service('./chromedriver.exe')

browser = webdriver.Chrome(service=s)

url = 'https://www.lib.pu.edu.tw/'
browser.get(url)

time.sleep(5)
form = browser.find_element(By.NAME, 'form1')
inputs = form.find_elements(By.TAG_NAME, 'input')
target = '九把刀'
inputs[0].send_keys(target)
time.sleep(5)
inputs[1].click()

browser.switch_to.window(browser.window_handles[1])
time.sleep(5)

browser.switch_to.frame('leftFrame')

soup = BeautifulSoup(browser.page_source, 'html.parser')
books = soup.find_all('a', {'class': 'bookname'})

print("\n========== Result for Searching '%s' ==========" % target)
for i in range(len(books)):
    print("(%d)" % (i+1), books[i].text)
