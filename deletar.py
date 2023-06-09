#função que deleta um produto do estoque
def deletar_produto(estoque, codigo):

    if codigo in estoque.produtos:
        del estoque.produtos[codigo]
        return "Produto deletado com sucesso"
    else: 
        return "O produto que você deseja deletar não está cadastrado"
