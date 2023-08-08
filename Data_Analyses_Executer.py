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
import numpy as np
import os 
#Directory where the Script loactes
os.chdir('C:/Work/Research/Data Analysis/Tools/Python_Scripts')
from Data_Analyses_Fns import *
# Working_dir = 'C:/Work/Research/LOONE/Nitrogen Module/Module_Inputs' 
Working_dir = 'C:/Work/Research/LOONE/Nitrogen Module/Model_Data_Filled_20082016' 
os.chdir('%s'%Working_dir) 


#Spread data
Data_Spread = Data_Daily_Spread('L008_DISSOLVED OXYGEN')


#Determine Monthly Average data
Monthly_Data = Data_to_Monthly("LO_Average_Chla_2000_2020",'mean')


#Determine Monthly Sum data
Monthly_Data = Data_to_Monthly("FISHCR_WH036",'sum')

#Annual Sum
Annual_Data = Data_to_Annual('LI_Q_monthly','sum')

#Merge multiple time series data into One file with the same date index!
# File_Names = ['S65Etotal','S84_Stotal','S71' ,'S72', 'S191', 'S127_C','S127_P','S129_C','S129_P','S133_P','S135_P','S135_C','FISHP','S154','S154C','S308DS','S2_P','S3_P','S4_P','S351','S352','S354','L8','INDUST','S77']
# File_Names = ['L001_Chl-a_Monthly', 'L004_Chl-a_Monthly','L005_Chl-a_Monthly', 'L006_Chl-a_Monthly','L007_Chl-a_Monthly', 'L008_Chl-a_Monthly','LZ40_Chl-a_Monthly']
# File_Names = ['LZ40_CHLOROPHYLL-A, CORRECTED', 'LZ40_CHLOROPHYLL-A(LC)']
# File_Names = ['L001_OP_Inter', 'L004_OP_Inter','L005_OP_Inter','L006_OP_Inter','L007_OP_Inter','L008_OP_Inter',
#               'LZ40_OP_Inter']
File_Names = ['LO_NO_Filled', 'LO_NH4_Filled']
File_Names_df = pd.DataFrame()
File_Names_df['File_Names'] = File_Names
File_Names_df.to_csv('./File_Names.csv')
Merge = Data_Merge('File_Names')

#List all files in a directory
allfiles = os.listdir()
#Identify Date Range
for i in allfiles:
    LO_Inflows = Csv_Date_Range("%s"%i, 2008, 1, 1, 2016, 12, 31)
Date_Identified = Csv_Date_Range("LO_NO_Filled.csv", 2000, 1, 1, 2016, 12, 31)
# Determine Organic N as (TKN - NH4_N)
File_Names = ['S65E_AMMONIA-N_Monthly', 'S65E_KJELDAHL NITROGEN, TOTAL_Monthly']
File_Names_df = pd.DataFrame()
File_Names_df['File_Names'] = File_Names
File_Names_df.to_csv('./File_Names.csv')
Merge = Data_Merge('File_Names')


# Assign one Reference Year to a set of years
date_rng_1yr = pd.date_range(start = '1/1/2020', end = '12/31/2020', freq ='D') 
date_rng_tot = pd.date_range(start = '1/1/2000', end = '12/31/2020', freq ='D') 
ReferenceYear = pd.DataFrame()
EntirePeriod = pd.DataFrame()
ReferenceYear['Date'] = date_rng_1yr
EntirePeriod['Date'] = date_rng_tot 
Simperioddays = len(EntirePeriod.index)
Oneyeardays = len(ReferenceYear.index)
#Read Data
PhotoPeriod_Oneyear = pd.read_csv('C:/Work/Research/LOONE/Nitrogen Module/PhotoPeriod.csv')
ReferenceYear['Data'] = PhotoPeriod_Oneyear['PhotoPeriod']

EntirePeriod_data = np.zeros(Simperioddays)
for i in range(Simperioddays):
    EntirePeriod_data[i] = Replicate_oneyear(ReferenceYear,EntirePeriod['Date'].iloc[i].year, EntirePeriod['Date'].iloc[i].timetuple().tm_yday)  
EntirePeriod_data_1 = [x for x in EntirePeriod_data if ~np.isnan(x)]
EntirePeriod['Data'] = EntirePeriod_data_1
EntirePeriod.to_csv('C:/Work/Research/LOONE/Nitrogen Module/PhotoPeriod_2000_2020.csv')

