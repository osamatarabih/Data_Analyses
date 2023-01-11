# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 15:24:35 2022

@author: osama
"""

# This script spreads data that are collected on a time step that is greater than one day to be visiualized on a daily time step where 
# the gap data will be illustrated as blank, moreover, if multiple measures were collected on one day, the average of these measurements 
# will be determined.
# import required packages
import pandas as pd 
import os 
#Directory where the Script loactes
os.chdir('C:/Work/Research/Data Analysis/Tools/Python_Scripts')
from Data_Analyses_Fns import *
Working_dir = 'C:/Work/Research/LOONE/Nitrogen Module/Data' 
os.chdir('%s'%Working_dir) 


#Spread data
Data_Spread = Data_Daily_Spread('LZ40_AMMONIA-N')


#Determine Monthly Average data
Monthly_Data = Data_to_Monthly("LZ40_Chl-a",'mean')


#Determine Monthly Sum data
Monthly_Data = Data_to_Monthly("S308BK",'sum')


#Merge multiple time series data into One file with the same date index!
# File_Names = ['L001_NITRATE+NITRITE-N_Monthly', 'L004_NITRATE+NITRITE-N_Monthly', 'L005_NITRATE+NITRITE-N_Monthly', 'L006_NITRATE+NITRITE-N_Monthly', 'L007_NITRATE+NITRITE-N_Monthly', 'L008_NITRATE+NITRITE-N_Monthly', 'LZ40_NITRATE+NITRITE-N_Monthly']
File_Names = ['L001_Chl-a_Monthly', 'L004_Chl-a_Monthly','L005_Chl-a_Monthly', 'L006_Chl-a_Monthly','L007_Chl-a_Monthly', 'L008_Chl-a_Monthly','LZ40_Chl-a_Monthly']
File_Names_df = pd.DataFrame()
File_Names_df['File_Names'] = File_Names
File_Names_df.to_csv('./File_Names.csv')
Merge = Data_Merge('File_Names')


#Identify Date Range
LO_Inflows = Define_Date_Range("S154_AMMONIA-N_Monthly", 1991, 1, 1, 2020, 12, 31)


# Determine Organic N as (TKN - NH4_N)
File_Names = ['S65E_AMMONIA-N_Monthly', 'S65E_KJELDAHL NITROGEN, TOTAL_Monthly']
File_Names_df = pd.DataFrame()
File_Names_df['File_Names'] = File_Names
File_Names_df.to_csv('./File_Names.csv')
Merge = Data_Merge('File_Names')
