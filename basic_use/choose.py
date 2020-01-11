"""
created by nzh
Date: 2020-01-11 15:17
"""
import numpy as np
import pandas as pd

# 学习如何选择数据

# 构造一个示例DataFrame
data = {
    'A': np.random.rand(10),
    'B': np.random.rand(10),
    'C': np.random.rand(10),
    'D': np.random.rand(10)
}
df = pd.DataFrame(data)
# print(df)

# 1. 选择单列
# 结果会生成一个Series
series_b = df['B']
# print(series_b)
# 等效于df.B
# print(df.B)

# 2. 选择某一行
# 这里需要使用切片，切的是index，而非column。
# 并且和python的切片一样，取值范围遵循"左闭右开"。
index_3 = df[3:4]
# print(index_3)

# 3. 按标签选择
# 3.1 用标签提取一行数据
# loc中的值，对应的是index。
row1 = df.loc[1]
# print(row1)

# 3.2 用标签选择多列数据
# df.loc[index列表，标签列表]
row2 = df.loc[[0, 1, 2, 3], ['A', 'B']]
# print(row2)

# 3.3 用标签切片
# df.loc[index切片, 标签列表]
row3 = df.loc[0:4, ['A', 'C']]
# print(row3)

# 3.4 返回对象降维
# 降维：df是二维数组， 但是如果index只有一行就会降维到一维数组
# 只需在index的位置传单个index即可
row4 = df.loc[0, ['A', 'B']]
# print(row4)

# 3.5 提取标量值(scalar)
scalar1 = df.loc[0, 'A']
# print(scalar1)

# 3.6 快速访问标量值
scalar2 = df.at[0, 'A']
# print(scalar2)


# 4. 按位置选择(df.iloc, 整数)
# 4.1 用整数位置选择(降维)
row5 = df.iloc[3]
# print(row5)

# 4.2 整数切片
row6 = df.iloc[3:5, 0:2]
# print(row6)

# 4.3 整行切片
row7 = df.iloc[3:5, :]
# print(row7)

# 4.4 显示提取值（访问标量值）
scalar3 = df.iloc[0, 0]
# print(scalar3)

# 4.5 快速访问标量值，同df.iloc[0, 0]
scalar4 = df.iat[0, 0]
# print(scalar4)


# 5. 布尔索引
# 5.1 用单列的值选择数据
df2 = df[df.A > 0.2]
# print(df2)

# 5.2 选择df中满足条件的值
# 若不满足条件的值，会用np.nan替换
df3 = df[df > 0.2]
# print(df3)

# 5.3 用isin()筛选
df4 = df.copy()
# 添加一列
df4['E'] = ['one', 'two', 'three', 'four', 'five',
            'six', 'seven', 'eight', 'nine', 'ten']
# print(df4)
# 选取某一列中的值所在的行
df5 = df4[df4['E'].isin(['two', 'five'])]
# print(df5)

# output:
#           A         B         C         D     E
# 1  0.679004  0.686674  0.670696  0.263404   two
# 4  0.748827  0.353744  0.381654  0.661387  five

# 6. 赋值
# 6.1 用索引自动对齐新增列的数据
# 若s1长度大于df长度，则根据df长度截取。若s1长度小于df长度，则会用np.nan补齐。
s1 = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], index=np.arange(0, 11))
# print(s1)
df4['F'] = s1
# print(df4)

# 6.2 按标签赋值
df4.at[0, 'F'] = 100
# print(df4)

# 6.3 按位置赋值
df4.iat[0, 5] = 99
# print(df4)

# 6.4 按numpy.array赋值
arr = np.array([888] * len(df4))
df4.loc[:, 'F'] = arr
# print(df4)

# 6.5 用where条件赋值
df5 = df4.copy()
# print(df5)
# 去掉'E'，'F'这两列，axis=1表示列
df6 = df5.drop(columns=['E', 'F'], axis=1)
# print(df6)
# 选取df6中大于0.6的值，并赋值为原来值的相反数
df6[df6 > 0.6] = -df6
print(df6)
