from model.procedimento import Procedimento
from helpers.conect import conecta_mysql

def cadastrar_procedimento(codigo_procedimento: Procedimento):

    connection = conecta_mysql()
    cursor = connection.cursor()

    sql = "INSERT INTO PROCEDIMENTO (CODIGO_PROCEDIMENTO) VALUES(\"{}\")".format(codigo_procedimento.CODIGO_PROCEDIMENTO)

    cursor.execute(sql)

    cursor.close()
    connection.commit()
    connection.close()

    return {"response": "PROCEDIMENTO CADASTRADO COM SUCESSO"}

def consulta_todos_procedimentos():

    connection = conecta_mysql()
    cursor = connection.cursor()

    sql = "SELECT * FROM PROCEDIMENTO"

    cursor.execute(sql)
    
     
    columns = [col[0] for col in cursor.description]
    listaprocedimento = [dict(zip(columns, row)) for row in cursor.fetchall()]

    cursor.close()
    connection.close()

    return {"response": listaprocedimento}

def consulta_procedimento(codigo_procedimento):

    connection = conecta_mysql()
    cursor = connection.cursor()

    sql = "SELECT * FROM PROCEDIMENTO WHERE CODIGO_PROCEDIMENTO LIKE \"{}%\"".format(codigo_procedimento)

    cursor.execute(sql)
    
     
    columns = [col[0] for col in cursor.description]
    listaprocedimento = [dict(zip(columns, row)) for row in cursor.fetchall()]
    
    cursor.close()
    connection.close()

    return listaprocedimento


def atualiza_procedimento(codigo_procedimento: Procedimento, codigo_atual_procedimento):
    connection = conecta_mysql()
    cursor = connection.cursor()
    id_procedimento = consulta_procedimento(codigo_atual_procedimento)[0].get("ID_PROCEDIMENTO")

    sql = "UPDATE PROCEDIMENTO SET CODIGO_PROCEDIMENTO = \"{}\" WHERE ID_PROCEDIMENTO = {}".format(codigo_procedimento.CODIGO_PROCEDIMENTO, id_procedimento)
    cursor.execute(sql)
    
    cursor.close()
    connection.commit()
    connection.close()

    return {"response": "PROCEDIMENTO ATUALIZADO COM SUCESSO"}


def deleta_procedimento(codigo_procedimento: Procedimento):
    connection = conecta_mysql()
    cursor = connection.cursor()
    id_procedimento = consulta_procedimento(codigo_procedimento.CODIGO_PROCEDIMENTO)[0].get("ID_PROCEDIMENTO")

    sql = "DELETE FROM PROCEDIMENTO WHERE ID_PROCEDIMENTO = {}".format(id_procedimento)
    cursor.execute(sql)
    
    cursor.close()
    connection.commit()
    connection.close()

    return {"response": "PROCEDIMENTO DELETADO COM SUCESSO"}