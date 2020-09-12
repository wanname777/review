import numpy as np
import pandas as pd


# cut、get_dummies、re方面未涉及


def demo_dropna():
    # 对于dropna，默认的axis是0，how是any
    data = pd.DataFrame([[1., 6.5, 3.],
                         [1., np.nan, np.nan],
                         [np.nan, np.nan, np.nan],
                         [np.nan, 6.5, 3.]])
    print(data)
    data1 = data.dropna(axis=0, how='all')
    print(data1)
    data2 = data.dropna(thresh=2)
    print(data2)


def demo_fillna():
    # fill_na的method有许多参数，比如ffill、bfill等
    # 同样的，他也可以设置inplace、limit等参数
    df = pd.DataFrame(np.random.randn(7, 3))
    df.iloc[:4, 1] = np.nan
    df.iloc[:2, 2] = np.nan
    print(df)
    df1 = df.fillna({1: 0.5, 2: 0}, inplace=False)
    print(df1)
    df2 = df.fillna(method='bfill', limit=2)
    print(df2)


def demo_duplicated():
    # drop_duplicated在去重时可以只针对某一部分判定是为重复
    # 默认时全部重复，你也可以设置keep参数来修改保留值
    data = pd.DataFrame(
        {'k1': ['one', 'two'] * 3 + ['two'], 'k2': [1, 1, 2, 3, 3, 4, 4]})
    print(data)
    data['v1'] = range(7)
    print(data)
    data.drop_duplicates(['k1', 'k2'], keep='last', inplace=True)
    print(data)


def demo_replace():
    # replace主要是修改值，与fillna有些类似
    data = pd.Series([1., -999., 2., -999., -1000., 3.])
    print(data)
    data.replace({-999: np.nan, -1000: 0}, inplace=True)
    print(data)


def demo_rename():
    # 与reindex不同的是，reindex是修改顺序，而rename是修改名称
    data = pd.DataFrame(np.arange(12).reshape((3, 4)),
                        index=['Ohio', 'Colorado', 'New York'],
                        columns=['one', 'two', 'three', 'four'])
    print(data)
    data.rename(index=str.title, columns=str.upper, inplace=True)
    print(data)


if __name__ == '__main__':
    demo_dropna()
    demo_fillna()
    demo_duplicated()
    demo_replace()
    demo_rename()
