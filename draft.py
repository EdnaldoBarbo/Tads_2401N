import pandas as pd 
import sqlite3

from functions.create_db import create_db
create_db ('mydatabase')

conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()
cursor.execute("""
        CREATE TABLE IF NOT EXISTS cliente (
               id_cliente INT,
               nome TEXT
               )       
               
               """)

cursor.execute("""
     DROP TABLE cliente          
""")












# Create a data example 
data = pd.DataFrame({
    'ID': [1,2,3,4],
    'Name': ['Aline','Bob','Charlie','David']
    })

# creat a connection 
conn = sqlite3.connect('mydatabase.db')

# Use the to_sql method to sabe the DataFrame
data.to_sql(
    'client', conn, 
    if_exists='replace',    
    index=False
)
# closing the connection 
conn.close()

######

conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()
query = """
    SELECT name 
    FROM client
    WHERE name = 'Aline'
    """
pd.read_sql_query(query, conn)
