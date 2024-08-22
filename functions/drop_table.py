import sqlite3

def drop_table(
     database: str,
     table_name: str  
) -> None: 
    
    database = f'{database}.db'
        
    conn = sqlite3.connect(database)
    cursor = conn.cursor()
        
    cursor.execute(f"""
             DROP TABLE {table_name}
             """)
    cursor.execute("DROP TABLE IF EXISTS cliente")
        
    cursor.execute("""
            CREATE TABLE IF NOT EXISTS cliente (
                id_cliente INTEGER PRIMARY KEY,
                nome TEXT
            )
        """)
    conn.close()
