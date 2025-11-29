from airflow.hooks.postgres_hook import PostgresHook
import pandas as pd
from sqlalchemy import create_engine

class PostgresOperators:
    def __init__(self, conn_id):
        self.conn_id = conn_id
        self.hook = PostgresHook(postgres_conn_id=self.conn_id)

    def save_data_to_postgres(self, df, table_name, schema='public', if_exists='replace'):
        conn = self.hook.get_uri()
        engine = create_engine(conn)
        df.to_sql(table_name, engine, schema=schema, if_exists=if_exists, index=False)

    def execute_query(self, sql):
        self.hook.run(sql)