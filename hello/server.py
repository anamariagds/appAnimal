from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

@app.get("/") #mapeando a url, responde ao metodo get(busca pela url)
async def root():
    return {"mensagem": "Olá, FastAPI!"}

@app.get('/hello/{nome}')
def hello(nome: str):
    texto = f'Bem-Vinde, {nome}!'
    return {"mensagem": texto}

@app.get('/quadrado/{x}')
def quadrado(x: int):
    quadrado = x*2
    return {"resultado": quadrado}

@app.get('/soma/{x}')
def soma(x: int, y:int=4):
    soma = x+y
    texto = f'A soma de {x} e {y}= {soma}'
    return {"resultado": texto}

class Produto(BaseModel):
    nome: str
    preco : float

@app.post('/produtos')
def produtos(produto : Produto):
    return {'mensagem': f'{produto.nome} - R${produto.preco} cadastrado com sucesso!'}

