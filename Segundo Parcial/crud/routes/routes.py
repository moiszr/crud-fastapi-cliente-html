from sqlalchemy.orm import Session

from fastapi import Depends, APIRouter, HTTPException

from crud.config.confiig import SessionLocal
from crud.models import models
from crud.schemas.schemas import *
from typing import List

articulos = APIRouter()

    # Dependency

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


    # Mostrar Tarea Agenda

def leer_tarea(db: Session, codigo: int):
    return db.query(models.Agenda).filter(models.Agenda.codigo == codigo).first()

@articulos.get("/agenda/{codigo}", tags=["Agenda"], response_model=AgendaSalida, description="Leer Tarea")
def Mostrar_Tareas(codigo: int, db: Session = Depends(get_db)):
    tblAgenda = leer_tarea(db, codigo=codigo)
    if tblAgenda is None:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    return tblAgenda
    

        # Mostrar Tareas Agenda

def leer_tareas(db:Session, skip: int = 0, limit: int = 100):
    return db.query(models.Agenda).offset(skip).limit(limit).all()

@articulos.get("/agenda/", tags=["Agenda"], response_model=List[AgendaSalida], description="Leer Tareas")
def Mostrar_Tareas(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    tblAgenda = leer_tareas(db, skip=skip, limit=limit)
    return tblAgenda


        # Crear Tarea Agenda

def crear_tarea_agenda(db: Session, agend: AgendaEntrada):
    tblAgenda = models.Agenda(nombre=agend.nombre, telefono=agend.telefono, correo=agend.correo)
    db.add(tblAgenda)
    db.commit()
    db.refresh(tblAgenda)
    return tblAgenda

@articulos.post("/agenda/", tags=["Agenda"], response_model=AgendaEntrada, description="Agendar")
def Crear_Tarea(agend: AgendaEntrada, db: Session = Depends(get_db)):
    return crear_tarea_agenda(db=db, agend=agend)


        # Eliminar Tarea Agenda

def eliminar_tarea_agenda(db: Session, codigo: int):
    tblAgenda = leer_tarea(db=db, codigo=codigo)
    db.delete(tblAgenda)
    db.commit()

@articulos.delete("/agenda/{codigo}", tags=["Agenda"], description="Eliminar Tarea")
def Eliminar_Tarea(codigo: int, db: Session = Depends(get_db)):
    tblAgenda = leer_tarea(db, codigo=codigo)
    if not tblAgenda:
        raise HTTPException(status_code=404, detail="No se encontro ninguna tarea para eliminar")
    try:
        eliminar_tarea_agenda(db=db, codigo=codigo)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"No se puede eliminar: {e}")
    return {"Estado de eliminación": "Éxito"}
