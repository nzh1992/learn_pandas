# -*- coding: utf-8 -*-
"""
Author: niziheng
Created Date: 2021/5/22
Last Modified: 2021/5/22
Description: 
"""
import pandas as pd


my_series = pd.Series([1, 2, 3, -4])

# 1. abs():
# 对series中的每个元素取绝对值
my_series_abs = my_series.abs()
print(my_series_abs)