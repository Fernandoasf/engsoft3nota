import unittest
from unittest import mock
import psycopg2
import Teste_adicionar

def adicionar_produto(nome, descricao, preco, quantidade):

    # Convertendo o nome e a descrição para maiúsculas
    nome = nome.upper()
    descricao = descricao.upper()

    # Conectar ao banco de dados
    conn = psycopg2.connect(
        database="mydatabase",
        user="myuser",
        password="mypassword"
    )

    # Verificar se o produto já existe
    cursor = conn.cursor()
    query = "SELECT COUNT(*) FROM produtos WHERE UPPER(nome) = %s AND UPPER(descricao) = %s"
    cursor.execute(query, (nome, descricao))
    count = cursor.fetchone()[0]
    if count > 0:
        cursor.close()
        conn.close()
        return "O produto já existe no banco de dados."

    # Inserir o produto no banco de dados
    query = "INSERT INTO produtos (nome, descricao, preco, quantidade) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, (nome, descricao, preco, quantidade))

    # Confirmar a transação e fechar a conexão
    conn.commit()
    cursor.close()
    conn.close()

    return "Produto adicionado com sucesso."
