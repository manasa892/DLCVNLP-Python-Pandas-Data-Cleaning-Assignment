# -*- coding: utf-8 -*-


#Data Cleaning Assignment - Problem Statement 
import pandas as pd
import numpy as np

df = pd.DataFrame({'From_To' : ['LonDon_paris','MAdrid_miLAN','londON_StockOlm',
                    'Budapest_PaRis','Brussels_londOn'],
                   'FlightNumber':[10045,np.nan,10065,np.nan,10085],
                   'RecentDelays': [[23,47],[],[24,43,87],[13],[67,32]],
                   'Airline': ['KLM(!)','<Air France>(12)','(British Airways.)',
                             '12.AirForce',"Swiss Air"]})


df

#1.Some values in the the FlightNumber column are missing. These numbers are
#meant to increase by 10 with each row so 10055 and 10075 need to be put in
#place. Fill in these missing numbers and make the column an integer column
#(instead of a float column).


for i in range(1,df['FlightNumber'].count() + 1):
    if pd.isnull(df.loc[i,'FlightNumber']):
        df.loc[i,'FlightNumber'] = df.loc[i-1,'FlightNumber'] + 10
                                
df

#2. The From_To column would be better as two separate columns! Split each
#string on the underscore delimiter _ to give a new temporary DataFrame with
#the correct values. Assign the correct column names to this temporary
#DataFrame.

temp = df.From_To.str.split('_',expand = True)
temp.columns = ['From','To']
temp



#3. Notice how the capitalisation of the city names is all mixed up in this
#temporary DataFrame. Standardise the strings so that only the first letter is
#uppercase (e.g. "londON" should become "London".)

temp['From'] = temp['From'].str.capitalize()
temp['To'] = temp['To'].str.capitalize()
temp

#4. Delete the From_To column from df and attach the temporary DataFrame
#from the previous questions. 

df = df.drop('From_To',axis = 1)
df = df.join(temp)
df


#5. In the RecentDelays column, the values have been entered into the
#DataFrame as a list. We would like each first value in its own column, each 
#second value in its own column, and so on. If there isn't an Nth value, the value
#should be NaN.
#Expand the Series of lists into a DataFrame named delays, rename the columns
#delay_1, delay_2, etc. and replace the unwanted RecentDelays column in df
#with delays.

delays = df['RecentDelays'].apply(pd.Series)
delays.columns = ['delay_{}'.format(n) for n in range(1,len(delays.columns)+1)]
df = df.drop('RecentDelays',axis = 1).join(delays)
df
