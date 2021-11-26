from sqlalchemy import Column, Integer, String
from crud.config.confiig import Base

class Agenda(Base):
    __tablename__ = 'agenda'

    codigo = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(70))
    telefono = Column(String(11))
    correo = Column(String)
