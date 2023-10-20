import sqlite3
import pandas as pd

conn = sqlite3.connect('sqlite3.db')
cols = ['Case Number', 'Date', 'Block', 'IUCR', 'Primary Type', 'Description', 'Location Description', 'Arrest', 'Domestic', 'FBI Code', 'Year', 'Updated On']
chunk_size = 50000
for chunk in pd.read_csv('Crimes_2001_to_Present.csv', chunksize=chunk_size, usecols=cols):
    chunk.to_sql('crime_data', conn, if_exists='append', index=False)