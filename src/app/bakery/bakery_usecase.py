import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

class BakeryUsecase:
  def train_model(self):
      # it should get by s3 partition saved by aws glue
      data = {
        'gasto_marketing': [10, 15, 20, 25, 30],  # investimento em marketing
        'vendas': [100, 150, 200, 250, 300]        # unidades
      }
      df = pd.DataFrame(data)
      X = df[['gasto_marketing']]
      y = df['vendas']
      model = LinearRegression()
      model.fit(X, y)

      with open('modelo_vendas.pkl', 'wb') as f:
          pickle.dump(model, f)

  # @doc: load trained model, on production it needs to get by s3
  def load_model(self):
      with open('modelo_vendas.pkl', 'rb') as f:
          model = pickle.load(f)
      return model

  # Predict sales by investment
  def predict_sales(self, gasto_marketing):
      model = self.load_model()
      predicted_sales = model.predict([[gasto_marketing]])

      if predicted_sales.size == 0:
          return None
      return model.predict([[gasto_marketing]])[0]

  def predict_financial_return(self, sales, price_per_unit):
      return sales * price_per_unit