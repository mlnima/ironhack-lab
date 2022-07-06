import numpy as np
import pandas as pd
import scipy.stats
from scipy.stats import t
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error as mse
from sklearn.metrics import mean_absolute_error as mae
import matplotlib.pyplot as plt
import json
from IPython.display import Markdown
from IPython.display import JSON



def df_spliter_by_data_type(df):
    numerical = df.select_dtypes(include=np.number)
    categorical = df.select_dtypes(include=object)
    return numerical, categorical


def y_from_x_spliter(df, y_column):
    X = df.drop(y_column, axis=1)
    Y = df[y_column]
    # x = x._get_numeric_data()
    return X, Y


def outliers_remover(df):
    cor_matrix = df.corr().abs()
    upper_tri = cor_matrix.where(np.triu(np.ones(cor_matrix.shape), k=1).astype(bool))
    to_drop = [column for column in upper_tri.columns if any(upper_tri[column] > 0.95)]
    df.drop(to_drop, axis=1, inplace=True)
    return df


def test_train_data_spliter(X, Y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.30, random_state=123)
    return X_train, X_test, y_train, y_test


def normal_distribution_calculator(pff_value, submit_val, hypo_val):
    zc = +- scipy.stats.norm.pff(pff_value)
    return hypo_val < submit_val == zc


def df_trainer(X, Y, C):
    x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=.30, random_state=123)
    c_train, c_test, _, _ = train_test_split(C, Y, test_size=.30, random_state=123)
    return x_train, x_test, y_train, y_test, c_train, c_test


def std_scaler_generator(x):
    return StandardScaler().fit(x)


def data_scaler(x_train, x_test, c_train, c_test, scale_categorical):
    std_scaler = std_scaler_generator(x_train)  # mean and std
    x_train_scaled_source = std_scaler.transform(x_train)
    x_test_scaled_source = std_scaler.transform(x_test)
    x_train_scaled_df = pd.DataFrame(x_train_scaled_source)
    x_test_scaled_df = pd.DataFrame(x_test_scaled_source)

    if scale_categorical:
        c_train.reset_index(drop=True, inplace=True)
        c_test.reset_index(drop=True, inplace=True)
        x_train_scaled = pd.concat([x_train_scaled_df, c_train], axis=1, ignore_index=False)
        x_test_scaled = pd.concat([x_test_scaled_df, c_test], axis=1, ignore_index=False)
        return x_train_scaled, x_test_scaled
    else:
        return x_train_scaled_df, x_test_scaled_df


def production_data_scaler(x, x_train):
    std_scaler = std_scaler_generator(x_train)
    # std_scaler = StandardScaler().fit(x)
    x_scaled_source = std_scaler.transform(x.values)
    # scaled_data = pd.DataFrame(x_scaled_source)
    return x_scaled_source


def model_generator(x_train_scaled, x_test_scaled, y_train, y_test):
    model = LinearRegression()
    model.fit(x_train_scaled, y_train)
    model.coef_
    model.intercept_
    return model, model.score(x_test_scaled, y_test)


def plot_builder(y_pred, y_test):
    result = pd.DataFrame({"y_test": y_test, "y_pred": y_pred})
    fig, ax = plt.subplots(1, 3, figsize=(14, 4))
    ax[0].plot(y_pred, y_test, 'o')
    ax[0].set_xlabel("y_test")
    ax[0].set_ylabel("y_pred")
    ax[0].set_title("Test Set -Predicted vs real")
    # Get a histogram of the residuals ie: y - y_pred.  Homoscdasticity
    # It resembles a normal distribution?
    ax[1].hist(y_test - y_pred)
    ax[1].set_xlabel("Test y-y_pred")
    ax[1].set_title("Test Set Residual histogram")

    ax[2].plot(y_pred, y_test - y_pred, "o")
    ax[2].set_xlabel("predited")
    ax[2].set_ylabel("residuals")
    ax[2].set_title("Residuals by Predicted")
    ax[2].plot(y_pred, np.zeros(len(y_pred)), linestyle='dashed')


def print_pretty_json(obj):
    output = json.dumps(obj, indent=2)
    line_list = output.split("\n")
    for line in line_list:
        print(line)


def print_pretty_json_widget(obj):
    JSON(obj, expanded=True)


