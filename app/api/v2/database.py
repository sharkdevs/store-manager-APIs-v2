import os
import psycopg2
# from app.api.v2 import sql_scripts
class DbConfig():

    '''Connect to the database'''
    def dbcon(self):
        dbcon_url = os.environ.get('DB_URL')

        try:
            conn = psycopg2.connect(dbcon_url)
            return "success"
        except ConnectionError as error:
            return "Could not connect "+error



if __name__ == '__main__':
    db = DbConfig()
    respo = db.dbcon()
    print(respo)