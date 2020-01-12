"""
created by nzh
Date: 2020-01-12 11:43
"""

import numpy as np
import pandas as pd

# 学习如何处理缺失值

# pandas是用np.nan表示缺失数据，计算时，默认不包含空值。

# 构建示例DataFrame
dates = pd.date_range('20180101', periods=6)
# print(dates)
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
print(df)

# 1. 重建索引(reindex)
df2 = df.reindex(index=dates[0:4], columns=list(df.columns) + ['E'])
# print(df2)
df2.loc[dates[0]:dates[1], 'E'] = 1
# print(df2)
# 删除所有包含'缺失值'的行
# 注意：dropna方法会返回一个新的DataFrame对象，而非更改原对象
df3 = df2.dropna(how='any')
# print(df3)

# 填充所有'缺失值', fillna方法也会返回一个新的DataFrame对象
df4 = df2.fillna(value=8.8888)
# print(df4)

# 提取布尔掩码（全是True/False的DataFrame）, np.nan会被标记为True
bool_df = pd.isna(df2)
# print(bool_df)