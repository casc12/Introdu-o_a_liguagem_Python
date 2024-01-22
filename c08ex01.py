
        a = []\n
        b = []\n
        
        
        print(\"Exemplo de checagem de índice\\n \")
        
        #Entrada de dados\n
        
        for i in range(10):
          valor = int(input(\"Entre como {0:2}º valor: \".format(i+1)))
          a.append(valor)
           #print(a[i])
        
        #Processamento par ou impar\n
        
        print()\n
        for i in range(10):
          if( i % 2 == 0):
            b.append(a[i] * 5)\n",
          else:\n
            b.append(a[i] + 5)
        
        
        #Apresentações da listas
        print()
        for i in range(10):
          print(\"A[{0:2}] = {1:4} na posição {2:2}.\".format(i + 1, a[i], i ))
        
        print()\n
        for i in range(10):\n
          print(\"B[{0:2}] = {1:4} na  posição {2:2}\".format(i + 1, b[i], i))
        
        enter = input("\nPressione <Enter> para encerrar ...")
      
