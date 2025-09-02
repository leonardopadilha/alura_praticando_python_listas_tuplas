def registrar_voluntario():
  lista_voluntarios = []
  participante = input("Digite o nome do voluntario ou sair para encerrar: ")
  while participante != "sair":
    lista_voluntarios.append(participante)
    participante = input("Digite o nome do voluntario ou sair para encerrar: ")
  return f"Voluntarios registrados: {lista_voluntarios}"



print(registrar_voluntario())
