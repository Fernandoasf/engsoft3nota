from Estoque import Estoque
from atualizar import atualizar_produto

#teste para a função que atualiza os dados de um produto
def teste_atualizar_produto():

    estoque = Estoque()

    #massa de dados
    estoque.produtos =  { 1: {'nome': 'feijão',   'valor': 4.50,   'quantidade': 50}, 
                          2: {'nome': 'arroz',    'valor': 5.50,   'quantidade': 100}
                        }
    
    #atualiza produto de código igual a 1
    resposta = atualizar_produto(estoque, 1, "macarrão", 3.30, 30)
    assert "Produto atualizado com sucesso" == resposta

    #tenta atualizar produto de código igual a 3 (não cadastrado)
    resposta = atualizar_produto(estoque, 3, "leite", 8.50, 75)
    assert "O produto que você deseja atualizar ainda está cadastrado"


    
    

