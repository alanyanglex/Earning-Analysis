from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
import pandas as pd
import re


CHROME_DRIVER = "/Users/alanyang/work/chromedriver"
service = Service(CHROME_DRIVER)
options = Options()
options.add_argument('--headless=new')
driver = webdriver.Chrome(service=service, options=options)

data = pd.read_csv ('/Users/alanyang/Desktop/stocklist.csv')
ticker_list = pd.DataFrame(data, columns = ['Symbol'])




def sanitizeDates_numbers(date):
    #make everything into year-month-day
    month = date[0:2]
    day = date[3:5]
    year = date[6:10]
    sanitized = year + "-" + month + "-" + day
    return sanitized
    

def sanitizeDates_letters(date):
    month_list = ['Jan','Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    date = date.split(':')
    print(len(date))
    if(len(date) < 2):
        return ""
    date = date[1]
    if(len(date) > 5):
        date = date[1:]
        date = date.replace(',', '')
        date = date.split(' ')
        month = date[0]
        day = date[1]
        if(int(day) < 10):
            day = "0" + str(day)
        year = date[2]

        for i in range(len(month_list)):
            if(month == month_list[i]):
                if(i < 10):
                    month = "0" + str(i + 1)
                else:
                    month = i + 1
                break

        sanitized = year + "-" + month + "-" + day
        return sanitized
    else:
        return ""


tickerdates = pd.DataFrame([], columns=['Symbol', 'Upcoming Earning Date', 'Past Earning 1', 'Past Earning 2', 'Past Earning 3',
                                           'Past Earning 4'])

for i in range(len(data)):
    earning_dates = []
    count = 0
    
    ticker = ticker_list.iat[i,0]
    print(ticker)
    ticker = ticker.lower()
    
    URL = "https://www.nasdaq.com/market-activity/stocks/" + ticker + "/earnings"
    print(URL)
    driver.get(URL)
    #driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[0])
    find_new_earning = driver.find_elements(By.XPATH, "//h2[@class='module-header']")
    print(len(find_new_earning))
    #for i, _ in enumerate(find_new_earning):
    
    date = find_new_earning[0].get_attribute('innerHTML')
    date = sanitizeDates_letters(date)
    print(date)
    earning_dates.append(date)

    find_past_earning = driver.find_elements(By.XPATH, "//td[@class='earnings-surprise__table-cell']")

    print(len(find_past_earning))

    if(len(find_past_earning) < 16):
        continue
    
    for j in range(len(find_past_earning)):
        if(j % 4 == 0):
            date = sanitizeDates_numbers(find_past_earning[j].get_attribute('innerHTML'))
            print(date)
            earning_dates.append(date)

    print(earning_dates)

    ticker_data = {
        'Symbol' : ticker,
        'Upcoming Earning Date' : earning_dates[0],
        'Past Earning 1' : earning_dates[1],
        'Past Earning 2' : earning_dates[2],
        'Past Earning 3' : earning_dates[3],
        'Past Earning 4' : earning_dates[4]
        }
    tickerdates.loc[i] = pd.Series(ticker_data)

    #df = pd.DataFrame([ticker_data])
    
tickerdates.to_csv('/Users/alanyang/Desktop/earningdata.csv', mode='a', index = False, header = True)

driver.quit()
    #save into csv file

    
























