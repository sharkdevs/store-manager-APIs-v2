import os
import psycopg2
from flask import current_app

from app.api.v2 import sql_scripts
class Db():
    

    def db_init(self):
        Db().create_tables()

        Db().insert_default_data()
    
    '''Connect to the database'''
    def dbcon(self):
        dbcon_url = current_app.config.get('DB_URL')

        conn = psycopg2.connect(dbcon_url)
        
        return conn

    def create_tables(self):
        scripts = [sql_scripts.create_tbl_products,sql_scripts.create_tbl_sales,sql_scripts.create_tbl_users]

        try:
            
            for query in scripts:
                Db().execute_query(query)
           
            return "Tables successfully created"
        except:
            return "Failed to create a tables"
                

    def insert_default_data(self):
        query = sql_scripts.query_insert_admin
        Db().execute_query(query)

    def execute_query(self, query):
        try:
            conn = Db().dbcon()
            cur = conn.cursor()
            cur.execute(query)
            conn.commit()
        except:
            return "Could not execute query"
        finally:
            conn.close()

    def execute_select(self, query):
        try:
            conn = Db().dbcon()
            cur = conn.cursor()
            cur.execute(query)
            res = cur.fetchone()
            conn.commit()
            return res
        except:
            print("Could not execute query")
        finally:
            conn.close()