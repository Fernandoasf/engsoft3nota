from Estoque import Estoque
from deletar import deletar_produto

# teste para a função que deleta um produto do estoque


def teste_deletar_produto():
    estoque = Estoque()

    # massa de dados
    estoque.produtos = {1: {'nome': 'feijão',   'valor': 4.50,   'quantidade': 50},
                        2: {'nome': 'arroz',    'valor': 5.50,   'quantidade': 100}
                        }
    # deleta produto já cadastrado
    resposta = deletar_produto(estoque, 2)
    assert "Produto deletado com sucesso" == resposta

    # tenta deletar produto ainda não cadastrado
    resposta = deletar_produto(estoque, 3)
    assert "O produto que você deseja deletar não está cadastrado" == resposta

    # tenta deletar produto que já foi deletado (recai no caso de produto não cadastrado)
    resposta = deletar_produto(estoque, 2)
    assert "O produto que você deseja deletar não está cadastrado" == resposta
