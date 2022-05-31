#!/usr/bin/env python
# coding: utf-8

# In[10]:


import pandas as pd
import numpy as np

dataRaces = pd.read_csv('races.csv')
countOfMostRaceName=dataRaces['name'].value_counts().max()
mostCommonRaceName=dataRaces['name'].mode()[0]
print('Race')
print('-'*10)
print("the most Frequent race name is " + mostCommonRaceName)
print("the count Of the most Frequent Race Name " , countOfMostRaceName)
print('-'*40)
print()

dataCircuits = pd.read_csv('circuits.csv')
mostCommoncircuitsName=dataCircuits['country'].mode()[0]
countOfMostcircuitName=dataCircuits['country'].value_counts().max()
print('Circuit')
print('-'*10)
print("the most common circuit's country is " + mostCommoncircuitsName)
print("the count of circuits in this country " , countOfMostcircuitName)
print('-'*40)
print()

dataDrivers = pd.read_csv('drivers.csv')
mostCommonDriverNationality=dataDrivers['nationality'].mode()[0]
countOfMostDriverNationality=dataDrivers['nationality'].value_counts().max()
print('Driver')
print('-'*10)
print("the the most common Driver's nationality is is " + mostCommonDriverNationality)
print("the count of the most Frequent constructor's nationality " , countOfMostDriverNationality)
print('-'*40)
print()

dC = pd.read_csv('constructors.csv')
dCf=dC['nationality']
countOfMostConstructornationality=dCf.value_counts().max()
mostCommonConstructorsnationality=dCf.mode()[0]
print('Constructor')
print('-'*10)
print("the most Frequent constructor's nationality is " + mostCommonConstructorsnationality)
print("the count of the most Frequent constructor's nationality " , countOfMostConstructornationality)
print('-'*40)

df=pd.read_csv('races.csv')
def time_stats(df):
    print('\nCalculating The Most Frequent Times of races...\n')    
    df['date'] = pd.to_datetime(df['date'])
    df['year'] = df['date'].dt.year
    countOfMostCommonYear=df['year'].value_counts().max()
    mostCommonYear=df['year'].mode()[0]
    print('YEAR')
    print('-'*10)
    print('The most common Year          :   ', mostCommonYear) 
    print('The count of the most Frequent common Year :   ',countOfMostCommonYear)
    print()

    df['date'] = pd.to_datetime(df['date'])
    df['month'] = df['date'].dt.month
    countOfMostCommonMonth=df['month'].value_counts().max()
    mostCommonMonth=df['month'].mode()[0]
    print('MONTH')
    print('-'*10)
    print('The most common Month          :   ', mostCommonMonth) 
    print('The count of the most Frequent common Month :   ',countOfMostCommonMonth)
    print()

    #------------------------------******************************************************************************
    # display the most common day of week
    # extract day from week from Start Time to create new columns
    df['day'] = df['date'].dt.day_name()
    countOfMostCommonDay=df['day'].value_counts().max()
    mostCommonDay=df['day'].mode()[0]
    print('DAY')
    print('-'*10)
    print('The most common Day            :   ',mostCommonDay)
    print('The count of most common Day   :   ',countOfMostCommonDay)
    print('-'*40)
time_stats(df)


# In[ ]:





# In[ ]:




