notas = [85, 70, 90, 60, 75]

print(f"Lista original: {notas}")

# Usando sort() - modifica a lista original
notas.sort()
print(f"Após notas.sort(): {notas}")

# Resetando a lista para demonstrar sorted()
notas = [85, 70, 90, 60, 75]
print(f"\nLista resetada: {notas}")

# Usando sorted() - cria uma nova lista
notas_ordenadas = sorted(notas)
print(f"Resultado de sorted(notas): {notas_ordenadas}")
print(f"Lista original permanece: {notas}")

# Demonstração adicional
print(f"\nnotas.sort() retorna: {notas.sort()}")
print(f"sorted(notas) retorna: {sorted(notas)}")