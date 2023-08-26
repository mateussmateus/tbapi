import mysql.connector 

def conecta_mysql():
    config = {
        "host": '127.0.0.1',
        "port": 3306,
        "user": 'root',
        "password": '123456',
        "database": 'DBTB'
    }

    try:
        db_connection = mysql.connector.connect(**config)
        print("conexão realizada com sucesso!")
        return db_connection
    except mysql.connector.Error as error:
        print(error)
