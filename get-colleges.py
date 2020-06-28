# -*- coding: utf-8 -*-
"""
Created on Thu May 14 18:07:24 2020


engg 5000+, arts 5700+, cmp 4200+, commerse 4200+, mngt 6600+



@author: pratiksha.garode
"""

from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import time

#step 1

driver = webdriver.Chrome(r"C:\Users\pratiksha.garode\softwares\chromedriver_win32\chromedriver.exe")

driver.get("https://collegedunia.com/management-colleges") #website url in ""


#step 2

college=[]
content = driver.page_source
soup = BeautifulSoup(content)
i = 0
for a in soup.findAll('a',href=True, attrs={'class':'college_name'}):
	name=a.find('h3')
	print(i)
	print(name)
	i += 1
#name=a.find('h3', attrs={'class':'row listing-block-cont js-scrolling-container'})
	college.append(name.text)
	
#step 3
	
df = pd.DataFrame(college) 
df.to_csv('C:\Practice\colleges_tai\category13_management.csv', index=False, encoding='utf-8')

check_height = driver.execute_script("return document.body.scrollHeight;")
while True:
    print(j * 2)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight - 750);")
    #time.sleep(5)
    #driver.execute_script("window.scrollTo(0, -5);")
    time.sleep(1)
    height = driver.execute_script("return document.body.scrollHeight;") 
    if height == check_height: 
        break 
    check_height = height