import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

class BakeryUsecase:
  def train_model(self):
      data = {
          'gasto_marketing': [10, 15, 20, 25, 30],  # investimento em marketing
          'vendas': [100, 150, 200, 250, 300]        # unidades
      }
      df = pd.DataFrame(data)
      X = df[['gasto_marketing']]
      y = df['vendas']
      model = LinearRegression()
      model.fit(X, y)

      # Salvar o modelo treinado
      with open('modelo_vendas.pkl', 'wb') as f:
          pickle.dump(model, f)

  # Carregar o modelo treinado
  def load_model(self):
      with open('modelo_vendas.pkl', 'rb') as f:
          model = pickle.load(f)
      return model

  # Prever vendas com base no gasto em marketing
  def predict_sales(self, gasto_marketing):
      model = self.load_model()
      print('Loaded model:', model)
      print('Gasto Marketing:', gasto_marketing)
      
      # Make prediction
      predicted_sales = model.predict([[gasto_marketing]])
      print('Predicted sales array:', predicted_sales)
      
      # Check if prediction returned any value
      if predicted_sales.size == 0:
          return None  # Return None explicitly if no prediction
      return model.predict([[gasto_marketing]])[0]

  # Prever retorno financeiro com base nas vendas e no preço por unidade
  def predict_financial_return(self, sales, price_per_unit):
      return sales * price_per_unit