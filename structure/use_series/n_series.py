"""
created by nzh
Date: 2020-01-11 12:34
"""
import numpy as np
import pandas as pd

# Pandas核心数据结构Series
# 带有标签的一维组数

# 1. 创建Series
# 1.1 字典
# 默认情况下，使用key作为标签
# 注意：Series中标签的顺序为dict中key的插入顺序（pandas >= 0.23 && python >= 3.6）
# 注意：Series中标签的顺序为dict中key的升序排列（pandas < 0.23 || python < 3.6）
data1 = {'a': 1, 'b': 2, 'c': 3}
series1 = pd.Series(data1)

# 1.2 多维数组
# data的长度必须和index的长度一致
indexs2 = ['A', 'B', 'C']
data2 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]
series2 = pd.Series(data2, index=indexs2)

# 1.3 标量值
# 如果使用标量值创建Series，将以index确定长度，如果index未提供，长度为1
index3 = ['A', 'B', 'C', 'D']
data3 = 7
series3 = pd.Series(data3, index=index3)
print(series3)
