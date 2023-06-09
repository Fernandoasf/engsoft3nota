#função que adiciona um produto no estoque
def adicionar_produto(estoque, codigo, nome, valor, quantidade):

    if codigo not in estoque.produtos:
        estoque.produtos[codigo] = {'nome': nome, 'valor': valor, 'quantidade': quantidade}
        return "Produto adicionado com sucesso"
    else:
        return "Um produto com o mesmo código já foi adicionado"
