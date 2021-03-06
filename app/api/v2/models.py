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
                VALUES(TRIM(%s),TRIM(%s),TRIM(%s),TRIM(%s)) RETURNING userid;"""
        try:
            conn = Db().dbcon()
            cur = conn.cursor()
            cur.execute(
                query,
                (self.username,
                 self.email.lower(),
                 self.password,
                 self.role))
            response = cur.fetchone()[0]
            conn.commit()
            return {"response": response}, 201
        except (Exception, psycopg2.DatabaseError) as e:
            print(e)

    """Get a specific user login detail"""

    def get_login_query(self, email, password):
        query = """ SELECT * FROM users WHERE TRIM(email) = lower(TRIM('{}')) AND password = '{}';""".format(
            email, password)
        return query
    """check if user email exists"""

    def get_email_query(self, email):
        query = """ SELECT * FROM users WHERE TRIM(lower(email)) = '{}';""".format(
            email.strip().lower())
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
                VALUES(TRIM(%s),%s,TRIM(%s),%s,TRIM(%s)) RETURNING product_id;"""
        try:
            conn = Db().dbcon()
            cur = conn.cursor()
            cur.execute(
                query,
                (self.product_name,
                 self.product_price,
                 self.description,
                 self.quantity,
                 self.product_image))
            response = cur.fetchone()[0]
            conn.commit()
            return {"response": response}, 201
        except (Exception, psycopg2.DatabaseError) as e:
            print(e)


    """get product by  name"""

    def get_one_product_query(self, product_name):
        query = """ SELECT * FROM products WHERE TRIM(lower(product_name)) = '{}';""".format(
            product_name.lower())
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
            SET product_name = TRIM('{}'),
            description = TRIM('{}'),
            quantity = {},
            product_image = TRIM('{}')
            WHERE product_id = {};""".format(
            data['product_name'],
            data['description'],
            data['quantity'],
            data['product_image'],
            product_id)

        Db().execute_query(query)

    def update_product_quantity(self, product_id, quant):
        query = """ UPDATE products
            SET quantity = {}
            WHERE product_id = {};""".format(quant, product_id)
        Db().execute_query(query)

    def delete_product(self, id):
        query = """DELETE FROM products WHERE product_id = {};""".format(id)
        Db().execute_query(query)


class SalesModel:
    """" Initialize a sales description"""

    def __init__(self, product_id, quantity, sales_price):
        self.product_id = product_id
        self.quantity = quantity
        self.amount = sales_price

    """ Create a product sale."""

    def make_a_sale(self):
        query = """INSERT INTO sales(product_id,quantity,sales_amount)
                VALUES(%s,%s,%s) RETURNING sales_id;"""
        try:
            conn = Db().dbcon()
            cur = conn.cursor()
            cur.execute(query, (self.product_id, self.quantity, self.amount,))
            response = cur.fetchone()[0]
            conn.commit()
            return {"response": response}, 201
        except (Exception, psycopg2.DatabaseError) as e:
            print(e)
        finally:
            conn.close()


    """Get all sales from the store"""

    def get_all_sales(self):
        query = """ SELECT * FROM sales;"""
        response = Db().execute_select(query)
        return response

    """Get product by id"""

    def get_sale_by_id(self, sales_id):
        query = """ SELECT * FROM sales WHERE sales_id = '{}';""".format(
            sales_id)
        response = Db().execute_select(query)
        return response
        