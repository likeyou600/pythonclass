from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
s = Service('./chromedriver.exe')

browser = webdriver.Chrome(service=s)

url = 'https://quizlet.com/zh-tw'
browser.get(url)

time.sleep(5)
bu = browser.find_element(By.CLASS_NAME, 'SiteNavLoginSection-loginButton')
login = bu.find_element(By.TAG_NAME, 'button')
login.click()

username = browser.find_element(By.ID, 'username')
username.send_keys('pucsimst@gmail.com')


password = browser.find_element(By.ID, 'password')
password.send_keys('pu123456')
time.sleep(1)

form = browser.find_element(By.CLASS_NAME, 'LoginPromptModal-form')
form.submit()

time.sleep(5)
soup = BeautifulSoup(browser.page_source, 'html.parser')
div = soup.find_all('div', {'class': 'UILinkBox-link'})
count = 1
print('================== 近期學習集 ==================')
for i in div:
    print('('+str(count)+')'+i.find("a").get('aria-label'))
    count += 1
