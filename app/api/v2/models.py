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
            return {"response":response},201
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

class ProductModel:
    """" Initialize a product description"""

    def __init__(
            self,
            product_name,
            product_price,
            description,
            quantity,
            product_image):
        self.product_name = product_name
        self.product_price = product_price
        self.description = description
        self.quantity = quantity
        self.product_image = product_image

    """ Create a product."""

    def create_a_product(self):
        query = """INSERT INTO products(product_name, product_price, description,quantity,product_image) 
                VALUES(%s,%s,%s,%s,%s) RETURNING product_id;"""
        try:
            conn = Db().dbcon()
            cur = conn.cursor()
            cur.execute(query,(self.product_name,self.product_price,self.description,self.quantity,self.product_image))
            response = cur.fetchone()[0]
            conn.commit()
            return {"response":response},201
        except (Exception, psycopg2.DatabaseError) as e:
            print(e)

    """get product by  name"""
    def get_one_product_query(self, product_name):
        query = """ SELECT * FROM products WHERE product_name = '{}';""".format(
            product_name)
        response = Db().execute_select(query)
        return response

    """Get product by id"""
    def get_product_b_id(self, product_id):
        query = """ SELECT * FROM products WHERE product_id = '{}';""".format(
            product_id)
        response = Db().execute_select(query)
        return response
    
    """Get all products"""
    def get_all_products(self):
        query = """ SELECT * FROM products;"""
        response = Db().execute_select(query)
        return response
    
    def update_product(self, product_id, data):
        query = """ UPDATE products 
            SET product_name = '{}',
            description = '{}', 
            quantity = {}, 
            product_image = '{}'
            WHERE product_id = {};""".format(
            data['product_name'],
            data['description'],
            data['quantity'], 
            data['product_image'],
            product_id)

        Db().execute_query(query)
    def delete_product(self,id):
        query = """DELETE FROM products WHERE product_id = {};""".format(id)
        Db().execute_query(query)
class Sales:
    """" Initialize a sales description"""

    def __init__(self, product_id, quantity, sales_price, sales_date):
        self.product_id = product_id
        self.quantity = quantity
        self.sales_date = sales_date
        self.amount = sales_price*quantity

    """ Create a product sale."""

    def make_a_sale(self):
        query = """INSERT INTO sales(product_id,quantity,sales_amount,,sales_date) 
                VALUES(%s,%s,%s,%s) RETURNING product_id;"""
        try:
            conn = Db().dbcon()
            cur = conn.cursor()
            cur.execute(query,(self.product_id,self.quantity,self.amount, self.quantity,self.sales_date))
            response = cur.fetchone()[0]
            conn.commit()
            return {"response":response},201
        except (Exception, psycopg2.DatabaseError) as e:
            print(e)

  