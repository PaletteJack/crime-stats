import sqlite3
import pandas as pd

conn = sqlite3.connect('sqlite3.db')
chunk_size = 50000
for chunk in pd.read_csv('Crimes_2001_to_Present.csv', chunksize=chunk_size):
    chunk.to_sql('crime_data', conn, if_exists='append', index=False)
