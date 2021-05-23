# -*- coding: utf-8 -*-
"""
Author: niziheng
Created Date: 2021/5/23
Last Modified: 2021/5/23
Description: add_prefix, add_suffix
"""
import pandas as pd


my_series = pd.Series([1, 2, 3, 4])

# add_prefix(prefix):
# 给索引添加前缀'aaa_'
s2 = my_series.add_prefix(prefix='aaa_')
print(s2)


# add_suffix(suffix):
# 给索引添加后缀
s3 = my_series.add_suffix(suffix='_end')
print(s3)
