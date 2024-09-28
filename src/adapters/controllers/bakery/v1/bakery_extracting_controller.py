from infrastructure.modules.routing.annotations.route import route
from infrastructure.modules.routing.annotations.get import get
from app.b3.extracting.extracting_usecase import ExtractingUsecase

import os
import json

@route('/bakery/v1/extracting')
class BakeryExtractingController:
  @get
  def index(self, requests):
    options = requests.query_params

    # getting from a service and its from some API or directly from DB source
    # think about get by excel format and run ETL
    # simulate other days
    response = [
      {
          "id_venda": 1,
          "data_venda": "2022-01-05",
          "produto": "Bolo de Chocolate",
          "categoria": "Doces",
          "quantidade_vendida": 30,
          "preco_unitario": 5.5,
          "valor_total": 165,
          "local_venda": "São Paulo",
          "cliente_id": 101
      },
      {
          "id_venda": 2,
          "data_venda": "2022-01-15",
          "produto": "Brigadeiro",
          "categoria": "Doces",
          "quantidade_vendida": 150,
          "preco_unitario": 1.2,
          "valor_total": 180,
          "local_venda": "Rio de Janeiro",
          "cliente_id": 102
      },
      {
          "id_venda": 3,
          "data_venda": "2022-02-10",
          "produto": "Pão de Mel",
          "categoria": "Doces",
          "quantidade_vendida": 50,
          "preco_unitario": 3,
          "valor_total": 150,
          "local_venda": "Belo Horizonte",
          "cliente_id": 103
      },
      {
          "id_venda": 4,
          "data_venda": "2022-02-25",
          "produto": "Coxinha",
          "categoria": "Salgados",
          "quantidade_vendida": 200,
          "preco_unitario": 3.5,
          "valor_total": 700,
          "local_venda": "Brasília",
          "cliente_id": 104
      },
      {
          "id_venda": 5,
          "data_venda": "2022-03-05",
          "produto": "Empadinha",
          "categoria": "Salgados",
          "quantidade_vendida": 80,
          "preco_unitario": 4,
          "valor_total": 320,
          "local_venda": "Curitiba",
          "cliente_id": 105
      },
      {
          "id_venda": 6,
          "data_venda": "2022-03-15",
          "produto": "Quiche de Queijo",
          "categoria": "Salgados",
          "quantidade_vendida": 40,
          "preco_unitario": 8.5,
          "valor_total": 340,
          "local_venda": "Porto Alegre",
          "cliente_id": 106
      },
      {
          "id_venda": 7,
          "data_venda": "2022-04-01",
          "produto": "Ovo de Páscoa",
          "categoria": "Páscoa",
          "quantidade_vendida": 120,
          "preco_unitario": 30,
          "valor_total": 3600,
          "local_venda": "Curitiba",
          "cliente_id": 107
      },
      {
          "id_venda": 8,
          "data_venda": "2022-04-10",
          "produto": "Torta de Maçã",
          "categoria": "Doces",
          "quantidade_vendida": 60,
          "preco_unitario": 20,
          "valor_total": 1200,
          "local_venda": "São Paulo",
          "cliente_id": 108
      },
      {
          "id_venda": 9,
          "data_venda": "2022-05-12",
          "produto": "Cupcake",
          "categoria": "Doces",
          "quantidade_vendida": 75,
          "preco_unitario": 4.5,
          "valor_total": 337.5,
          "local_venda": "Salvador",
          "cliente_id": 109
      },
      {
          "id_venda": 10,
          "data_venda": "2022-05-25",
          "produto": "Pão Caseiro",
          "categoria": "Padaria",
          "quantidade_vendida": 90,
          "preco_unitario": 10,
          "valor_total": 900,
          "local_venda": "Porto Alegre",
          "cliente_id": 110
      },
      {
          "id_venda": 11,
          "data_venda": "2022-06-05",
          "produto": "Café Gourmet",
          "categoria": "Bebidas",
          "quantidade_vendida": 200,
          "preco_unitario": 12,
          "valor_total": 2400,
          "local_venda": "Recife",
          "cliente_id": 111
      },
      {
          "id_venda": 12,
          "data_venda": "2022-06-25",
          "produto": "Sanduíche Natural",
          "categoria": "Lanches",
          "quantidade_vendida": 120,
          "preco_unitario": 7.5,
          "valor_total": 900,
          "local_venda": "Rio de Janeiro",
          "cliente_id": 112
      },
      {
          "id_venda": 13,
          "data_venda": "2022-07-10",
          "produto": "Salada de Frutas",
          "categoria": "Lanches",
          "quantidade_vendida": 50,
          "preco_unitario": 5,
          "valor_total": 250,
          "local_venda": "Fortaleza",
          "cliente_id": 113
      },
      {
          "id_venda": 14,
          "data_venda": "2022-07-25",
          "produto": "Torta de Limão",
          "categoria": "Doces",
          "quantidade_vendida": 50,
          "preco_unitario": 20,
          "valor_total": 1000,
          "local_venda": "Recife",
          "cliente_id": 114
      },
      {
          "id_venda": 15,
          "data_venda": "2022-08-15",
          "produto": "Bolo de Aniversário",
          "categoria": "Datas Comemorativas",
          "quantidade_vendida": 15,
          "preco_unitario": 60,
          "valor_total": 900,
          "local_venda": "Natal",
          "cliente_id": 115
      },
      {
          "id_venda": 16,
          "data_venda": "2022-08-30",
          "produto": "Canapés",
          "categoria": "Lanches",
          "quantidade_vendida": 100,
          "preco_unitario": 5,
          "valor_total": 500,
          "local_venda": "Brasília",
          "cliente_id": 116
      },
      {
          "id_venda": 17,
          "data_venda": "2022-09-10",
          "produto": "Quiche de Espinafre",
          "categoria": "Salgados",
          "quantidade_vendida": 45,
          "preco_unitario": 9,
          "valor_total": 405,
          "local_venda": "Salvador",
          "cliente_id": 117
      },
      {
          "id_venda": 18,
          "data_venda": "2022-09-25",
          "produto": "Pão de Queijo",
          "categoria": "Lanches",
          "quantidade_vendida": 80,
          "preco_unitario": 3,
          "valor_total": 240,
          "local_venda": "São Paulo",
          "cliente_id": 118
      },
      {
          "id_venda": 19,
          "data_venda": "2022-10-01",
          "produto": "Bolo de Halloween",
          "categoria": "Datas Comemorativas",
          "quantidade_vendida": 35,
          "preco_unitario": 50,
          "valor_total": 1750,
          "local_venda": "Fortaleza",
          "cliente_id": 119
      },
      {
          "id_venda": 20,
          "data_venda": "2022-10-20",
          "produto": "Sanduíche de Frango",
          "categoria": "Lanches",
          "quantidade_vendida": 150,
          "preco_unitario": 8,
          "valor_total": 1200,
          "local_venda": "Brasília",
          "cliente_id": 120
      },
      {
          "id_venda": 21,
          "data_venda": "2022-11-05",
          "produto": "Biscoito de Polvilho",
          "categoria": "Lanches",
          "quantidade_vendida": 250,
          "preco_unitario": 2.5,
          "valor_total": 625,
          "local_venda": "Curitiba",
          "cliente_id": 121
      },
      {
          "id_venda": 22,
          "data_venda": "2022-11-25",
          "produto": "Pastel de Queijo",
          "categoria": "Lanches",
          "quantidade_vendida": 200,
          "preco_unitario": 4,
          "valor_total": 800,
          "local_venda": "Belo Horizonte",
          "cliente_id": 122
      },
      {
          "id_venda": 23,
          "data_venda": "2022-12-15",
          "produto": "Panetone",
          "categoria": "Natal",
          "quantidade_vendida": 250,
          "preco_unitario": 25,
          "valor_total": 6250,
          "local_venda": "São Paulo",
          "cliente_id": 123
      },
      {
          "id_venda": 24,
          "data_venda": "2022-12-22",
          "produto": "Rabanada",
          "categoria": "Natal",
          "quantidade_vendida": 180,
          "preco_unitario": 6,
          "valor_total": 6250,
          "local_venda": "São Paulo",
          "cliente_id": 123
      },
      {
          "id_venda": 25,
          "data_venda": "2023-01-10",
          "produto": "Bolo de Morango",
          "categoria": "Doces",
          "quantidade_vendida": 45,
          "preco_unitario": 55,
          "valor_total": 2475,
          "local_venda": "São Paulo",
          "cliente_id": 124
      },
      {
          "id_venda": 26,
          "data_venda": "2023-01-20",
          "produto": "Trufas",
          "categoria": "Doces",
          "quantidade_vendida": 200,
          "preco_unitario": 1.5,
          "valor_total": 300,
          "local_venda": "Rio de Janeiro",
          "cliente_id": 125
      },
      {
          "id_venda": 27,
          "data_venda": "2023-02-15",
          "produto": "Torta de Chocolate",
          "categoria": "Doces",
          "quantidade_vendida": 30,
          "preco_unitario": 70,
          "valor_total": 2100,
          "local_venda": "Curitiba",
          "cliente_id": 126
      },
      {
          "id_venda": 28,
          "data_venda": "2023-03-05",
          "produto": "Salada de Frutas",
          "categoria": "Lanches",
          "quantidade_vendida": 100,
          "preco_unitario": 10,
          "valor_total": 1000,
          "local_venda": "Brasília",
          "cliente_id": 127
      },
      {
          "id_venda": 29,
          "data_venda": "2023-03-25",
          "produto": "Pão de Queijo",
          "categoria": "Lanches",
          "quantidade_vendida": 75,
          "preco_unitario": 3.5,
          "valor_total": 262.5,
          "local_venda": "Fortaleza",
          "cliente_id": 128
      },
      {
          "id_venda": 30,
          "data_venda": "2023-04-15",
          "produto": "Biscoitos Decorados",
          "categoria": "Doces",
          "quantidade_vendida": 200,
          "preco_unitario": 2,
          "valor_total": 400,
          "local_venda": "Recife",
          "cliente_id": 129
      },
      {
          "id_venda": 31,
          "data_venda": "2023-05-10",
          "produto": "Empanadas",
          "categoria": "Salgados",
          "quantidade_vendida": 150,
          "preco_unitario": 5,
          "valor_total": 750,
          "local_venda": "Salvador",
          "cliente_id": 130
      },
      {
          "id_venda": 32,
          "data_venda": "2023-06-05",
          "produto": "Coxinha de Frango",
          "categoria": "Salgados",
          "quantidade_vendida": 100,
          "preco_unitario": 3,
          "valor_total": 300,
          "local_venda": "Belo Horizonte",
          "cliente_id": 131
      },
      {
          "id_venda": 33,
          "data_venda": "2023-06-30",
          "produto": "Torta de Frango",
          "categoria": "Salgados",
          "quantidade_vendida": 60,
          "preco_unitario": 20,
          "valor_total": 1200,
          "local_venda": "Natal",
          "cliente_id": 132
      },
      {
          "id_venda": 34,
          "data_venda": "2023-07-15",
          "produto": "Café com Leite",
          "categoria": "Bebidas",
          "quantidade_vendida": 250,
          "preco_unitario": 3,
          "valor_total": 750,
          "local_venda": "Porto Alegre",
          "cliente_id": 133
      },
      {
          "id_venda": 35,
          "data_venda": "2023-08-01",
          "produto": "Chá Gelado",
          "categoria": "Bebidas",
          "quantidade_vendida": 150,
          "preco_unitario": 2.5,
          "valor_total": 375,
          "local_venda": "São Paulo",
          "cliente_id": 134
      },
      {
          "id_venda": 36,
          "data_venda": "2023-08-20",
          "produto": "Torta de Maçã",
          "categoria": "Doces",
          "quantidade_vendida": 90,
          "preco_unitario": 25,
          "valor_total": 2250,
          "local_venda": "Rio de Janeiro",
          "cliente_id": 135
      },
      {
          "id_venda": 37,
          "data_venda": "2023-09-15",
          "produto": "Bolo de Banana",
          "categoria": "Doces",
          "quantidade_vendida": 45,
          "preco_unitario": 45,
          "valor_total": 2025,
          "local_venda": "Curitiba",
          "cliente_id": 136
      },
      {
          "id_venda": 38,
          "data_venda": "2023-09-30",
          "produto": "Bebida Energética",
          "categoria": "Bebidas",
          "quantidade_vendida": 500,
          "preco_unitario": 4,
          "valor_total": 2000,
          "local_venda": "Fortaleza",
          "cliente_id": 137
      },
      {
          "id_venda": 39,
          "data_venda": "2023-10-05",
          "produto": "Pão de Mel",
          "categoria": "Doces",
          "quantidade_vendida": 70,
          "preco_unitario": 5,
          "valor_total": 350,
          "local_venda": "Salvador",
          "cliente_id": 138
      },
      {
          "id_venda": 40,
          "data_venda": "2023-10-20",
          "produto": "Quiche de Legumes",
          "categoria": "Salgados",
          "quantidade_vendida": 30,
          "preco_unitario": 25,
          "valor_total": 750,
          "local_venda": "Brasília",
          "cliente_id": 139
      }
    ]

    return response
