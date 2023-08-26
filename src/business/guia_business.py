from model.guia import Guia
from helpers.conect import conecta_mysql

def cadastrar_guia(codigo_guia: Guia):

    connection = conecta_mysql()
    cursor = connection.cursor()

    sql = "INSERT INTO GUIA (CODIGO_GUIA) VALUES(\"{}\")".format(codigo_guia.CODIGO_GUIA)

    cursor.execute(sql)

    cursor.close()
    connection.commit()
    connection.close()

    return {"response": "GUIA CADASTRADO COM SUCESSO"}

def consulta_todas_guias():

    connection = conecta_mysql()
    cursor = connection.cursor()

    sql = "SELECT * FROM GUIA"

    cursor.execute(sql)
    
     
    columns = [col[0] for col in cursor.description]
    listaguia = [dict(zip(columns, row)) for row in cursor.fetchall()]

    cursor.close()
    connection.close()

    return {"response": listaguia}

def consulta_guia(codigo_guia):

    connection = conecta_mysql()
    cursor = connection.cursor()

    sql = "SELECT * FROM GUIA WHERE CODIGO_GUIA LIKE \"{}%\"".format(codigo_guia)

    cursor.execute(sql)
    
     
    columns = [col[0] for col in cursor.description]
    listaguia = [dict(zip(columns, row)) for row in cursor.fetchall()]
    
    cursor.close()
    connection.close()

    return listaguia


def atualiza_guia(codigo_guia: Guia, codigo_atual_guia):
    connection = conecta_mysql()
    cursor = connection.cursor()
    id_guia = consulta_guia(codigo_atual_guia)[0].get("ID_GUIA")

    sql = "UPDATE GUIA SET CODIGO_GUIA = \"{}\" WHERE ID_GUIA = {}".format(codigo_guia.CODIGO_GUIA, id_guia)
    cursor.execute(sql)
    
    cursor.close()
    connection.commit()
    connection.close()

    return {"response": "GUIA ATUALIZADO COM SUCESSO"}


def deleta_guia(codigo_guia: Guia):
    connection = conecta_mysql()
    cursor = connection.cursor()
    id_guia = consulta_guia(codigo_guia.CODIGO_GUIA)[0].get("ID_GUIA")

    sql = "DELETE FROM GUIA WHERE ID_GUIA = {}".format(id_guia)
    cursor.execute(sql)
    
    cursor.close()
    connection.commit()
    connection.close()

    return {"response": "GUIA DELETADO COM SUCESSO"}