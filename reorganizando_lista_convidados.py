lista_convidados = []
qtd_convidados = int(input("Digite a quantidade de convidados:"))

for index, convidado in enumerate(range(qtd_convidados)):
  nome_convidados = input(f"Digite o nome do {index+1}º convidado:")
  lista_convidados.append(nome_convidados)

print(f"Lista atual de convidados: {lista_convidados}")

novo_convidado = input("\nDeseja adicionar um novo convidado? (s/n):")
if novo_convidado.lower() == "s":
  nome_novo_convidado = input("Digite o nome do novo convidado:")
  posicao_novo_convidado = int(input("Digite a posição na qual deseja inserir o convidado: "))
  if posicao_novo_convidado > len(lista_convidados):
    lista_convidados.append(nome_novo_convidado)
  lista_convidados.insert(posicao_novo_convidado - 1, nome_novo_convidado)

print(f"Lista atualizada de convidados: {lista_convidados}")

