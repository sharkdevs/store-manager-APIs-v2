import psycopg2

from .database import Db
class UserModel:
    """Initialize users"""
    def __init__(self, username, email, password, role):
        self.username = username
        self.email = email
        self.password = password
        self.role = role

    """Create a user"""
    def creat_user(self):
        query = """INSERT INTO users(username, email, password,role) 
                VALUES(%s,%s,%s,%s) RETURNING userid;"""
        try:
            conn = Db().dbcon()
            cur = conn.cursor()
            cur.execute(query,(self.username,self.email,self.password,self.role))
            response = cur.fetchone()[0]
            conn.commit()
            return {"response":response},206
        except (Exception, psycopg2.DatabaseError) as e:
            print(e)
       

    """Get a specific user login detail"""
    def get_login_query(self, email, password):
        query = """ SELECT * FROM users WHERE email = '{}' AND password = '{}';""".format(
            email, password)
        return query
    """check if user email exists"""
    def get_email_query(self, email):
        query = """ SELECT * FROM users WHERE email = '{}';""".format(
            email)
        response = Db().execute_select(query)
        return response
