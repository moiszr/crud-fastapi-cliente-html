from fastapi import FastAPI
from starlette.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from .routes.routes import articulos

from .models import models
from .config.confiig import engine

models.Base.metadata.create_all(bind=engine)

description = '''
Practica Segundo parcial 

Moises Nuñez del Rosario'''

app = FastAPI(
    title='Segundo Parcial',
    description=description,
    version=202010457,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

app.include_router(articulos)

@app.get("/")
def main():
    return RedirectResponse(url="/docs/")
