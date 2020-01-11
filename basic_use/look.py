"""
created by nzh
Date: 2020-01-11 14:54
"""

import numpy as np
import pandas as pd

# 学习查看DataFrame

# 先构造一个示例DataFrame
data = {
    'A': np.arange(start=1, stop=11, step=1),
    'B': np.arange(start=11, stop=21, step=1),
    'C': np.arange(start=21, stop=31, step=1),
    'D': np.arange(start=31, stop=41, step=1)
}
df = pd.DataFrame(data)

# 1. 查看前3行数据
# head方法，默认返回前5条
head_3 = df.head(n=3)
# print(head_3)

# 2. 查看后3行数据, 默认返回后5条
tail_3 = df.tail(n=3)
# print(tail_3)

# 3. 查看索引（index）
indexs = df.index
# print(indexs)         # output: RangeIndex(start=0, stop=10, step=1)

# 4. 查看列（column）
columns = df.columns
# print(columns)          # output: Index(['A','B', 'C','D'], dtype='object')

# 5. DaraFrame转为numpy（pandas 0.25, python 3.6.6不可用，没有to_numpy方法）
# data_numpy = df.to_numpy()
# print(data_numpy)

# 6. 快速查看数据的统计摘要
describe = df.describe()
# print(describe)

# 7. 查看转置数据(行转列，列转行)
df_t = df.T
# print(df_t)

# 8. 按轴排序
# axis参数为0时，按列排序。为1时，按行排序。
sort_by_index = df.sort_index(axis=0, ascending=False)
# print(sort_by_index)

# 9. 按值排序
sort_by_value = df.sort_values(by='C', ascending=False)
print(sort_by_value)