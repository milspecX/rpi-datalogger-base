#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 10:08:30 2020

@author: rw
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy.interpolate import CubicSpline

data = pd.read_csv('/Users/rw/Desktop/data_log_04252020.csv')
x = data['Date']
y = data['Time']
z = data['Reading']

plt.figure()
plt.plot(y, z, linewidth=2.5)