itens_mercado = ["maça", "laranja", "pera"]
item = input("Digite o item que você quer verificar: ")
if item in itens_mercado:
  print(f"O item {item} não precisa ser comprado.")
else:
  print(f"O item {item} precisa ser comprado.")

print(f"Lista de itens: {itens_mercado}")
