# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 00:42:20 2022

@author: osama
"""

#Data Analyses Functions 
import pandas as pd
from datetime import datetime

def Data_Daily_Spread(File_Name):
    Data_In = pd.read_csv('./%s.csv'%File_Name)
    Data_In = Data_In.set_index(['Date'])
    Data_In.index = pd.to_datetime(Data_In.index, unit = 'ns')
    Data_Out_df = Data_In.resample('D').mean()
    Data_Out_df.to_csv('./%s_daily.csv'%File_Name)
def Data_to_Monthly(File_Name,method):
    Data_In = pd.read_csv('./%s.csv'%File_Name)
    #Set date as index 
    Data_In = Data_In.set_index('Date')
    Data_In.index = pd.to_datetime(Data_In.index, unit = 'ns')
    #convert time series to monthly (mean, or sum)
    if method == 'mean':
        Data_Monthly = Data_In.resample('M').mean()
    elif method == 'sum':
        Data_Monthly = Data_In.resample('M').sum()
    #Export weekly average TP concentrations
    Data_Monthly.to_csv('./%s_Monthly.csv'%File_Name)
def Data_Merge(File_Names):
    File_Names_df = pd.read_csv('./%s.csv'%File_Names)
    Data_0 = pd.read_csv('./%s.csv'%File_Names_df['File_Names'].iloc[0])
    Data_1 = pd.read_csv('./%s.csv'%File_Names_df['File_Names'].iloc[1])
    Data_Merge = pd.merge(Data_0,Data_1, how = 'outer', on = 'Date')
    for i in range (2, len(File_Names_df.index)):
        Data = pd.read_csv('./%s.csv'%File_Names_df['File_Names'].iloc[i])
        Data_Merge = Data_Merge.merge(Data, how = 'outer', on = 'Date')
    Data_Merge.to_csv('./Data_Merged.csv')
def Define_Date_Range(File_Name, start_year, start_month, start_day, end_year, end_month, end_day):
    #Identify the date ranges
    startyear = start_year
    startmonth = start_month
    startday = start_day
    endyear = end_year
    endmonth = end_month
    endday = end_day

    startdate = startyear,startmonth,startday 
    year, month, day = map(int, startdate)
    startdate = datetime(year, month, day).date() 
    enddate = endyear,endmonth,endday 
    year, month, day = map(int, enddate)
    enddate = datetime(year, month, day).date() 
   
    Data = pd.read_csv('./%s.csv'%File_Name)
    Data['Date'] = pd.to_datetime(Data['Date'])
    mask = ((Data['Date'] >= startdate) & (Data['Date'] <= enddate))
    Data_Date_Range = Data.loc[mask]
    Data_Date_Range.to_csv('./%s_%s-%s-%s_%s-%s-%s.csv'% (File_Name,start_year,start_month,start_day,end_year,end_month,end_day))
    
