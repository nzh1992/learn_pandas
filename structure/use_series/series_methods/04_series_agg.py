# -*- coding: utf-8 -*-
"""
Author: niziheng
Created Date: 2021/5/23
Last Modified: 2021/5/23
Description: 聚合函数
"""
import pandas as pd


s1 = pd.Series([pd.NA, 1, 2, 3, 4])

# agg(func=None, axis=0, *args, **kwargs):
# func表示用于聚合操作的函数名，可以接受function，str，list 或者 dict。

# 1. func is function
def get_first(s):
    """
    获取第一个大于3的非空值
    :param s: series的一个元素
    :return:
    """
    if not pd.isna(s) and s > 3:
        return s


# 通过agg调用自定义函数，会对每个元素都执行一次get_first
# 效果类似于apply函数
s2 = s1.agg(get_first)
# print(s2)       # output: Series([NaN, NaN, NaN, NaN, 4.0])

# 2. 自带聚合函数
s3 = s1.agg('max')

# 3. 多维度聚合
s4 = s1.agg(['max', 'min', 'mean'])
print(s4)
