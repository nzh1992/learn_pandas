"""
created by nzh
Date: 2020-01-11 12:51
"""

import numpy as np
import pandas as pd

# Pandas核心数据结构DataFrame
# 带有标签的二维数组

# 1. 创建DataFrame
# 1.1 多个Series
data1 = {'a': 1, 'b': 2, 'c': 3}
series1 = pd.Series(data1)

data2 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
series2 = pd.Series(data2)

data3 = {'one': series1, 'two': series2}
df1 = pd.DataFrame(data3)

# 'd' 'one' 位置缺少的值会插入np.nan
# missing_data = df1['one']['d']
# print(np.isnan(missing_data))     # output: True

# 1.2 字典
data4 = {
    'one': pd.Series([1, 2, 3], index=['a', 'b', 'c']),
    'two': pd.Series([4, 5, 6, 7], index=['a', 'b', 'c', 'd'])
}
df2 = pd.DataFrame(data4)
# print(df2)

# output:
#    one  two
# a  1.0    4
# b  2.0    5
# c  3.0    6
# d  NaN    7

# 为什么'one'列的数据都变成了float类型？
# 因为np.nan是float类型，而Series和ndarray一样，支持同构数据，所以int类型被隐式转换为float类型。

# 生成DataFrame时，还可以指定保留哪些行和列
df3 = pd.DataFrame(data4, index=['b', 'c'], columns=['one'])

# 如果要保留的列没有值，则会用np.nan填充
df4 = pd.DataFrame(data4, index=['b', 'c', 'e'], columns=['one', 'two', 'three'])
# print(df4)

# output:
#    one  two three
# b  2.0  5.0   NaN
# c  3.0  6.0   NaN
# e  NaN  NaN   NaN

# 1.3 多为数组字典
# 若未传递index参数，则行标签是range(len(data['one']))
# 注意：其中'one'和'two'的长度必须相同，否则引发ValueError异常。
data5 = {
    'one': [1, 2, 3, 4],
    'two': [5, 6, 7, 8]
}
df5 = pd.DataFrame(data5)
# print(df5)

# 1.4 结构多维数组
data6 = np.zeros((2,), dtype=[('A', 'i4'), ('B', 'f4'), ('C', 'a10')])
# print(data6)
data6[:] = [(1, 2., 'hello'), (2, 3., 'world')]
# print(data6)

df6 = pd.DataFrame(data6, index=['first', 'second'])
# print(df6)

# 注意: 如果传入了column参数，会根据data6中的key('A','B','C')调整数据的位置
# 数据是跟着标签走的
df7 = pd.DataFrame(data6, columns=['C', 'B', 'A'])
# print(df7)

# output:
#           C    B  A
# 0  b'hello'  2.0  1
# 1  b'world'  3.0  2

# 1.5 列表字典
data8 = [
    {'a': 1, 'b': 2, 'c': 3},
    {'a': 10, 'b': 20, 'c': 30}
]
df8 = pd.DataFrame(data8)
print(df8)

# output:
#     a   b   c
# 0   1   2   3
# 1  10  20  30
