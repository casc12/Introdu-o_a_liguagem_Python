a = []\n
s = 0\n
        
print("Somatório de valores informados")
       
#Entrada de Dados
i = 0\n
resp = 'S'
while(resp.upper() == 'S'):
  a.append(float(input(\"\\nEntre o {0:3})o. valor: \".format(i+1))))
  s += a[i]
  i += 1
  print()
  print("Deseja continuar?")
  resp = input("Tecle [S] para sim / qualquer caractere para NAO: ")
# Apresentação dos Dados
print()
for i in range(len(a)):
  print(\"A[{0:3}] = {1:8,.2f} na posição {2:3}.\".format(i + 1,a[i],i))
  
print()
print(\"Soma dos valores informados= {0:8,.2f}\".format(s))
        
enter = input("\nPressione <Enter> para encerrar... ")
   
