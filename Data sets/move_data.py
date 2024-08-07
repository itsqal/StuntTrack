import pandas as pd
from sqlalchemy import create_engine, Integer, Column, String, Float, MetaData, Table
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

metadata = MetaData()

for csv_file, table_name in csv_table_pairs.items():
    df = pd.read_csv(csv_file)

    df.insert(0, 'id', range(1, len(df) + 1))
    df['id'] = df['id'].astype('int')

    df['jumlah balita'] = df['jumlah balita'].astype('int')
    df['stunting (pendek)'] = df['stunting (pendek)'].astype('int')
    df['stunting (sangat pendek)'] = df['stunting (sangat pendek)'].astype('int')
    df['persentase stunting'] = df['persentase stunting'].astype('float')

    table = Table(table_name, metadata,
        Column('id', Integer, primary_key=True),
        Column('provinsi', String),
        Column('jumlah balita', Integer),
        Column('stunting (pendek)', Integer),
        Column('stunting (sangat pendek)', Integer),
        Column('persentase stunting', Float)
    )

    metadata.create_all(engine) 
    df.to_sql(table_name, engine, if_exists='replace', index=False) 
