create_tbl_products = """CREATE TABLE IF NOT EXISTS products(
        product_id serial PRIMARY KEY,
        product_name VARCHAR (50) NOT NULL,
        product_price INT NOT NULL,
        description TEXT NOT NULL,
        quantity INT NOT NULL,
        product_image VARCHAR(50) NOT NULL
    );"""

create_tbl_users = """CREATE TABLE IF NOT EXISTS users(
        userid serial PRIMARY KEY,
        username VARCHAR (50) NOT NULL,
        email VARCHAR(50) UNIQUE NOT NULL,
        password VARCHAR(50) NOT NULL,
        role VARCHAR(50) NOT NULL
    );"""

create_tbl_sales = """CREATE TABLE IF NOT EXISTS sales(
        sales_id serial PRIMARY KEY,
        product_id INT NOT NULL,
        quantity INT NOT NULL,
        sales_amount INT NOT NULL,
        sales_date timestamp,
        CONSTRAINT sales_products_id_fkey FOREIGN KEY (product_id)
        REFERENCES products (product_id) MATCH SIMPLE
        ON UPDATE NO ACTION ON DELETE NO ACTION
    );"""

query_insert_admin = """INSERT 
                    INTO users (username, email, password,role)
                    SELECT 'superadmin','su@admin.com','admin@2018*','admin'
                    WHERE 'su@admin.com' NOT IN
                        (
                            SELECT email FROM users
                        );"""

query_get = """SELECT * FROM products;"""
