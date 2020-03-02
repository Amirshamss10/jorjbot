#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 07:09:53 2020

@author: amir
"""

from os import system 
try:
    from selenium import webdriver 
except ModuleNotFoundError:
    system('pip3 install selenium') 
try:
    from termcolor import colored 
except ModuleNotFoundError:
    system('pip3 install termcolor') 
import time

print(colored('i am bot instagram', 'blue') )

time.sleep(3)

use = input(colored('Hello my name is JORJ, Enter a username instagram:','yellow'))
passwed = input(colored('password:','green'))
userName = str(use)
password = str(passwed)
time.sleep(1)

print(colored('Loading Instagram...','red')) 

url = 'https://www.instagram.com/accounts/login/?source=auth_switcher'
driver = webdriver.Chrome() 
driver.maximize_window()
driver.get(url) 
time.sleep(2)
driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[2]/div/label/input').send_keys(userName) #input
time.sleep(1)  
driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input') .send_keys(password)#input 
driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[4]').click()#login
time.sleep(4)

print(colored('Login was successful!', 'green')) 
time.sleep(2) 

driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[2]').click()#isButton, not Notifacions
time.sleep(2) 

driver.find_element_by_xpath('//*[@id="react-root"]/section/main/section/div[3]/div[1]/div/div[2]/div/a').click()  #page
print(colored('I logged in to your page :)', 'yellow')) #color
time.sleep(2) #time

driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[3]/a').click() #click button folowing
time.sleep(3) 

for i in range(1,100):
    page = driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/ul/div/li['+str(i)+']/div/div[3]/button')#list following
    page.click() 
    time.sleep(2) 
    driver.find_element_by_xpath('/html/body/div[5]/div/div/div[3]/button[1]').click()#unfollow
driver.close()   
print('FINISH')
print(colored('Developer: AmirShamss10','red') )



    
    

    
