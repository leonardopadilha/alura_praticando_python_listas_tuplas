notas = input("Digite as notas dos alunos separadas por vírgula: ").split(", ")
notas = [float(nota) for nota in notas]
print(f"Média final da turma: {(sum(notas) / len(notas)):.2f}")