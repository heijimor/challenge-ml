import joblib
import os
import pandas as pd

class BakeryPredictUsecase:
  def predict(self, data):

    root_folder_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..'))
    print(root_folder_path)
    # Define the path to the model
    model_path = os.path.join(root_folder_path, 'modelo_vendas.pkl')

    # Load the model
    model = joblib.load(model_path)
    
    # Create a DataFrame from the input data
    input_data = pd.DataFrame({
        'produto': [data['produto']],
        'categoria': [data['categoria']],
        'local_venda': [data['local_venda']],
        'quantidade': [data['quantidade']],
        'preco_unitario': [data['preco_unitario']]
    })
    
    # Make prediction (ensure that the model is set to predict quantity)
    predicted_quantity = model.predict(input_data)

    # Return the prediction as a JSON response
    # return jsonify({'predicted_quantity': predicted_quantity[0]})
    return { "data": "teste " }
