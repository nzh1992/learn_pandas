# -*- coding: utf-8 -*-
"""
Author: niziheng
Created Date: 2021/5/22
Last Modified: 2021/5/22
Description: 
"""
import pandas as pd

# 2. add(other, level=None, fill_value=None, axis=0):
# 加法操作。如果other是个series，那么会对对应索引的数值进行相加，若长度不相同，用np.nan替代。
s1 = pd.Series([1, 2, 3, 4])
other1 = pd.Series([5, 6])
result1 = s1.add(other1)

# 如果other是个数值，那么series中的每个元素都会和这个数值相加。
other2 = 5
result2 = s1.add(other2)

# other 还可以是list, tuple。但是长度必须和series相同。
other3 = [7, 8, 9, 10]
result3 = s1.add(other3)

other4 = (7, 8, 9, 10)
result4 = s1.add(other4)

# 如果other是Series类型，通过指定fill_value参数，可以填充缺失值
# 比如other1会被填充为Series([5, 6, 0, 0])再计算
result5 = s1.add(other1, fill_value=0)

# level没有效果，作用未知
result6 = s1.add(other1, level='3')
print(result6)