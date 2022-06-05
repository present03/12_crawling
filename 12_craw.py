import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="C:/Users/user/Desktop/12-crawling/chromedriver.exe")
url = 'https://shopping.naver.com/home/p/index.naver'
driver.get(url)

time.sleep(10)

serch = driver.find_element_by_xpath('//*[@id="_verticalGnbModule"]/div/div[2]/div/div[2]/div/div[2]/form/fieldset/div/input')
serch.click()
driver.find_element_by_xpath('//*[@id="_verticalGnbModule"]/div/div[2]/div/div[2]/div/div[2]/form/fieldset/div/input').send_keys('신발')
serch.send_keys(Keys.ENTER)

shopping=[]
name = driver.find_element_by_xpath('//*[@id="__next"]/div/div[2]/div[2]/div[3]/div[1]/ul/div/div[8]/li/div/div[2]/div[1]/a')
for i in range(1,4):
    time.sleep(10)
    for j in range(1,47):
        
        try:
          name = driver.find_element_by_xpath(f'//*[@id="__next"]/div/div[2]/div[2]/div[3]/div[1]/ul/div/div[{j}]/li/div/div[2]/div[1]/a').text
          print(f'{name}')
        except:
          name = 'NAN'
          
        try: 
          price = driver.find_element_by_xpath(f'//*[@id="__next"]/div/div[2]/div[2]/div[3]/div[1]/ul/div/div[{j}]/li/div/div[2]/div[2]/strong/span/span[2]').text
          print(f'{price}')
        except:
          try:
            price = driver.find_element_by_xpath(f'//*[@id="__next"]/div/div[2]/div[2]/div[3]/div[1]/ul/div/div[{j}]/li/div/div[2]/div[2]/strong/span/span').text
            print(f'{price}')
          except:
            name = 'NAN'

            
        shopping.append((name,price))
    driver.find_element_by_css_selector('#__next > div > div.style_container__1YjHN > div.style_inner__18zZX > div.style_content_wrap__1PzEo > div.style_content__2T20F > div.pagination_pagination__6AcG4 > a')
print(shopping)
driver.quit()

data = pd.DataFrame(shopping)
data.to_csv('C:/Users/user/Desktop/12-crawling/crawlingdata.csv')