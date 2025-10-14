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
    return {"mensagem": "Bem-Vindo ao Gerenciador de Filmes"}


@app.post("/filmes")
def criar_filmes(titulo: str, genero: str, ano: int, avaliacao: float):
    funcao.inserir_filmes(titulo, genero, ano, avaliacao)
    return{"mensagem": "Filme adicionado com sucesso"}

@app.get("/filmes")
def listar_filmes():
    filmes = funcao.exibir_filmes()
    lista = []
    for linha in filmes:
        lista.append({
            "id": linha[0],           
            "titulo": linha[1],
            "genero": linha[2],
            "ano": linha[3],
            "avaliação":linha[4]
            })
    return{"filmes": lista}

@app.put("/filmes/{id_filmes}")
def atulizar_filmes(id_filme: int,nova_avalicao:float):
    filme = funcao.buscar_filme(id_filme)
    if filme:
        funcao.atualizar_filme(id_filme, nova_avalicao)
        return{"mensagem": "Filme atualizado com sucesso!"}
    else:
        return {"erro": "Filme não encontrado"}