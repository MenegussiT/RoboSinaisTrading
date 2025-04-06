from sqlalchemy import Column, Integer, String, DateTime, Float
from .db import Base
from datetime import datetime, UTC

class Signal(Base):
    __tablename__ = "signals"

    id = Column(Integer, primary_key=True, index=True)
    ativo = Column(String)
    horario_entrada = Column(DateTime)
    ordem = Column(String)
    reentrada_1 = Column(DateTime, nullable=True)
    reentrada_2 = Column(DateTime, nullable=True)
    status = Column(String, default="Pendente") # GAIN, LOSS ou Pendente
    resultado = Column(Float, nullable=True) 
    created_at = Column(DateTime, default=lambda: datetime.now(UTC))
    updated_at = Column(DateTime, default=lambda: datetime.now(UTC), onupdate=lambda: datetime.now(UTC))
    

