"""
created by nzh
Date: 2020-01-12 14:52
"""
import numpy as np
import pandas as pd

from basic_use.create_data import create_data_frame, get_dates


# 学习如何使用分组

# 分组
# 1. 分割：按照条件将df分割为多组
# 2. 应用：为每组单独应用函数
# 3. 组合：将处理的结果组合成一个数据结构(一般是DataFrame)

data = {
    'A': ['foo', 'bar', 'foo', 'bar', 'foo', 'bar', 'foo', 'foo'],
    'B': ['one', 'one', 'two', 'three', 'two', 'two', 'one', 'three'],
    'C': np.random.randn(8),
    'D': np.random.randn(8)
}
df = pd.DataFrame(data)
print(df)

group_a_sum = df.groupby('A').sum()
print(group_a_sum)

group_ab_sum = df.groupby(list('AB')).sum()
print(group_ab_sum)