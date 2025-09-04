dados = input("Digite os dados do aluno no formato: Nome, Idade, Nota separados por vírgula: ").split(", ")
for i in range(0, len(dados), 3):
  nome, idade, nota = dados[i], dados[i+1], dados[i+2]
  print(f"Aluno: {nome}")
  print(f"Idade: {idade}")
  print(f"Nota: {nota}")
  print(" ")