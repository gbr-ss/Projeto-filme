from conexao import conectar

def criar_tabela():
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS filme (
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

def inserir_filme(titulo, genero, ano ,avaliacao):
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute(
                "INSERT INTO filme (titulo, genero, ano, avaliacao) VALUES (%s, %s, %s, %s)",
                (titulo, genero, ano, avaliacao)
            )
            conexao.commit()
        except Exception as erro:
            print(f"Erro ao inserir filme {erro}")
        finally:
            cursor.close()
            conexao.close()

def listar_filme():
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute(
                "SELECT * FROM filme",
                ()
            )
            return cursor.fetchall()
        except Exception as erro:
            print(f"Erro ao mostrar  o filme")
        finally:
            cursor.close()
            conexao.close()

def atualizar_filme(id_filme, nova_avaliacao):
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute(
                "UPDATE filme SET avaliacao = %s WHERE id = %s",
                (nova_avaliacao, id_filme)
            )
            conexao.commit()
        except Exception as erro:
            print(f"Erro ao tentar atuaizar o filme {erro}")
        finally:
            cursor.close()
            conexao.close()

def deletar_filme(id_filme):
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute("DELETE FROM filme WHERE id = ?", (id_filme))
            conexao.commit()
        except Exception as erro:
            print(f"Erro ao deletar o filme ")
        finally:
            cursor.close()
            conexao.close()