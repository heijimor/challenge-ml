import joblib
import os
import pandas as pd

class BakeryPredictUsecase:
  def __init__(self):
    # Define the root folder path to locate the model file
    self.root_folder_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..'))
    self.model_path = os.path.join(self.root_folder_path, 'modelo_vendas.pkl')
    
    # Load the model
    self.model = joblib.load(self.model_path)
    
    # Print out the feature names (if available)
    if hasattr(self.model, 'feature_names_in_'):
      print("Expected Feature Names:", self.model.feature_names_in_)

    # Print the number of features the model expects
    if hasattr(self.model, 'n_features_in_'):
      print("Number of Expected Features:", self.model.n_features_in_)

    # Check if model has `feature_names_in_` attribute to get expected features
    if hasattr(self.model, 'feature_names_in_'):
      self.expected_columns = list(self.model.feature_names_in_)
    else:
      # Manually define expected columns based on training data
      self.expected_columns = [
        'quantidade_vendida', 'preco_unitario', 'month', 'year', 
        'quantidade_vendida_lag1', 'valor_total_lag1', 
        'quantidade_vendida_lag2', 'valor_total_lag2', 
        'quantidade_vendida_lag3', 'valor_total_lag3', 
        'rolling_avg_quantidade', 'rolling_avg_valor_total', 
        'produto_Biscoito de Polvilho', 'produto_Biscoitos Decorados', 
        'produto_Bolo de Aniversário', 'produto_Bolo de Halloween', 
        'produto_Bolo de Morango', 'produto_Café Gourmet', 
        'produto_Café com Leite', 'produto_Chá Gelado', 
        'produto_Coxinha de Frango', 'produto_Cupcake', 
        'produto_Empanadas', 'produto_Ovo de Páscoa', 
        'produto_Panetone', 'produto_Pão de Mel', 
        'produto_Pão de Queijo', 'produto_Salada de Frutas', 
        'produto_Torta de Chocolate', 'categoria_Datas Comemorativas', 
        'categoria_Doces', 'categoria_Lanches', 'categoria_Natal', 
        'categoria_Salgados', 'local_venda_Brasília', 
        'local_venda_Curitiba', 'local_venda_Fortaleza', 
        'local_venda_Porto Alegre', 'local_venda_Recife', 
        'local_venda_Rio de Janeiro', 'local_venda_Salvador', 
        'local_venda_São Paulo'
      ]
      
    print(f'Expected columns: {self.expected_columns}')

  def predict(self, data):
    try:
      # Create a DataFrame from the input data
      input_data = pd.DataFrame({
        'produto': [data['produto']],
        'categoria': [data['categoria']]
      })

      # One-hot encode categorical columns
      input_encoded = pd.get_dummies(input_data, columns=['produto', 'categoria'])

      # Debugging: Check which columns were created
      print(f"One-hot encoded input columns: {input_encoded.columns.tolist()}")

      # Add missing columns with zero if they are not present
      for col in self.expected_columns:
        if col not in input_encoded.columns:
          input_encoded[col] = 0  # Fill missing columns with zero

      # Ensure the columns are ordered correctly
      input_encoded = input_encoded[self.expected_columns]

      # Print the shape and columns of the input for debugging
      print(f'Input columns after processing: {input_encoded.columns.tolist()}')
      print(f'Input shape: {input_encoded.shape}')

      # Make prediction
      predicted_quantity = self.model.predict(input_encoded.values.reshape(1, -1))  # Ensure input is 2D for prediction

      return {'predicted_quantity': predicted_quantity[0]}

    except ValueError as ve:
      return {'error': f'Value Error: {str(ve)}'}
    except Exception as e:
      return {'error': f'General Error: {str(e)}'}
