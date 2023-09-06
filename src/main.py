from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from model.paciente import Paciente
from model.convenio import Convenio
from model.guia import Guia
from model.procedimento import Procedimento
from model.atendimento import Atendimento

from business.paciente_business import cadastra_paciente, \
    consulta_todos_pacientes, \
    consulta_paciente, \
    atualiza_paciente, \
    deleta_paciente

from business.convenio_business import cadastrar_convenio, \
    consulta_todos_convenios, \
    consulta_convenio, \
    atualiza_convenio, \
    deleta_convenio

from business.guia_business import cadastrar_guia, \
    consulta_todas_guias, \
    consulta_guia, \
    atualiza_guia, \
    deleta_guia

from business.procedimento_business import cadastrar_procedimento, \
    consulta_todos_procedimentos, \
    consulta_procedimento, \
    atualiza_procedimento, \
    deleta_procedimento

from business.atendimento_business import cadastrar_atendimento, \
    consulta_todos_atendimentos, \
    consulta_atendimento, \
    atualiza_atendimento, \
    deleta_atendimento

app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
##INICIO PACIENTE
@app.post("/cadastra_paciente/")
def post_cadastra_paciente(nome_paciente: Paciente):    
    return cadastra_paciente(nome_paciente)

@app.get("/consulta_paciente/")
def get_consulta_paciente(nome_paciente: str):    
    return consulta_paciente(nome_paciente)

@app.get("/consulta_todos_pacientes")
def get_consulta_todos_pacientes():
    return consulta_todos_pacientes()

@app.patch("/atualiza_paciente/")
def patch_atualiza_paciente(nome_atual_paciente: str, nome_paciente: Paciente):
    return atualiza_paciente(nome_paciente, nome_atual_paciente)

@app.delete("/deleta_paciente/")
def delete_deleta_paciente(nome_paciente: Paciente):
    return deleta_paciente(nome_paciente)
##FIM PACIENTE

##INICIO CONVENIO
@app.post("/cadastra_convenio/")
def post_cadastra_convenio(nome_convenio: Convenio):    
    return cadastrar_convenio(nome_convenio)

@app.get("/consulta_convenio/")
def get_consulta_convenio(nome_convenio: str):    
    return consulta_convenio(nome_convenio)

@app.get("/consulta_todos_convenios")
def get_consulta_todos_convenios():
    return consulta_todos_convenios()

@app.patch("/atualiza_convenio/")
def patch_atualiza_convenio(nome_atual_convenio: str, nome_convenio: Convenio):
    return atualiza_convenio(nome_convenio, nome_atual_convenio)

@app.delete("/deleta_convenio/")
def delete_deleta_convenio(nome_convenio: Convenio):
    return deleta_convenio(nome_convenio)
##FIM CONVENIO

##INICIO GUIA
@app.post("/cadastra_guia/")
def post_cadastra_guia(codigo_guia: Guia):    
    return cadastrar_guia(codigo_guia)

@app.get("/consulta_guia/")
def get_consulta_guia(codigo_guia: str):    
    return consulta_guia(codigo_guia)

@app.get("/consulta_todas_guias")
def get_consulta_todas_guias():
    return consulta_todas_guias()

@app.patch("/atualiza_guia/")
def patch_atualiza_guia(codigo_atual_guia: str, codigo_guia: Guia):
    return atualiza_guia(codigo_guia, codigo_atual_guia)

@app.delete("/deleta_guia/")
def delete_deleta_guia(codigo_guia: Guia):
    return deleta_guia(codigo_guia)
##FIM GUIA


##INICIO PROCEDIMENTO
@app.post("/cadastra_procedimento/")
def post_cadastrar_procedimento(codigo_procedimento: Procedimento):    
    return cadastrar_procedimento(codigo_procedimento)

@app.get("/consulta_procedimento/")
def get_consulta_procedimento(codigo_procedimento: str):    
    return consulta_procedimento(codigo_procedimento)

@app.get("/consulta_todos_procedimentos")
def get_consulta_todos_procedimentos():
    return consulta_todos_procedimentos()

@app.patch("/atualiza_procedimento/")
def patch_atualiza_procedimento(codigo_atual_procedimento: str, codigo_procedimento: Procedimento):
    return atualiza_procedimento(codigo_procedimento, codigo_atual_procedimento)

@app.delete("/deleta_procedimento/")
def delete_deleta_procedimento(codigo_procedimento: Procedimento):
    return deleta_procedimento(codigo_procedimento)
##FIM PROCEDIMENTO

##INICIO PROCEDIMENTO
@app.post("/cadastra_atendimento/")
async def post_cadastrar_atendimento(atendimento: Atendimento):    
    return cadastrar_atendimento(atendimento)

@app.get("/consulta_todos_atendimentos")
def get_consulta_todos_atendimento():
    return consulta_todos_atendimentos()

@app.get("/consulta_atendimento")
def get_consulta_atendimento(id_atendimento: int):
    return consulta_atendimento(id_atendimento)

@app.put("/atualiza_atendimento")
def put_atualiza_atendimento(atendimento: Atendimento, id_atendimento: int ):
    return atualiza_atendimento(atendimento, id_atendimento)

@app.delete("/deleta_atendimento")
def delete_atendimento(id_atendimento: int ):
    return deleta_atendimento(id_atendimento)
##FIM PROCEDIMENTO
