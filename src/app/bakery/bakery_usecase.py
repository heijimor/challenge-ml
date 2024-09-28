import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score

import joblib
import os

class BakeryUsecase:
  def get(self, options):
    folder_path = '/home/heijimor/Desktop/fiap/challenge-ml/temp'
    os.makedirs(folder_path, exist_ok=True)
    filename = os.path.join(folder_path, 'data.csv')

    # Lê o arquivo CSV que acabou de ser salvo
    data = pd.read_csv(filename)

    print(data.head())
    print('-----')
    print(data.isnull().sum())
    print('-----')
    print(data.describe())
    print('-----')

    X = data.drop(['id_venda', 'data_venda', 'valor_total'], axis=1)  # Remover colunas não necessárias
    y = data['valor_total']  # Rótulo: valor total

    # Usando one-hot encoding para variáveis categóricas
    X = pd.get_dummies(X, columns=['produto', 'categoria', 'local_venda'], drop_first=True)

    # Dividir os dados
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    print(f'Erro Quadrático Médio: {mse:.2f}')
    print(f'R²: {r2:.2f}')

    joblib.dump(model, 'modelo_vendas.pkl')

    return { "data": "bakery" }
