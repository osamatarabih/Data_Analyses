# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 00:42:20 2022

@author: osama
"""

#Data Analyses Functions 
import pandas as pd
def Data_Daily_Spread(File_Name):
    Data_In = pd.read_csv('./%s.csv'%File_Name)
    Data_In = Data_In.set_index(['Date'])
    Data_In.index = pd.to_datetime(Data_In.index, unit = 'ns')
    Data_Out_df = Data_In.resample('D').mean()
    Data_Out_df.to_csv('./%s_daily.csv'%File_Name)