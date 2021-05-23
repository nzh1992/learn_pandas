# -*- coding: utf-8 -*-
"""
Author: niziheng
Created Date: 2021/5/22
Last Modified: 2021/5/22
Description: Series的方法
"""
import pandas as pd


my_series = pd.Series([1, 2, 3, -4])

# 1. abs():
# 对series中的每个元素取绝对值
my_series_abs = my_series.abs()

# 2. add(other, level=None, fill_value=None, axis=0):
# 加法操作。如果other是个series，那么会对对应索引的数值进行相加。
# 如果other是个数值，那么series中的每个元素都会和这个数值相加。
my_series2 = pd.Series([5, 6, 7])
my_series3 = my_series.add(my_series2)
print(my_series3)

