from selenium import webdriver
from bs4 import BeautifulSoup
import time
import requests as rq
import pandas as pd
  
# Creating a webdriver instance
driver = webdriver.Chrome("chromedriver.exe")


# Opening linkedIn's login page
driver.get("https://www.linkedin.com/login")
time.sleep(5)
  
# entering username
username = driver.find_element_by_id("username")
  
# Enter Your Email Address
username.send_keys("dfbau2002@gmail.com")  
  
# entering password
pword = driver.find_element_by_id("password")
  
# Enter Your Password
pword.send_keys(['PSW'])        
  
# Clicking on the log in button
# Format (syntax) of writing XPath --> 
# //tagname[@attribute='vgitalue']
driver.find_element_by_xpath("//button[@type='submit']").click()

profile_url = "https://www.linkedin.com/in/nicolasrbernal/"
driver.get(profile_url)

time.sleep(5)
  
src = driver.page_source  

soup = BeautifulSoup(src, "html.parser")

intro = soup.find('div', {'class': 'pv-text-details__left-panel'}) 

name_loc = intro.find("h1")
name = name_loc.get_text().strip()

works_info = intro.find("div", {'class': 'text-body-medium'})
works = works_info.get_text().strip()


loc_info = soup.find('div', {'class':'pb2 pv-text-details__left-panel'})
loc = loc_info.find('span').text.strip()


data = pd.DataFrame(index = ['Name', 'Works At', 'Location'], columns = ['value'])
data['value'] = [name, works, loc]
data.to_csv('scrap_results.csv')
