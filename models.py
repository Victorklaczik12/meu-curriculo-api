from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from database import Base

class Mensagem(Base):
    __tablename__ = "mensagens"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    email = Column(String, nullable=False)
    mensagem = Column(String, nullable=False)
    data_envio = Column(DateTime, default=datetime.utcnow)

class Visita(Base):
    __tablename__ = "visitas"

    id = Column(Integer, primary_key=True, index=True)
    data_visita = Column(DateTime, default=datetime.utcnow)