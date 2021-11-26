from pydantic import BaseModel
from typing import Optional

class AgendaSalida(BaseModel):
    codigo: Optional[int]
    nombre: str
    telefono: str
    correo: str

    class Config:
        orm_mode = True

        
class AgendaEntrada(BaseModel):
    nombre: str
    telefono: str
    correo: str

    class Config:
        orm_mode = True