from airflow.hooks.mysql_hook import MySqlHook
import pandas as pd 
from sqlalchemy import create_engine

class MySqlOperators:
    def __init__(self, conn_id):
        self.conn_id = conn_id
        self.hook = MySqlHook(mysql_conn_id = self.conn_id)

    def get_data_to_pd(self,sql):
        return self.hook.get_pandas_df(sql)
    
    def execute_query(self, sql):
        return self.hook.run(sql)

