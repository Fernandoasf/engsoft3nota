from Estoque import Estoque
from adicionar import adicionar_produto

#teste para a função que adicuona um produto no estoque 
def teste_adicionar_produto():
    estoque = Estoque()

    #adiciona produto cujo código ainda não está cadastrado
    resposta = adicionar_produto(estoque, 1, 'feijão', 4.50, 30, False)
    assert "Produto adicionado com sucesso" == resposta

    #tenta adicionar produto cujo código já está cadastrado 
    resposta = adicionar_produto(estoque, 1, 'arroz', 5.50, 100, False)
    assert "Um produto com o mesmo código já foi adicionado" == resposta

    #caso de cancelamento
    resposta = adicionar_produto(estoque, 1, 'arroz', 5.50, 100, True)
    assert "Operação cancelada" == resposta
