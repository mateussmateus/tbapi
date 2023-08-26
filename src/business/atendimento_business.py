from datetime import datetime
from model.atendimento import Atendimento
from helpers.conect import conecta_mysql

def cadastrar_atendimento(atendimento: Atendimento):

    connection = conecta_mysql()
    cursor = connection.cursor()
    
    datestr = datetime.strptime(atendimento.DATA_ATENDIMENTO, '%Y-%m-%d')
    

    sql = "INSERT INTO ATENDIMENTO (DATA_ATENDIMENTO, \
        ID_PACIENTE, ID_CONVENIO, ATENDIMENTO_PAGO,\
        ID_GUIA, ID_PROCEDIMENTO, VALOR_TOTAL_ATENDIMENTO, \
        VALOR_RECEBER, OBSERVACOES) VALUES('{}', {}, {}, {}, {}, {}, {}, {}, \"{}\")". \
        format(datestr, atendimento.ID_PACIENTE, atendimento.ID_CONVENIO, \
               atendimento.ATENDIMENTO_PAGO, atendimento.ID_GUIA, atendimento.ID_PROCEDIMENTO, \
               atendimento.VALOR_TOTAL_ATENDIMENTO, atendimento.VALOR_RECEBER, atendimento.OBSERVACOES)

    cursor.execute(sql)

    cursor.close()
    connection.commit()
    connection.close()

    return {"response": "ATENDIMENTO CADASTRADO COM SUCESSO"}

def consulta_todos_atendimentos():

    connection = conecta_mysql()
    cursor = connection.cursor()

    sql = "SELECT * FROM ATENDIMENTO"

    cursor.execute(sql)
    
     
    columns = [col[0] for col in cursor.description]
    listaatendimentos = [dict(zip(columns, row)) for row in cursor.fetchall()]

    cursor.close()
    connection.close()

    return {"response": listaatendimentos}

def consulta_atendimento(id_atendimento):

    connection = conecta_mysql()
    cursor = connection.cursor()

    sql = "SELECT * FROM ATENDIMENTO WHERE ID_ATENDIMENTO ={}".format(id_atendimento)

    cursor.execute(sql)
    
     
    columns = [col[0] for col in cursor.description]
    atendimento = [dict(zip(columns, row)) for row in cursor.fetchall()]
    
    cursor.close()
    connection.close()

    return atendimento


def atualiza_atendimento(atendimentoatualizado: Atendimento, id_atendimento):
    connection = conecta_mysql()
    cursor = connection.cursor()
    atendimento = consulta_atendimento(id_atendimento)[0]

    sql = "UPDATE ATENDIMENTO SET DATA_ATENDIMENTO = \"{}\", ID_PACIENTE = {}, ID_CONVENIO = {}, \
            ATENDIMENTO_PAGO = {}, ID_GUIA = {}, ID_PROCEDIMENTO = {}, VALOR_TOTAL_ATENDIMENTO = {} \
            , VALOR_RECEBER = {}, OBSERVACOES = \"{}\" \
            WHERE ID_ATENDIMENTO = {}".format(atendimentoatualizado.DATA_ATENDIMENTO, atendimentoatualizado.ID_PACIENTE, \
                                              atendimentoatualizado.ID_CONVENIO, atendimentoatualizado.ATENDIMENTO_PAGO, \
                                              atendimentoatualizado.ID_GUIA, atendimentoatualizado.ID_PROCEDIMENTO, \
                                              atendimentoatualizado.VALOR_TOTAL_ATENDIMENTO, atendimentoatualizado.VALOR_RECEBER, \
                                              atendimentoatualizado.OBSERVACOES, id_atendimento)
    cursor.execute(sql)
    
    cursor.close()
    connection.commit()
    connection.close()

    return {"response": "ATENDIMENTO ATUALIZADO COM SUCESSO"}


def deleta_atendimento(id_atendimento):
    connection = conecta_mysql()
    cursor = connection.cursor()

    sql = "DELETE FROM ATENDIMENTO WHERE ID_ATENDIMENTO = {}".format(id_atendimento)
    cursor.execute(sql)
    
    cursor.close()
    connection.commit()
    connection.close()

    return {"response": "ATENDIMENTO DELETADO COM SUCESSO"}