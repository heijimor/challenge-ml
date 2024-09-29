import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV
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

        # Read the CSV file
        data = pd.read_csv(filename)

        # Convert 'data_venda' to datetime
        data['data_venda'] = pd.to_datetime(data['data_venda'])

        # Aggregate by month
        monthly_data = data.resample('M', on='data_venda').agg({
            'quantidade_vendida': 'sum',
            'preco_unitario': 'mean',
            'valor_total': 'sum',
            'produto': lambda x: x.mode()[0],
            'categoria': lambda x: x.mode()[0],
            'local_venda': lambda x: x.mode()[0]
        }).reset_index()

        # Add month and year as features
        monthly_data['month'] = monthly_data['data_venda'].dt.month
        monthly_data['year'] = monthly_data['data_venda'].dt.year

        # Add lagged features
        for lag in range(1, 4):  # Add lags for 1, 2, and 3 months
            monthly_data[f'quantidade_vendida_lag{lag}'] = monthly_data['quantidade_vendida'].shift(lag)
            monthly_data[f'valor_total_lag{lag}'] = monthly_data['valor_total'].shift(lag)

        # Add rolling statistics
        monthly_data['rolling_avg_quantidade'] = monthly_data['quantidade_vendida'].rolling(window=3).mean()
        monthly_data['rolling_avg_valor_total'] = monthly_data['valor_total'].rolling(window=3).mean()

        # Drop NaN values caused by shifting and rolling
        monthly_data.dropna(inplace=True)

        # Drop unnecessary columns and prepare for training
        X = monthly_data.drop(['data_venda', 'valor_total'], axis=1)
        y = monthly_data['valor_total']

        # One-hot encoding for categorical variables
        X_encoded = pd.get_dummies(X, columns=['produto', 'categoria', 'local_venda'], drop_first=True)

        # Store the column names after encoding for later use
        encoded_columns = X_encoded.columns.tolist()
        
        print(encoded_columns)

        # Split the data
        X_train, X_test, y_train, y_test = train_test_split(X_encoded, y, test_size=0.2, random_state=42)

        # Scaling the features
        scaler = StandardScaler()
        X_train = scaler.fit_transform(X_train)
        X_test = scaler.transform(X_test)

        # Hyperparameter tuning using GridSearchCV
        param_grid = {
            'n_estimators': [50, 100, 200],
            'max_depth': [None, 10, 20, 30],
            'min_samples_split': [2, 5, 10]
        }

        grid_search = GridSearchCV(RandomForestRegressor(random_state=42), param_grid, cv=5, scoring='neg_mean_squared_error')
        grid_search.fit(X_train, y_train)

        # Get the best model
        best_model = grid_search.best_estimator_

        # Save the best model and column names
        joblib.dump(best_model, 'modelo_vendas.pkl')
        joblib.dump(encoded_columns, 'encoded_columns.pkl')
        joblib.dump(scaler, 'scaler.pkl')

        # Make predictions
        y_pred = best_model.predict(X_test)
        mse = mean_squared_error(y_test, y_pred)
        r2 = r2_score(y_test, y_pred)

        print(f'Erro Quadrático Médio: {mse:.2f}')
        print(f'R²: {r2:.2f}')

        return {
            "data": {
                "quadratic-error": f'{mse:.2f}',
                "r": f'{r2:.2f}'
            }
        }
