# -*- coding: utf-8 -*-
"""
Author: niziheng
Created Date: 2021/5/22
Last Modified: 2021/5/22
Description: 
"""
import numpy as np
import pandas as pd


my_series = pd.Series([1, 2, 3, 4])

# 20. ndim: 返回一个整数，用于表示series的维度
my_series_ndim = my_series.ndim

# 21. shape: 返回一个元组，用于表示series的形状
my_series_shape = my_series.shape       # output: (4,)

# 22. size: 返回一个整数，用于表示series的长度
my_series_length = my_series.size       # output: 4

# 23. values: 返回等价的np.ndarray对象
my_series_values = my_series.values
