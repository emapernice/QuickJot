import datetime
import hashlib
import users.connection as connection

connect = connection.connect()
database = connect[0]
cursor = connect[1]

class User:

    def __init__(self, name, last_names, email, password):
        self.name = name
        self.last_names = last_names
        self.email = email
        self.password = password

    def register(self):
        date = datetime.datetime.now()

        # Encrypt password
        cipher = hashlib.sha256()
        cipher.update(self.password.encode('utf8'))

        sql = "INSERT INTO users VALUES(null, %s, %s, %s, %s, %s)"
        user = (self.name, self.last_names, self.email, cipher.hexdigest(), date)

        try:
            cursor.execute(sql, user)
            database.commit()
            result = [cursor.rowcount, self]
        except:    
            result = [0, self]
        return result

    def login(self): 
        sql = "SELECT * FROM users WHERE email = %s AND password = %s"  

        # Encrypt password
        cipher = hashlib.sha256()
        cipher.update(self.password.encode('utf8'))

        user = (self.email, cipher.hexdigest())  

        cursor.execute(sql, user)
        result = cursor.fetchone()

        return result        