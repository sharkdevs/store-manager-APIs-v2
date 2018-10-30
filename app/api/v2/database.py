import os
import psycopg2
from app.api.v2 import sql_scripts
class DbConfig():
    

    
    '''Connect to the database'''
    def dbcon(self):
        dbcon_url = os.environ.get('DB_URL')

        conn = psycopg2.connect(dbcon_url)
        
        return conn

    def create_tables(self):
        scripts = [sql_scripts.create_tbl_products,sql_scripts.create_tbl_sales,sql_scripts.create_tbl_users]

        try:
            conn = DbConfig().dbcon()
            cur = conn.cursor()
            for query in scripts:
                cur.execute(query)
            conn.commit()
            conn.close()
            return "Tables successfully created"
        except:
            return "Failed to create a tables"
                


# if __name__ == '__main__':
#     db = DbConfig()
#     respo = db.dbcon()
#     print(respo)