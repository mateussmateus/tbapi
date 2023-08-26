from model.convenio import Convenio
from helpers.conect import conecta_mysql

def cadastrar_convenio(nome_convenio: Convenio):

    connection = conecta_mysql()
    cursor = connection.cursor()

    sql = "INSERT INTO CONVENIO (NOME_CONVENIO) VALUES(\"{}\")".format(nome_convenio.NOME_CONVENIO)

    cursor.execute(sql)

    cursor.close()
    connection.commit()
    connection.close()

    return {"response": "CONVENIO CADASTRADO COM SUCESSO"}

def consulta_todos_convenios():

    connection = conecta_mysql()
    cursor = connection.cursor()

    sql = "SELECT * FROM CONVENIO"

    cursor.execute(sql)
    
     
    columns = [col[0] for col in cursor.description]
    listaconvenios = [dict(zip(columns, row)) for row in cursor.fetchall()]

    cursor.close()
    connection.close()

    return {"response": listaconvenios}

def consulta_convenio(nome_convenio):

    connection = conecta_mysql()
    cursor = connection.cursor()

    sql = "SELECT * FROM CONVENIO WHERE NOME_CONVENIO LIKE \"{}%\"".format(nome_convenio)

    cursor.execute(sql)
    
     
    columns = [col[0] for col in cursor.description]
    listaconvenios = [dict(zip(columns, row)) for row in cursor.fetchall()]
    
    cursor.close()
    connection.close()

    return listaconvenios


def atualiza_convenio(convenio: Convenio, nome_atual_convenio):
    connection = conecta_mysql()
    cursor = connection.cursor()
    id_convenio = consulta_convenio(nome_atual_convenio)[0].get("ID_CONVENIO")

    sql = "UPDATE CONVENIO SET NOME_CONVENIO = \"{}\" WHERE ID_CONVENIO = {}".format(convenio.NOME_CONVENIO, id_convenio)
    cursor.execute(sql)
    
    cursor.close()
    connection.commit()
    connection.close()

    return {"response": "CONVENIO ATUALIZADO COM SUCESSO"}


def deleta_convenio(convenio: Convenio):
    connection = conecta_mysql()
    cursor = connection.cursor()
    id_convenio = consulta_convenio(convenio.NOME_CONVENIO)[0].get("ID_CONVENIO")

    sql = "DELETE FROM CONVENIO WHERE ID_CONVENIO = {}".format(id_convenio)
    cursor.execute(sql)
    
    cursor.close()
    connection.commit()
    connection.close()

    return {"response": "CONVENIO DELETADO COM SUCESSO"}