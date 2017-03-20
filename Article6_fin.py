#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 18:20:04 2017

@author: Alex
"""


import pandas as pd
import statsmodels.api as sm
import numpy as np
import matplotlib
from scipy.stats import wilcoxon

df = pd.read_csv("Morgan_6.csv")
X = pd.DataFrame()
X['DIFF'] = df['DIFF']


t_value, p_value = wilcoxon(X['DIFF'], y=None, zero_method="zsplit")
print(t_value)
print(p_value)