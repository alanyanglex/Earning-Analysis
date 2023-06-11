import numpy as np
import pandas as pd
import math


earning_dates = pd.read_csv('/Users/alanyang/Desktop/earningdata.csv')
ticker_list = pd.DataFrame(earning_dates, columns = ['Symbol'])
future_earning = pd.DataFrame(earning_dates, columns = ['Upcoming Earning Date'])
past_earning_1 = pd.DataFrame(earning_dates, columns = ['Past Earning 1'])
past_earning_2 = pd.DataFrame(earning_dates, columns = ['Past Earning 2'])
past_earning_3 = pd.DataFrame(earning_dates, columns = ['Past Earning 3'])
past_earning_4 = pd.DataFrame(earning_dates, columns = ['Past Earning 4'])


count = 0
total_pattern = 0
correct_guess = 0

for i in range(len(ticker_list)):
    #print(ticker_list.iat[i,0])
    #print(future_earning.iat[i,0])
    #try:
    #    print(math.isnan(future_earning.iat[i,0]))
    #    count += 1
    #except:
    #    print(False)

    ticker = ticker_list.iat[i,0]
    ticker = ticker.upper()

    ticker_csv = "/Users/alanyang/Desktop/Historical Stock Data/" + ticker + ".csv"

    historical_data = pd.read_csv(ticker_csv)
    date = pd.DataFrame(historical_data, columns = ['Date'])
    past_open = pd.DataFrame(historical_data, columns = ['Open'])
    past_close = pd.DataFrame(historical_data, columns = ['Close'])

    past1_loc = 0
    past2_loc = 0
    past3_loc = 0
    past4_loc = 0
    
    for j in range(len(historical_data)):
        #print(date.iat[j,0])
        if(past_earning_1.iat[i,0] == date.iat[j,0]):
            past1_loc = j
        if(past_earning_2.iat[i,0] == date.iat[j,0]):
            past2_loc = j
        if(past_earning_3.iat[i,0] == date.iat[j,0]):
            past3_loc = j
        if(past_earning_4.iat[i,0] == date.iat[j,0]):
            past4_loc = j
        if(past1_loc != 0 and past2_loc != 0 and past3_loc != 0 and past4_loc != 0):
            continue


    decrease_before_earning = False
    increase_after_earning = False
    increase_before_earning = False
    
    if((past_close.iat[past2_loc - 6,0] - past_close.iat[past2_loc - 1,0])/past_close.iat[past2_loc - 6,0] < -0.):
        decrease_before_earning = True
    if((past_open.iat[past2_loc - 1,0] - past_close.iat[past2_loc + 6,0])/past_open.iat[past2_loc - 1,0] > 0.1):
        increase_after_earning = True
    if(past_close.iat[past1_loc - 2,0] - past_close.iat[past1_loc - 25,0]/past_close.iat[past1_loc - 25,0] > 0.2):
        increase_before_earning = True

    if(decrease_before_earning == True and increase_after_earning == True and increase_before_earning == True):
        total_pattern += 1
        if((past_open.iat[past1_loc - 1,0] - past_close.iat[past1_loc + 1,0])/past_open.iat[past1_loc - 1,0] < 0):
            correct_guess += 1;
            print("GUESSED CORRECTLY")
        else:
            print("GUESSED INCORRECTLY")
        print((past_open.iat[past1_loc - 1,0] - past_close.iat[past1_loc + 1,0])/past_open.iat[past1_loc - 1,0])


    decrease_before_earning = False
    increase_after_earning = False
    increase_before_earning = False
    
    if((past_close.iat[past3_loc - 6,0] - past_close.iat[past3_loc - 1,0])/past_close.iat[past3_loc - 6,0] < -0.):
        decrease_before_earning = True
    if((past_open.iat[past3_loc - 1,0] - past_close.iat[past3_loc + 6,0])/past_open.iat[past3_loc - 1,0] > 0.1):
        increase_after_earning = True
    if(past_close.iat[past2_loc - 2,0] - past_close.iat[past2_loc - 25,0]/past_close.iat[past2_loc - 25,0] > 0.2):
        increase_before_earning = True

    if(decrease_before_earning == True and increase_after_earning == True and increase_before_earning == True):
        total_pattern += 1
        if((past_open.iat[past2_loc - 1,0] - past_close.iat[past2_loc + 1,0])/past_open.iat[past2_loc - 1,0] < 0):
            correct_guess += 1;
            print("GUESSED CORRECTLY")
        else:
            print("GUESSED INCORRECTLY")
        print((past_open.iat[past2_loc - 1,0] - past_close.iat[past2_loc + 1,0])/past_open.iat[past2_loc - 1,0])


    decrease_before_earning = False
    increase_after_earning = False
    increase_before_earning = False
    
    if((past_close.iat[past4_loc - 6,0] - past_close.iat[past4_loc - 1,0])/past_close.iat[past4_loc - 6,0] < -0.03):
        decrease_before_earning = True
    if((past_open.iat[past4_loc - 1,0] - past_close.iat[past4_loc + 6,0])/past_open.iat[past4_loc - 1,0] > 0.1):
        increase_after_earning = True
    if(past_close.iat[past3_loc - 2,0] - past_close.iat[past3_loc - 25,0]/past_close.iat[past3_loc - 25,0] > 0.2):
        increase_before_earning = True

    if(decrease_before_earning == True and increase_after_earning == True and increase_before_earning == True):
        total_pattern += 1
        if((past_open.iat[past3_loc - 1,0] - past_close.iat[past3_loc + 1,0])/past_open.iat[past3_loc - 1,0] < 0):
            correct_guess += 1;
            print("GUESSED CORRECTLY")
        else:
            print("GUESSED INCORRECTLY")
        print((past_open.iat[past3_loc - 1,0] - past_close.iat[past3_loc + 1,0])/past_open.iat[past3_loc - 1,0])


    try:
        if((past_close.iat[past1_loc - 6,0] - past_close.iat[past1_loc - 1,0])/past_close.iat[past1_loc - 6,0] < -0.):
            decrease_before_earning = True
        if((past_open.iat[past1_loc - 1,0] - past_close.iat[past1_loc + 6,0])/past_open.iat[past1_loc - 1,0] > 0.1):
            increase_after_earning = True
        if(past_close.iat[len(past_close) - 2,0] - past_close.iat[len(past_close) - 25,0]/past_close.iat[len(past_close) - 25,0] > 0.2):
            increase_before_earning = True

        if(decrease_before_earning == True and increase_after_earning == True and increase_before_earning == True):
            print(ticker)
            print(future_earning.iat[i,0])
    except:
        pass
    


print(total_pattern)
print(correct_guess)












