import pandas as pd
import sqlite3

from functions.create_db import create_db
from functions.drop_table import drop_table
from functions.create_table import create_table

# Criar o banco de dados
create_db('mydatabase')

# Criar a tabela 'produto'
create_table(database='mydatabase',
             table_name='produto',
             columns_desc="""
             id_produto INTEGER PRIMARY KEY,
             nome CHAR NOT NULL,
             qtd INTEGER NOT NULL""")

# Conexão com o banco de dados
conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()

# Inserir uma linha na tabela 'produto'
cursor.execute("""
    INSERT INTO produto (nome, qtd)
    VALUES ("PS5", 30)
""")
conn.commit()

# Função para inserir uma linha
def insert_one_row(database_name, table_name, columns_name, values):
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()
    query = f"""
        INSERT INTO {table_name} ({columns_name})
        VALUES ({values})
    """
    cursor.execute(query)
    conn.commit()
    conn.close()

# Inserir um produto na tabela 'produto'
insert_one_row(
    database_name='mydatabase.db',
    table_name='produto',
    columns_name='nome, qtd',
    values="'PS4', 45"
)

# Remover a tabela 'produto'
drop_table(database='mydatabase', table_name='produto')

# Criar a tabela 'cliente'
conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS cliente (
        id_cliente INT PRIMARY KEY,
        nome TEXT
    )
""")

# Excluir a tabela 'cliente'
cursor.execute("DROP TABLE IF EXISTS cliente")

# Criar a tabela 'cliente' usando a função
columns_desc = """id_cliente INT PRIMARY KEY,
    nome TEXT"""
create_table(
    database='mydatabase',
    table_name='cliente',
    columns_desc=columns_desc
)

# Remover a tabela 'cliente' usando a função
drop_table(database='mydatabase', table_name='cliente')

# Excluir a tabela 'produto'
cursor.execute("DROP TABLE IF EXISTS produto")

# Criar um DataFrame de exemplo
data = pd.DataFrame({
    'ID': [1, 2, 3, 4],
    'Name': ['Aline', 'Bob', 'Charlie', 'David']
})

# Conectar ao banco de dados
conn = sqlite3.connect('mydatabase.db')

# Usar o método to_sql para salvar o DataFrame no banco de dados
data.to_sql('client', conn, if_exists='replace', index=False)

# Fechar a conexão
conn.close()

# Reabrir a conexão e executar uma consulta
conn = sqlite3.connect('mydatabase.db')
query = """
    SELECT Name 
    FROM client
    WHERE Name = 'Aline'
"""
result = pd.read_sql_query(query, conn)
print(result)

# Fechar a conexão novamente
conn.close()
