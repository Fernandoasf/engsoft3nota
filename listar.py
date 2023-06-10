# função que lista os dados de todos os produtos cadastrados

def listar_produtos(estoque):
    if len(estoque.produtos) > 0:
        lista = ""
        for codigo, produto in estoque.produtos.items():
            nome = produto['nome']
            valor = produto['valor']
            quantidade = produto['quantidade']
            linha = f"Código: {codigo}, Nome: {nome}, Preço: {valor:.2f}, Quantidade: {quantidade}\n"
            lista += linha
        return lista
    else:
        return "Não há produtos para serem listados"
