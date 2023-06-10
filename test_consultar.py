from Estoque import Estoque
from consultar import consultar_produto

# teste para a função que faz a consulta de um produto específico no estoque


def teste_consultar_produto():
    estoque = Estoque()

    # massa de dados
    estoque.produtos = {1: {'nome': 'feijão', 'valor': 4.50, 'quantidade': 50},
                        2: {'nome': 'arroz', 'valor': 5.50, 'quantidade': 100},
                        3: {'nome': 'macarrão', 'valor': 3.30, 'quantidade': 30},
                        4: {'nome': 'leite', 'valor': 8.50, 'quantidade': 75}
                        }

    # consulta o produto de código 2
    resposta = consultar_produto(estoque, 2)
    assert "Código: 2, Nome: arroz, Preço: 5.50, Quantidade: 100" == resposta

    # consulta o produto de código 3
    resposta = consultar_produto(estoque, 3)
    assert "Código: 3, Nome: macarrão, Preço: 3.30, Quantidade: 30" == resposta

    # consulta o produto de código 5 (não cadastrado)
    resposta = consultar_produto(estoque, 5)
    assert "O produto consultado não está cadastrado no estoque" == resposta
