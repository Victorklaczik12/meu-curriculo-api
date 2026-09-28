from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

# Schema para validar os dados que VÊM do formulário (Front-End)
class MensagemCreate(BaseModel):
    nome: str
    email: str
    mensagem: str


# Schema para RETORNAR os dados da mensagem ao cliente (com ID e Data gerados pelo banco)
class MensagemResponse(BaseModel):
    id: int
    nome: str
    email: str
    mensagem: str
    data_envio: datetime

    class Config:
        from_attributes = True # Permite converter o modelo do SQLAlchemy direto para JSON


# Schema para retornar as métricas/estatísticas do dashboard
class AnalyticsResponse(BaseModel):
    total_visitas: int
    total_mensagens: int


# Schema para retornar os dados da visita registada
class VisitaResponse(BaseModel):
    id: int
    data_visita: datetime

    class Config:
        from_attributes = True