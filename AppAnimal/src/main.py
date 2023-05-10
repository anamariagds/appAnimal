from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
from uuid import uuid4

app = FastAPI()

origins = [
    "http://127.0.0.1:5500",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Animal(BaseModel):
    id: Optional[int] 
    nome: str
    idade : int
    sexo : str
    cor : str

animais: list[Animal] = []


@app.get('/animais/')
def listar_animais():
    return animais

@app.get('/animais/{id}')
def ver_animal(id : str):
    for animal in animais:
        if animal.id == id:
            return animal
    return {"erro": "Animal não encontrado."}

@app.post('/novo_animal/')
def cadastrar(animal : Animal):
   animal.id = str(uuid4())
   animais.append(animal)
   return None

@app.delete('/animais/{id}')
def ver_animal(id : str):
    indice = -1
    for index, animal in enumerate(animais):
        if animal.id == id:
            indice = index
            break
    
    if indice != -1:
        animais.pop(indice)
        return {'mensagem': 'Animal removido com sucesso'}
    else:
        return {"erro": "Animal não encontrado."}

