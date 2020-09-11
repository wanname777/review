import numpy as np
import pandas as pd


def demo_series():
    obj = pd.Series(np.arange(0, 9).astype(np.float64),
                    index=[chr(ord('a') + i) for i in range(9)])
    print(obj)
    for i in zip(obj.index, obj.values):
        print(i)
    print(obj.isna().sum())
    obj1 = obj.copy()
    obj1 += obj1
    print(obj1)
    print(obj.name)
    # numpy数组可以拥有name和index.name
    obj.name = 'aa'
    print(obj)
    obj.index.name = 'bb'
    print(obj)


def demo_dataframe():
    data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada', 'Nevada'],
            'year': [2000, 2001, 2002, 2001, 2002, 2003],
            'pop': [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]}
    frame = pd.DataFrame(data, index=[chr(ord('a') + i) for i in
                                      range(len(data['year']))])
    print(frame)
    # 注意loc与iloc的使用
    print(frame.loc['a':'e', 'state'])
    print(frame.T)
    print(frame.columns)


def demo_reindex():
    # reindex只会修改index或者columns的顺序及对应值，不会产生新的值
    # 如果索引不存在，则默认是Nan
    data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada', 'Nevada'],
            'year': [2000, 2001, 2002, 2001, 2002, 2003],
            'pop': [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]}
    frame = pd.DataFrame(data)
    print(frame)
    frame1 = frame.reindex([0, 1, 3, 6])
    print(frame1)
    # 可以用method的ffill参数表示前置填充
    frame2 = frame.reindex(range(len(frame[frame.columns[0]]) + 1),
                           method='ffill')
    print(frame2)
    # reindex对columns也可以生效，不过需要手动输入参数，而且Index在操作时只能append Index才行
    frame3 = frame.reindex(columns=frame.columns.append(pd.Index(['aa'])))
    print(frame3)


def demo_drop():
    # drop可以去除某一列或某一行，不过需要用axis选项，而且这个去除只是暂时的，必须有值承接他
    # 如果不想承接，也可以用参数inplace=True来代替
    data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada', 'Nevada'],
            'year': [2000, 2001, 2002, 2001, 2002, 2003],
            'pop': [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]}
    frame = pd.DataFrame(data)
    frame = frame.drop(['state'], axis=1)
    print(frame)
    temp_a = pd.Series(['a', 'b', 'c', 'd'])
    print(temp_a.iloc[1:3])


def demo_add():
    # 对于pandas中的add函数，可以有fill_value参数进行填补缺失值
    # 这个缺失值对两边都生效，因此可能出现1+fill_value的情况
    df1 = pd.DataFrame(np.arange(12.).reshape(3, 4),
                       columns=[chr(ord('a') + i) for i in range(4)])
    print(df1)
    df2 = pd.DataFrame(np.arange(20.).reshape(4, 5),
                       columns=[chr(ord('a') + i) for i in range(5)])
    print(df2)
    print(df1 + df2)
    print(df1.add(df2, fill_value=-99))


def demo_mapping():
    # 有趣的apply函数与lambda函数
    # 需要注意的是，Series有map函数，而Dataframe是apply和applymap函数
    frame = pd.DataFrame(np.random.randn(4, 3), columns=list('bde'),
                         index=['Utah', 'Ohio', 'Texas', 'Oregon'])
    print(frame)
    frame1 = frame.apply(lambda x: x.max() - x.min(), axis=1)
    print(frame1)
    frame2 = frame.applymap(lambda x: '%.2f' % x)
    print(frame2)
    frame3 = frame.apply(
        lambda x: pd.Series([x.max(), x.min()], index=['max', 'min']), axis=1)
    print(frame3, type(frame3))


if __name__ == '__main__':
    demo_series()
    demo_dataframe()
    demo_reindex()
    demo_drop()
    demo_add()
    demo_mapping()
