import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.preprocessing import StandardScaler


def read():
    temp_data = pd.read_csv("D:/360安全浏览器下载/demo案例附件/data.csv", encoding="gbk")
    print(temp_data.head())
    print(temp_data.shape)
    print(temp_data.describe())
    return temp_data


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


def preprocessing(temp_data):
    xs = temp_data.iloc[:, 4:]
    ys = temp_data.iloc[:, 3]
    temp_x_train, temp_x_test, temp_y_train, temp_y_test = \
        train_test_split(xs, ys, random_state=420)
    temp_x_train.index = range(len(temp_x_train.index))
    temp_y_train.index = range(len(temp_y_train.index))
    temp_x_test.index = range(len(temp_x_test.index))
    temp_y_test.index = range(len(temp_y_test.index))
    print(temp_x_train)
    print(temp_y_train)
    # scale = StandardScaler()
    # scale.fit(x_train)
    # x_train=scale.transform(x_train)
    # y_train=scale.transform(y_train)
    return temp_x_train, temp_x_test, temp_y_train, temp_y_test


if __name__ == '__main__':
    data = read()
    print(data.columns)
    data = fill_nan(data)
    data = set_ys(data)
    print(data.iloc[:, 3])
    new_data = data.copy()
    x_train, x_test, y_train, y_test = preprocessing(new_data)

    clf = LogisticRegression(random_state=420, penalty="l2", max_iter=100,
                             class_weight="auto", n_jobs=-1,
                             solver="lbfgs").fit(x_train, y_train)

    print(clf.score(x_test, y_test))
    scores = cross_val_score(clf, x_train, y_train, cv=5)
    print(scores)
    # para_grid = {}
    # grid_search = GridSearchCV(clf, para_grid, cv=5,
    #                            scoring='neg_mean_squared_error')
    clf_xgb = GradientBoostingClassifier(random_state=420) \
        .fit(x_train, y_train)
    print(clf_xgb.score(x_test, y_test))
    scores = cross_val_score(clf_xgb, x_train, y_train, cv=5)
    print(scores.mean())
