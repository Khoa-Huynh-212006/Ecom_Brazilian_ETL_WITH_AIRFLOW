from airflow.hooks.base import BaseHook
from sqlalchemy import create_engine

def get_engine(conn_id, db_type='mysql'):
    conn = BaseHook.get_connection(conn_id)
    
    if db_type == 'mysql':
        uri = f"mysql+mysqlconnector://{conn.login}:{conn.password}@{conn.host}:{conn.port}/{conn.schema}"
    else:
        uri = f"postgresql+psycopg2://{conn.login}:{conn.password}@{conn.host}:{conn.port}/{conn.schema}"
        
    return create_engine(uri)