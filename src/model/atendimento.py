from pydantic import BaseModel

class Atendimento(BaseModel):
    DATA_ATENDIMENTO: str
    ID_PACIENTE: int
    ID_CONVENIO: int
    ATENDIMENTO_PAGO: bool
    ID_GUIA: int
    ID_PROCEDIMENTO: int
    VALOR_TOTAL_ATENDIMENTO: float
    VALOR_RECEBER: float
    OBSERVACOES: str