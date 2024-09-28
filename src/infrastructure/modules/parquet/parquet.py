import pandas as pd
from datetime import datetime

def convert_csv_to_partitioned_parquet(csv_file_path, output_directory):
  try:
    print(csv_file_path)
    print(output_directory)
    parquetFile = output_directory + '/output.parquet'

    with open(csv_file_path, 'r', encoding='latin1') as file:
        first_line = file.readline().strip()
        date_str = first_line.split('Dia ')[1]

    df = pd.read_csv(
      csv_file_path,
      delimiter=';',
      encoding='latin1',
      on_bad_lines = "skip",
      skiprows=1,
      header=0,
      index_col=False,
      keep_default_na=False
    )
    df_cleaned = df[~df['Setor'].isin(['Quantidade Teórica Total', 'Redutor'])]
    df_cleaned.columns = ['Setor', 'Código', 'Ação', 'Tipo', 'Quantidade', 'Part', 'Acum']
    # date_obj = pd.to_datetime(date_str, format='%d/%m/%y %H:%M').dt.floor('D')
    # df_cleaned['Date'] = date_str
    df_cleaned['Date'] = pd.to_datetime(date_str, format='%d/%m/%y').date()
    df = df_cleaned.reset_index(drop=True)
    print(df)

    df.to_parquet(parquetFile)
    validate_parquet_file(parquetFile)
  except Exception as error:
    print(error)
    return {'error': str(error)}


def validate_parquet_file(parquet_file_path):
    print('--------- Validating parquet file ---------')
    df = pd.read_parquet(parquet_file_path, engine='pyarrow')
    print("DataFrame Structure:")
    print(df.info())
    print("\nMissing Values:")
    print(df.isnull().sum())
    print("\nData Types:")
    print(df.dtypes)
    print("\nSample Data:")
    print(df.head())
    print("\nSummary Statistics:")
    print(df.describe())
    print("\nSpecific Value Check:")
    specific_value_check = (df['Código'] == 'RRRP3').any()
    print(f"Contains 'RRRP3' in 'Código': {specific_value_check}")

    print('--------- Parquet file validation finished ---------')