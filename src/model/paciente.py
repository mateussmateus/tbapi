from pydantic import BaseModel

class Paciente(BaseModel):
    NOME_PACIENTE: str