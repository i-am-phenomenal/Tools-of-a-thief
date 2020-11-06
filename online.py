from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By 
import time 
from datetime import datetime
import os

url = "https://web.whatsapp.com/"
driver = webdriver.Chrome()
driver.get(url)
driver.implicitly_wait(10)
driver.maximize_window()


def writeToLogFile(name):
    filePath = os.getcwd() + "/logFile.txt"
    with open(filePath, mode="a") as file: 
        now = datetime.now()
        toString = now.strftime("%d-%m-%y, %H:%M:%S")
        message = name + " ---->  " + toString
        file.write(message)
        file.write("\n")

def checkStatus(name):
    while True:
        xPath = "//span[@title='{0}']".format(name)
        element = driver.find_element_by_xpath(xPath)
        element.click()
        driver.implicitly_wait(15)
        titleBar = driver.find_elements_by_class_name("_33QME")
        for div in titleBar:
            splitted = div.text.split("\n")
            if len(splitted) == 2: 
                if splitted[1] == "online":
                    writeToLogFile(name)
                    print("ONLINE !!")

checkStatus(input("Enter name"))