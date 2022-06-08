#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 16 10:57:04 2022

@author: gideongiorgis
"""

import csv
#import numpy as np
#import pandas as pd
import matplotlib.pyplot as plt

Names = [] 
Values = []
MonthArr = []
Months = ['January', 'February', 'March', 'April', 'May', 'June','July', 'August', 'September', 'October', 'November', 'December']
Avg = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
Count = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
index = 0
num = 0.0
index2 = 0

with open('./MD_COVID-19_-_Total_Currently_Hospitalized_-_Acute_and_ICU.csv', 'r') as csv_file:
    data = csv.reader(csv_file, delimiter = ',')
    
    


    for row in reversed(list(data)):
           Names.append(row[1])
           Values.append(row[4])
           
Names.pop()
Values.pop()
print("Dates from CSV file put in array")
print(Names)
print(" ")
print(" ")
print(" ")
print("Number of hospital beds in same index as date")
print(Values)
print(" ")
print(" ")
print(" ")
           
for i in Names:
     numDates = Names[index]
     numDatesList = numDates.split('/')
     MonthArr.append(numDatesList[0])
     
     
     if MonthArr[index] == '01':
         Count[0]+=1.0
         MonthArr[index] = Months[0]
         numVal = Values[index]
         num = float(numVal)
         Avg[0] = Avg[0] + num
        
         
     elif MonthArr[index] == '02':
          Count[1]+=1.0
          MonthArr[index] = Months[1]
          numVal = Values[index]
          num = float(numVal)
          Avg[1] = (Avg[1] + num) 
         
         
     elif MonthArr[index] == '03':
         Count[2]+=1.0
         MonthArr[index] = Months[2]
         numVal = Values[index]
         num = float(numVal)
         Avg[2] = Avg[2] + num
         
             
     elif MonthArr[index] == '04':
         if numDatesList[1] != '02': #csv file has error on 04/02 date
             Count[3]+=1.0
             MonthArr[index] = Months[3]
             numVal = Values[index]
             num = float(numVal)
             Avg[3] = Avg[3] + num
         
                 
     elif MonthArr[index] == '05':
         Count[4]+=1.0
         MonthArr[index] = Months[4]
         numVal = Values[index]
         num = float(numVal)
         Avg[4] = Avg[4] + num
         
                     
     elif MonthArr[index] == '06':
         Count[5]+=1.0
         MonthArr[index] = Months[5]
         numVal = Values[index]
         num = float(numVal)
         Avg[5] = Avg[5] + num
         
                         
     elif MonthArr[index] == '07':
         Count[6]+=1.0
         MonthArr[index] = Months[6]
         numVal = Values[index]
         num = float(numVal)
         Avg[6] = Avg[6] + num
        
                             
     elif MonthArr[index] == '08':
         Count[7]+=1.0
         MonthArr[index] = Months[7]
         numVal = Values[index]
         num = float(numVal)
         Avg[7] = Avg[7] + num
        
                                 
     elif MonthArr[index] == '09':
         Count[8]+=1.0
         MonthArr[index] = Months[8]
         numVal = Values[index]
         num = float(numVal)
         Avg[8] = Avg[8] + num
         
         
     elif MonthArr[index] == '10':
         Count[9]+=1.0
         MonthArr[index] = Months[9]
         numVal = Values[index]
         num = float(numVal)
         Avg[9] = Avg[9] + num
         
         
     elif MonthArr[index] == '11':
         Count[10]+=1.0
         MonthArr[index] = Months[10]
         numVal = Values[index]
         num = float(numVal)
         Avg[10] = Avg[10] + num
         
         
     else:
         Count[11]+=1.0
         MonthArr[index] = Months[11]
         numVal = Values[index]
         num = float(numVal)
         Avg[11] = Avg[11] + num
         
             
     index+=1
 
for j in Avg:
    Avg[index2] = Avg[index2] / Count[index2]
    index2+=1

    
print("Average hospital beds per month (Jan-Dec)")
print(Avg)
print(" ")
print(" ")
print(" ")
   
            
  
plt.scatter(Months, Avg, color = 'g')
plt.xticks(rotation = 25)
plt.xlabel('Month')
plt.ylabel('Average Hospital Beds')
plt.title('Average Hospital Covid Beds', fontsize = 20)
  
plt.show()



AvgPhys = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
index3 = 0


for k in AvgPhys:
    AvgPhys[index3] = Avg[index3] / 10 #average physicians daily needed
    index3+=1
    
print("Physicans needed per month at the COVID hospital")
print(AvgPhys)
