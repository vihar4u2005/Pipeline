'''
Created on 29 Jun 2020
Testcases to check the facebook login
@author: vihar
'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

username='vihar.ralkar@gmail.com'
password='Heidelberg'

driver = webdriver.Chrome()
url = 'http://www.youtube.com'
driver.get(url)
driver.maximize_window()



driver.implicitly_wait(5)
driver.close()