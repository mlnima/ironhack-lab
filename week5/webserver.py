from flask import Flask, request, jsonify
import sys

sys.path.append('../')
import pandas as pd
import numpy as np
from custom_utils import df_spliter_by_data_type
from custom_utils import y_from_x_spliter
from custom_utils import outliers_remover
from custom_utils import df_trainer
from custom_utils import data_scaler
from custom_utils import production_data_scaler
from custom_utils import model_generator
from custom_utils import plot_builder
from sklearn.metrics import r2_score

sourceDf = pd.read_excel('../data/Data_MidTerm_Project_Real_State_Regression.xls')


def df_cleaner(df):
    df = df.drop(
        ['date', 'waterfront', 'zipcode', 'lat', 'long', 'id'],
        errors='ignore',
        axis='columns'
    )
    df = df.reindex(sorted(df.columns), axis=1)
    return df


sourceDf = df_cleaner(sourceDf)

X, Y = y_from_x_spliter(sourceDf, 'price')

X = outliers_remover(X)

numerical, categorical = df_spliter_by_data_type(X)

x_train, x_test, y_train, y_test, c_train, c_test = df_trainer(X, Y, categorical)

x_train_scaled, x_test_scaled = data_scaler(x_train, x_test, c_train=False, c_test=False, scale_categorical=False)

model, model_score = model_generator(x_train_scaled, x_test_scaled, y_train, y_test)

y_pred = model.predict(x_test_scaled)
y_pred_train = model.predict(x_train_scaled)

data_plot = plot_builder(
    y_test=y_test,
    y_pred=y_pred,
)

R2 = r2_score(y_test, y_pred)
R2_train = model.score(x_train_scaled, y_train)
R2_test = model.score(x_test_scaled, y_test)

features_importances = pd.DataFrame(data={
    'Attribute': x_train.columns,
    'Importance': abs(model.coef_)
})
features_importances = features_importances.sort_values(by='Importance', ascending=False)

app = Flask(__name__)


@app.route('/api', methods=['GET'])
def hello_world():
    print(request.data)
    return 'API Is Working Fine'


@app.route('/api/estimatePrice', methods=['POST'])
def price_estimate():
    request_data = request.json
    fake_df = pd.DataFrame(request_data, index=[0])
    fake_df = df_cleaner(fake_df)
    fake_numerical_scaled = production_data_scaler(fake_df, x_train)
    y_pred_train_fake = model.predict(fake_numerical_scaled)
    # print('your estimate price is: ',abs(np.round(y_pred_train_fake, 1)[0]))
    return {'estimate_price': abs(np.round(y_pred_train_fake, 1)[0])}


if __name__ == '__main__':
    app.run(host="localhost", port=4000, debug=True)
