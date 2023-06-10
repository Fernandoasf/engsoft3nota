#função que faz a consulta de um produto específico no estoque

def consultar_produto(estoque,codigo):
    
    if codigo in estoque.produtos:
        nome = estoque.produtos[codigo]['nome']
        valor = estoque.produtos[codigo]['valor']
        quantidade = estoque.produtos[codigo]['quantidade']
        return f"Código: {codigo}, Nome: {nome}, Preço: {valor:.2f}, Quantidade: {quantidade}"
    else:
        return "O produto consultado não está cadastrado no estoque"
