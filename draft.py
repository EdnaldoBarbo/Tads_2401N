import pandas as pd 
import sqlite3

from functions.create_db import create_db
from functions.drop_table import drop_table
from functions.create_table import create_table
create_db ('mydatabase')

conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()
cursor.execute("""
        CREATE TABLE IF NOT EXISTS cliente (
               id_cliente INT PRIMARY KEY,
               nome TEXT
               )       
               """)

cursor.execute("""
     DROP TABLE cliente          
""")

# create table 
columns_desc = """id_cliente INT PRIMARY KEY,
    nome TEXT"""

create_table(
    database='mydatabase',
    table_name='cliente',
    columns_desc= columns_desc
)


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
