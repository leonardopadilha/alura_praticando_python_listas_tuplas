pedido = input("Pedidos feitos (separados por vírgula): ").split(", ")
pedido.pop() # remove o último item da lista
print(f"Pedidos finais: {pedido}")