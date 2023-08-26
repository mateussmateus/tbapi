from model.paciente import Paciente
from helpers.conect import conecta_mysql

def cadastra_paciente(nome_paciente: Paciente):

    connection = conecta_mysql()
    cursor = connection.cursor()

    sql = "INSERT INTO PACIENTE (NOME_PACIENTE) VALUES(\"{}\")".format(nome_paciente.NOME_PACIENTE)

    cursor.execute(sql)

    cursor.close()
    connection.commit()
    connection.close()

    return {"response": "PACIENTE CADASTRADO COM SUCESSO"}

def consulta_todos_pacientes():

    connection = conecta_mysql()
    cursor = connection.cursor()

    sql = "SELECT * FROM PACIENTE"

    cursor.execute(sql)
    
     
    columns = [col[0] for col in cursor.description]
    listapacientes = [dict(zip(columns, row)) for row in cursor.fetchall()]

    cursor.close()
    connection.close()

    return {"response": listapacientes}

def consulta_paciente(nome_paciente):

    connection = conecta_mysql()
    cursor = connection.cursor()

    sql = "SELECT * FROM PACIENTE WHERE NOME_PACIENTE LIKE \"{}%\"".format(nome_paciente)

    cursor.execute(sql)
    
     
    columns = [col[0] for col in cursor.description]
    listapacientes = [dict(zip(columns, row)) for row in cursor.fetchall()]
    
    cursor.close()
    connection.close()

    return listapacientes


def atualiza_paciente(paciente: Paciente, nome_atual_paciente):
    connection = conecta_mysql()
    cursor = connection.cursor()
    id_paciente = consulta_paciente(nome_atual_paciente)[0].get("ID_PACIENTE")

    sql = "UPDATE PACIENTE SET NOME_PACIENTE = \"{}\" WHERE ID_PACIENTE = {}".format(paciente.NOME_PACIENTE, id_paciente)
    cursor.execute(sql)
    
    cursor.close()
    connection.commit()
    connection.close()

    return {"response": "PACIENTE ATUALIZADO COM SUCESSO"}


def deleta_paciente(paciente: Paciente):
    connection = conecta_mysql()
    cursor = connection.cursor()
    id_paciente = consulta_paciente(paciente.NOME_PACIENTE)[0].get("ID_PACIENTE")

    sql = "DELETE FROM PACIENTE WHERE ID_PACIENTE = {}".format(id_paciente)
    cursor.execute(sql)
    
    cursor.close()
    connection.commit()
    connection.close()

    return {"response": "PACIENTE DELETADO COM SUCESSO"}