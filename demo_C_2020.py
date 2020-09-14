import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression


def read():
    data = pd.read_csv("D:/360安全浏览器下载/demo案例附件/data.csv", encoding="gbk")
    print(data.head())
    print(data.shape)
    print(data.describe())
    return data


def fill_nan(temp_data):
    print(temp_data.isna().sum())
    all_data = temp_data.fillna(axis=1, method="ffill")
    print(all_data[all_data["企业代号"] == "E69"]["('金额', 'std')_x"])
    return all_data


def set_ys(temp_data):
    temp_data.loc[temp_data["是否违约"] == "是", "是否违约"] = 1.
    temp_data.loc[temp_data["是否违约"] == "否", "是否违约"] = 0.
    temp_data.iloc[:, 3] = temp_data.iloc[:, 3].astype(np.float64)
    print(temp_data.head()["是否违约"])
    return temp_data


if __name__ == '__main__':
    data = read()
    print(data.columns)
    data = fill_nan(data)
    data = set_ys(data)
    print(data.iloc[:, 3])
    new_data = data.copy()
    xs = new_data.iloc[:, 4:]
    ys = new_data.iloc[:, 3]
    x_train, x_test, y_train, y_test = train_test_split(xs, ys,
                                                        random_state=420)
    x_train.index = range(len(x_train.index))
    y_train.index = range(len(y_train.index))
    x_test.index = range(len(x_test.index))
    y_test.index = range(len(y_test.index))
    print(x_train)
    print(y_train)
    clf = LogisticRegression(random_state=420, penalty="l2", max_iter=100).fit(
        x_train, y_train)
    print(clf.score(x_test, y_test))
