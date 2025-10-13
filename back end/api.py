from fastapi import FastAPI
import funcao

#Rodar o fastapi:
# python -m uvicorn api:app --reload

#testar api FastAPI
#/docs > documentação swagger
#/redoc > documentação redoc

#GET = pegar / Listar
#POST = Criar / Enviar
#PUT = Atualizar
#DELETE = Deletar

#Iniciar o fastapi
app = FastAPI(title="Gerenciador de Filmes") 

@app.get("/")
def home():
    return {"mensagem": "Quero ir para casa🏠"}


@app.post("/filmes")
def criar_filmes(titulo: str, genero: str, ano: int, avaliacao: float):
    funcao.inserir_filme(titulo, genero, ano, avaliacao)
    return{"mensagem": "Filme adicionado com sucesso"}

@app.get("/filmes")
def listar_filmes():
    filmes = funcao.listar_filme()
    lista = []
    for linha in filmes:
        lista.append({
            "id": linha[0],           
            "titulo": linha[1],
            "genero": linha[2],
            "ano": linha[3],
            "avaliação":linha[4]
            })
    return{"filme": lista}