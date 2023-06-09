#função que atualiza os dados de um produto
def atualizar_produto(estoque, codigo, novo_nome, novo_valor, nova_quantidade):
    if codigo in estoque.produtos:
        estoque.produtos[codigo]['nome'] = novo_nome
        estoque.produtos[codigo]['valor'] = novo_valor
        estoque.produtos[codigo]['quantidade'] = nova_quantidade
        return "Produto atualizado com sucesso"
    else:
        return "O produto que você deseja atualizar ainda está cadastrado"


    