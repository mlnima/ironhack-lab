# uti module
import pandas as pd
import numpy as np


def categorical_numerical_spliter(df):
    numerical = df.select_dtypes(include=np.number)
    categorical = df.select_dtypes(include=object)
    return numerical, categorical


def xY_spliter(df, y_column):
    x = df.drop(y_column, axis=1)
    y = df.total_claim_amount
    x = x._get_numeric_data()
    return x, y


def test_train_data_spliter(X, Y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.30, random_state=123)
    return X_train, X_test, y_train, y_test
