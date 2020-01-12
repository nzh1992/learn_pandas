"""
created by nzh
Date: 2020-01-12 12:03
"""

import numpy as np
import pandas as pd

from basic_use.create_data import create_data_frame, get_dates

# 学习如何对DataFrame进行运算

# 注意：运算时，一般会排除'缺失值'

# 创建示例DataFrame
df = create_data_frame()
print(df)

# 1. 统计
# 1.1 描述性统计
# 按列统计
df_mean_by_column = df.mean()
# print(df_mean_by_column)

# 按行统计
df_mean_by_index = df.mean(1)
# print(df_mean_by_index)

# 2. 偏移函数shift
# shift其实就是移动series中的index，没有值的位置用np.nan填充
dates = get_dates(num=4)
series = pd.Series([1,3, np.nan, 6], index=dates)
# print(series)
series_shift_2 = series.shift(2)
# print("series_shift_2: \n", series_shift_2, end="")

df_sub = df.sub(series_shift_2, axis='index')
# print("df_sub: \n", df_sub, end="")

# 3. Apply函数
# 和python的map函数有点像，对数据集中的元素依次操作
total = df.apply(np.cumsum)
# print(total)

# 按列求极差(最大值-最小值), axis=0表示列优先，axis=1表示行优先
# lambda中的x参数其实接受的是，每一列的数据
column_range = df.apply(lambda x: x.max() - x.min(), axis=0)
# print(column_range)

# 按行求极差(最大值-最小值)
index_range = df.apply(lambda x: x.max() - x.min(), axis=1)
# print(index_range)

# 4. 直方图
series2 = pd.Series(np.random.randint(0, 7, size=10))
# print(series2)
# value_counts方法，统计了每个值出现的次数
t = series2.value_counts()
# print(t)

# 5. 字符串方法
series3 = pd.Series(['A', 'B', 'C', 'Aaba', 'Baca', np.nan, 'CABA', 'dog', 'cat'])
series3_lower = series3.str.lower()
print(series3_lower)
