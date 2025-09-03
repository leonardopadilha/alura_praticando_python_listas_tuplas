convidados = ["Ana", "Carlos", "Pedro"]
print(f"Lista original: {convidados}")

nome_incorreto = input("Digite o nome incorreto: ")
nome_correto = input("Digite o nome correto: ")

posicao_nome_incorretol = convidados.index(nome_incorreto)
convidados[posicao_nome_incorretol] = nome_correto
print(f"O nome {nome_incorreto} foi substituído para {nome_correto}")
print(f"Lista atualizada: {convidados}")