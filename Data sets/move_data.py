import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

load_dotenv()

database_url = os.getenv('DATABASE_URL')

engine = create_engine(database_url)

csv_table_pairs = {
    'df_2019.csv': 'table_2019',
    'df_2020.csv': 'table_2020',
    'df_2021.csv': 'table_2021',
    'df_2022.csv': 'table_2022',
    'df_2023.csv': 'table_2023',
    'df_2024.csv': 'table_2024'
}

for csv_file, table_name in csv_table_pairs.items():
    df = pd.read_csv(csv_file)
    df.to_sql(table_name, engine, if_exists='replace', index=False)


    