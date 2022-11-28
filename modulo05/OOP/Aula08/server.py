from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get('/profile')
def profile():
    return {"Nome": "David Simas"}

@app.post('/profile')
def signup():
    return {"Menssagem": "Perfil criado com sucesso"}

@app.put('/profile')
def atualizar():
    return {"Menssagem": "Perfil atualizado com sucesso"}

@app.delete('/profile')
def remover():
    return {"Menssagem": "Perfil excluido com sucesso"}


"""
    - Paramentro de ROTA
"""

@app.get('/saudacao/{nome}')
def saudacao(nome: str):
    texto = f"Olá {nome}, tudo bem com você?"
    return {"Mensagem": texto}
# Para acessar no navegador digite: localhost:8000/saudacao/passando_um_nome

@app.get('/quadrado/{numero}')
def quadrado(numero: int):
    resultado = numero * numero
    texto = f"O quadrado de {numero} é {resultado}"
    return {"Mensagem": texto}


"""
    - Parametros de QUERY STRING
"""

@app.get('/dobro')
def dobreo(valor: int):
    resultado = 2 * valor
    return {"Resultaod": f"O dobre de {valor} é {resultado}"}
# Para acessar no navegador digite: localhost:8000/dobro?valor=4

# Passando dois paramentros
@app.get('/area_retangulo')
def area_retangulo(largura: int, altura: int):
    area = largura * altura
    return {"Resultaod": f"A area do retangulo é {area}"}
# Para acessar no navegador digite: localhost:8000/area_retangulo?largura=4&altura=5

# Com valor padrão
@app.get('/area_quadrado')
def area_quadrado(largura: int, altura: int = 1):
    area = largura * altura
    return {"Resultaod": f"A area do quadrado é {area}"}
# Para acessar no navegador digite: localhost:8000/area_quadrado?largura=3


"""
    - Request Body
"""
class Produto(BaseModel):
    nome: str
    preco: float

@app.post('/produtos')
def produtos(produto: Produto):
    return {"Mensagem": f"Produto ({produto.nome} - R${produto.preco}) cadastrado com sucesso."}