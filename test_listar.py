from Estoque import Estoque
from listar import listar_produtos

#teste para a função que lista os dados de todos os produtos cadastrados

def teste_listar_produtos():
    estoque = Estoque()

    # massa de dados
    estoque.produtos = {1: {'nome': 'feijão', 'valor': 4.50, 'quantidade': 50},
                        2: {'nome': 'arroz', 'valor': 5.50, 'quantidade': 100},
                        3: {'nome': 'macarrão', 'valor': 3.30, 'quantidade': 30},
                        4: {'nome': 'leite', 'valor': 8.50, 'quantidade': 75}
                        }

    # lista os 4 produtos do estoque, um em cada linha
    resposta = listar_produtos(estoque)
    esperado = "Código: 1, Nome: feijão, Preço: 4.50, Quantidade: 50\n" \
               "Código: 2, Nome: arroz, Preço: 5.50, Quantidade: 100\n" \
               "Código: 3, Nome: macarrão, Preço: 3.30, Quantidade: 30\n" \
               "Código: 4, Nome: leite, Preço: 8.50, Quantidade: 75\n"
    assert esperado == resposta

    #nova massa de dados
    estoque.produtos = {}

    #tenta listar os produtos de um estoque vazio
    resposta = listar_produtos(estoque)
    assert "Não há produtos para serem listados" == resposta