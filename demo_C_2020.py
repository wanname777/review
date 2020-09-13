import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


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
    temp_data.loc[temp_data["是否违约"] == "是", "是否违约"] = 1
    temp_data.loc[temp_data["是否违约"] == "否", "是否违约"] = 0
    print(temp_data.head()["是否违约"])
    return temp_data


if __name__ == '__main__':
    data = read()
    print(data.columns)
    data = fill_nan(data)
    data = set_ys(data)
    print(data.iloc[:, 3])
