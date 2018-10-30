class UserModel:
    def __init__(self, username, email, password, role):
        self.username = username
        self.email = email
        self.password = password
        self.role = role

    def creat_user(self):
        pass
    
    def get_login_query(self, email, password):
        query =""" SELECT * FROM users WHERE email = '{}' AND password = '{}';""".format(email, password)
        return query

    
    