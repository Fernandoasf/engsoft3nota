import unittest
from unittest import mock
import psycopg2


class TestAdicionarProduto(unittest.TestCase):
    @mock.patch('psycopg2.connect')
    def test_adicionar_produto(self, mock_connect):
        # Configurando o mock para retornar um mock de cursor
        mock_cursor = mock_connect.return_value.cursor.return_value

        # Emulando uma consulta que retorna 1 (produto já existe)
        mock_cursor.fetchone.return_value = (1,)

        # Executando o teste
        result1 = adicionar_produto("Produto A", "Descrição A", 10.99, 5)

        # Verificando o resultado
        self.assertEqual(result1, "O produto já existe no banco de dados.")

        # Emulando uma consulta que retorna 0 (produto não existe)
        mock_cursor.fetchone.return_value = (0,)

        # Executando o teste novamente
        result2 = adicionar_produto("Produto B", "Descrição B", 15.99, 8)

        # Verificando o resultado
        self.assertEqual(result2, "Produto adicionado com sucesso.")


if __name__ == '__main__':
    unittest.main()


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
