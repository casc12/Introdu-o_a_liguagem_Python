escolar = {}

#Entrada de dados
for i in range(8):
  nome = input("Entre com o nome {0:2}° aluno: ".format(i+1))
  escolar[i] = nome

#Apresentação das listas
print()
for i in range(8):
  print("Aluno {0} ...: {1} ".format(i+1, escolar[i]))

enter = input("\nPressione <Enter> para encerrar")
