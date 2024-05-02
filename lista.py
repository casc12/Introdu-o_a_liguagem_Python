import math
lista1 = [1,2,3,4,5]
      
#chamando a lista1
print(lista1)
       
#pegando o segundo elemento da lista
print(lista1[1])
      
#pegando o quinto elemento da lista\n",
print(lista1[4])
        
#saber o tipo de objeto python,
print(type(lista1))\n",
        
#erro de indexação posição inexistente na lista
#print(lista1[5])
       
        
#trabalhando com a lista2
lista2 = [1,3,5,7,9]
print(lista2[2])
#usando um index negtivo
print(lista2[-1])\n",
#pegando o valor da primeira posição da lista
print(lista2[0])
        
#pegando um valor negativo
print(lista2[-2])\n",
      
#tabalhando com a lista3, em que se mostra que os valores dentro de uma poisção ou index podem ser trocados
lista3 = [2,4,6,8]
print(lista3)
lista3[2]=9
print(lista3)
       
       
# trabalhando com a lista4 & lista5, copias com lista cópia espelhada
lista4 = [11,22,33,44,55]
print(lista4)
#lista5 vai receber lista4 e vai referênciar a mesma memoria tb
lista5 = lista4
print(lista5)
lista4.append(66)
lista4[0] = 99
lista5.append('alo')
print(lista4)
print(lista5)
        
# trabalhando com a lista6 & lista7 , cópia independente
lista6 = ["a","b","c"]
print(lista6)
lista7 = lista6[:]
lista6.append("d")
lista6[0] = "x"
lista7.append("z")
print(lista6),
print(lista7)
        
#trabalhando com a lista8 & lista9 & listax & listay , operações de soma e multiplicação com listas
lista8 = ["a","b","c"]
lista9 = ["d","e","f"]
        
#somando dus listas em uma nova
listax = lista8 + lista9
print(listax)
        
#multiplicando uma lista em uma nova\n",
listay = listax * 3
print(listay)
       
#trabalahando com a lista 10, fatiamento\n",
lista10 = [1,2,3,4,5,6,7,8,9,0]
print(lista10[2:5])
print(lista10[:5])
print(lista10[2:])
# fatiamento com número negativo
print(lista10[-5:-3])
print(lista10[:-3])
print(lista10[-5:])
print(lista10[-5:3])
        
# trabalhando com o Lista11 , usando a concatenação como alternativa ao append
        
lista11 = [1,2,3,4,5]
print(lista11)
lista11 = lista11 +["a"]
print(lista11)
lista11 += ["b"]
print(lista11)
lista11 += [6,7,8,9,0]
print(lista11)
        
# Trabalhando com o lista12, usando o metodo extend
        
lista12 = []
print(lista12)
lista12.append(9)
print(lista12)
lista12.append(8)
print(lista12)
       
lista12.extend([7])
print(lista12)
lista12.extend([6,5,4])
print(lista12)
lista12.append([3,2,1])
print(lista12)
print(len(lista12))
        
# Trabalhando com lista13, usando o short para ordenar uma list
lista13 = ["Silvio","Maria","Silvia","Mario","Augusto"]
lista13.sort()
print(lista13)
        
#trabalhando com lista14, usando o short para autera a ordem de exibição usando o reverse\
lista14 = ["Silvio","Maria","Silvia","Mario","Augusto"]
lista14.sort(reverse= True)
print(lista14)
        
#trabalhando com lista15, usando o sorted() para auterar a ordem de exibição usando reverse
lista15 = [8,2,6,4,0,9,1,3,7,5]
# print(lista15)
# print(\" 12 \")
        
#organizando a lista
x = sorted(lista15)
print(x)
print("\nComando\n")
# ordem inversa numerica\n",
sorted(lista15, reverse = True)\n",
        
#acessadno elementos da lista por index()\n",
lista16 = [8,2,6,4,0,9,1,3,7,5]
print(lista16.index(9))
#print(lista16.index(10))
        
# usando o comando del para remover um intem de lista
lista17 = [11,22,33,44,66,77,88,99]
print(lista17)
del lista17[3]
        
print(lista17)
        
del lista17[4:6]
   
print(lista17)
# voce poderia ultilizar del lista17[:] mas vou cololcar o Lista17.clear()
lista17.clear()
print(lista17)
        
# ultilizando pop() com a lista18
lista18 = [2,4,6,8,10,12,14,16,18,20]
print(lista18)
v1 = lista18.pop()
print(lista18)\n",
print(v1)
v2 = lista18.pop(4)
print(lista18)
print(v2)
        
# ultilizando remove() com a lista19
lista19 = ["a","b","c","d","e","f","g"]
print(lista19)
lista19.remove("d")
print(lista19)
        
#Criando uma lista partir de um exitente usando a biblioteca Math
lista20 = [1,2,3,4,5]
lista21 = [math.factorial(i) for i in lista20]\
        
print(lista21)
        
# Usando um o métod index através de um elemento dentro de um lista
        
lista22 = [1,2,3,"quatro","cinco","seis"]
print(lista22)
#vai retornar em qual poisição se encontra o elemento procurado
print(lista22.index("quatro"))
