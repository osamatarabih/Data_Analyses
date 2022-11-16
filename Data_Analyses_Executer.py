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

Data_Spread = Data_Daily_Spread('LZ40_AMMONIA-N')
