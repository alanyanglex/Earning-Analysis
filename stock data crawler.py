from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait 
from bs4 import BeautifulSoup
import time
import pandas as pd
import numpy as np
import re


CHROME_DRIVER = "/Users/alanyang/work/chromedriver"
service = Service(CHROME_DRIVER)
options = Options()
options.add_argument('--headless=new')
driver = webdriver.Chrome(service=service, options=options)

data = pd.read_csv ('/Users/alanyang/Desktop/earningdata.csv')
ticker_list = pd.DataFrame(data, columns = ['Symbol'])

download_list = []


for i in range(len(ticker_list)):
    print(i + 602)
    ticker = ticker_list.iat[i + 602,0]
    ticker = ticker.upper()
    print(ticker)

    URL = "https://finance.yahoo.com/quote/" + ticker + "/history?p=" + ticker

    print(URL)

    driver.get(URL)
    print("p1")
    driver.switch_to.window(driver.window_handles[0])
    print("p2")
    
    download_link = driver.find_element(By.XPATH, "//a[@class='Fl(end) Mt(3px) Cur(p)']")

    download_link = download_link.get_attribute('href')

    print("old download link: " + str(download_link))
    
    if(i > 0):
        counter = 0
        while(str(download_list[i - 1]) == str(download_link)):
            download_link = driver.find_element(By.XPATH, "//a[@class='Fl(end) Mt(3px) Cur(p)']")
            download_link = download_link.get_attribute('href')
            print(counter)
            counter += 1
            time.sleep(3)
        download_list.append(download_link)
        driver.find_element(By.LINK_TEXT, "Download").click()
        print("new download link: " + str(download_link))
    else:
        driver.find_element(By.LINK_TEXT, "Download").click()
        download_list.append(download_link)
    
    #WebDriverWait(driver, 10).until(lambda x: x.find_element(By.LINK_TEXT, "Download")).click()

    print("download true")

    time.sleep(3)



















    
    
    
