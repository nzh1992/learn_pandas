"""
created by nzh
Date: 2020-01-12 13:48
"""
import numpy as np
import pandas as pd

from basic_use.create_data import create_data_frame, get_dates

df = create_data_frame()

# 1. 分解DataFrame
# 1.1 按行分解
pieces_for_index = [df[0:2], df[2:4]]
for i in pieces_for_index:
    # print(i)
    pass

# 1.2 按列分解
pieces_for_column = [df.iloc[:, 0:2], df.iloc[:, 2:4]]
for i in pieces_for_column:
    # print(i)
    pass

# 2. 合并DataFrame
# 2.1 按行合并
concat_by_index = pd.concat(pieces_for_index)
# print(concat_by_index)

# 2.2 按列合并
concat_by_column = pd.concat(pieces_for_column, axis=1)
# print(concat_by_column)

# 3. 连接(merge)
left_df = pd.DataFrame({'key': ['foo1', 'foo2'], 'lval': [1, 2]})
right_df = pd.DataFrame({'key': ['foo1', 'foo2'], 'rval': [4, 5]})

merge_df = pd.merge(left_df, right_df, on='key')
# print(merge_df)

# 4. 追加(append)
# df.append方法返回一个新的df
df2 = pd.DataFrame(np.random.randn(8, 4), columns=list('ABCD'))
print(df2)
series = df2.iloc[3]
print(series)

df3 = df2.append(series, ignore_index=True)
print(df3)