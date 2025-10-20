from conexao import conectar

def criar_tabela():
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS filmes (
            id SERIAL PRIMARY KEY,
            titulo TEXT NOT NULL,
            genero TEXT NOT NULL,
            ano INTEGER NOT NULL,
            avaliacao REAL
            )
            """)
            conexao.commit()
        except Exception as erro:
            print(f"Erro ao criar a tabela {erro}")
        finally:
            cursor.close()
            conexao.close()
criar_tabela()

def inserir_filmes(titulo, genero, ano ,avaliacao):
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute(
                "INSERT INTO filmes (titulo, genero, ano, avaliacao) VALUES (%s, %s, %s, %s)",
                (titulo, genero, ano, avaliacao)
            )
            conexao.commit()
        except Exception as erro:
            print(f"Erro ao inserir filmes {erro}")
        finally:
            cursor.close()
            conexao.close()

def exibir_filmes():
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute(
                "SELECT * FROM filmes ORDER BY id"
            )
            return cursor.fetchall()
        except Exception as erro:
            print(f"Erro ao mostrar  o filmes")
        finally:
            cursor.close()
            conexao.close()

def atualizar_filmes(id_filmes, nova_avaliacao):
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute(
                "UPDATE filmes SET avaliacao = %s WHERE id = %s",
                (nova_avaliacao, id_filmes)
            )
            conexao.commit()
        except Exception as erro:
            print(f"Erro ao tentar atuaizar o filmes {erro}")
        finally:
            cursor.close()
            conexao.close()

def deletar_filmes(id_filmes):
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute("DELETE FROM filmes WHERE id = %s", (id_filmes,))
            conexao.commit()
        except Exception as erro:
            print(f"Erro ao deletar o filmes ")
        finally:
            cursor.close()
            conexao.close()
def buscar_filmes(id_filmes):    
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute(
                "SELECT * FROM filmes WHERE  id = %s", (id_filmes,)
            )
            return cursor.fetchone()
        except Exception as erro:
            print(f"Erro ao mostrar  o filmes")
        finally:
            cursor.close()
            conexao.close()