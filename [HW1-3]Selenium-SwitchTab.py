from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
s = Service('./chromedriver.exe')

browser = webdriver.Chrome(service=s)

url = 'https://www.lib.pu.edu.tw/'
browser.get(url)
time.sleep(3)

post5 = browser.find_element(By.CLASS_NAME, 'post5')
post5.find_element(By.TAG_NAME, 'a').click()
browser.switch_to.window(browser.window_handles[1])

time.sleep(3)

search = browser.find_element(By.ID, 'search_input')
target = '九把刀'
search.send_keys(target)
browser.find_element(By.NAME, 'formA').find_element(By.TAG_NAME, 'a').click()
time.sleep(3)

soup = BeautifulSoup(browser.page_source, 'html.parser')
titles = soup.find_all('h6', {'class': 'owl-title'})
print("\n========== Result for Searching '%s' ==========" % target)
count = 1
for title in titles:
    if(count > 30):
        break
    print('('+str(count)+')' + title.find('a').getText())
    count += 1
