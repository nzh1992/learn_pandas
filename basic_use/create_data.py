"""
created by nzh
Date: 2020-01-12 12:06
"""

import numpy as np
import pandas as pd


def create_data_frame():
    """
    构造示例DataFrame
    :return: DataFrame
    """
    # 用日期构建index
    dates = pd.date_range('20180101', periods=6)
    # print(dates)
    df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))

    return df

def get_dates(num=6):
    return pd.date_range('20180101', periods=num)