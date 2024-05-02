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
        "lista5.append('alo')\n",
        "print(lista4)\n",
        "print(lista5)\n",
        "\n",
        "# trabalhando com a lista6 & lista7 , cópia independente\n",
        "lista6 = [\"a\",\"b\",\"c\"]\n",
        "print(lista6)\n",
        "lista7 = lista6[:]\n",
        "lista6.append(\"d\")\n",
        "lista6[0] = \"x\"\n",
        "lista7.append(\"z\")\n",
        "print(lista6)\n",
        "print(lista7)\n",
        "\n",
        "#trabalhando com a lista8 & lista9 & listax & listay , operações de soma e multiplicação com listas\n",
        "lista8 = [\"a\",\"b\",\"c\"]\n",
        "lista9 = [\"d\",\"e\",\"f\"]\n",
        "\n",
        "#somando dus listas em uma nova\n",
        "listax = lista8 + lista9\n",
        "print(listax)\n",
        "\n",
        "#multiplicando uma lista em uma nova\n",
        "listay = listax * 3\n",
        "print(listay)\n",
        "\n",
        "#trabalahando com a lista 10, fatiamento\n",
        "lista10 = [1,2,3,4,5,6,7,8,9,0]\n",
        "print(lista10[2:5])\n",
        "print(lista10[:5])\n",
        "print(lista10[2:])\n",
        "# fatiamento com número negativo\n",
        "print(lista10[-5:-3])\n",
        "print(lista10[:-3])\n",
        "print(lista10[-5:])\n",
        "print(lista10[-5:3])\n",
        "\n",
        "# trabalhando com o Lista11 , usando a concatenação como alternativa ao append\n",
        "\n",
        "lista11 = [1,2,3,4,5]\n",
        "print(lista11)\n",
        "lista11 = lista11 +[\"a\"]\n",
        "print(lista11)\n",
        "lista11 += [\"b\"]\n",
        "print(lista11)\n",
        "lista11 += [6,7,8,9,0]\n",
        "print(lista11)\n",
        "\n",
        "# Trabalhando com o lista12, usando o metodo extend\n",
        "\n",
        "lista12 = []\n",
        "print(lista12)\n",
        "lista12.append(9)\n",
        "print(lista12)\n",
        "lista12.append(8)\n",
        "print(lista12)\n",
        "\n",
        "lista12.extend([7])\n",
        "print(lista12)\n",
        "lista12.extend([6,5,4])\n",
        "print(lista12)\n",
        "lista12.append([3,2,1])\n",
        "print(lista12)\n",
        "print(len(lista12))\n",
        "\n",
        "# Trabalhando com lista13, usando o short para ordenar uma list\n",
        "lista13 = [\"Silvio\",\"Maria\",\"Silvia\",\"Mario\",\"Augusto\"]\n",
        "lista13.sort()\n",
        "print(lista13)\n",
        "\n",
        "#trabalhando com lista14, usando o short para autera a ordem de exibição usando o reverse\n",
        "lista14 = [\"Silvio\",\"Maria\",\"Silvia\",\"Mario\",\"Augusto\"]\n",
        "lista14.sort(reverse= True)\n",
        "print(lista14)\n",
        "\n",
        "#trabalhando com lista15, usando o sorted() para auterar a ordem de exibição usando reverse\n",
        "lista15 = [8,2,6,4,0,9,1,3,7,5]\n",
        "# print(lista15)\n",
        "# print(\" 12 \")\n",
        "\n",
        "#organizando a lista\n",
        "x = sorted(lista15)\n",
        "print(x)\n",
        "print(\"\\nComando\\n\")\n",
        "# ordem inversa numerica\n",
        "sorted(lista15, reverse = True)\n",
        "\n",
        "#acessadno elementos da lista por index()\n",
        "lista16 = [8,2,6,4,0,9,1,3,7,5]\n",
        "print(lista16.index(9))\n",
        "#print(lista16.index(10))\n",
        "\n",
        "# usando o comando del para remover um intem de lista\n",
        "lista17 = [11,22,33,44,66,77,88,99]\n",
        "print(lista17)\n",
        "del lista17[3]\n",
        "\n",
        "print(lista17)\n",
        "\n",
        "del lista17[4:6]\n",
        "\n",
        "print(lista17)\n",
        "# voce poderia ultilizar del lista17[:] mas vou cololcar o Lista17.clear()\n",
        "lista17.clear()\n",
        "print(lista17)\n",
        "\n",
        "# ultilizando pop() com a lista18\n",
        "lista18 = [2,4,6,8,10,12,14,16,18,20]\n",
        "print(lista18)\n",
        "v1 = lista18.pop()\n",
        "print(lista18)\n",
        "print(v1)\n",
        "v2 = lista18.pop(4)\n",
        "print(lista18)\n",
        "print(v2)\n",
        "\n",
        "# ultilizando remove() com a lista19\n",
        "lista19 = [\"a\",\"b\",\"c\",\"d\",\"e\",\"f\",\"g\"]\n",
        "print(lista19)\n",
        "lista19.remove(\"d\")\n",
        "print(lista19)\n",
        "\n",
        "#Criando uma lista partir de um exitente usando a biblioteca Math\n",
        "lista20 = [1,2,3,4,5]\n",
        "lista21 = [math.factorial(i) for i in lista20]\n",
        "\n",
        "print(lista21)\n",
        "\n",
        "# Usando um o métod index através de um elemento dentro de um lista\n",
        "\n",
        "lista22 = [1,2,3,\"quatro\",\"cinco\",\"seis\"]\n",
        "print(lista22)\n",
        "#vai retornar em qual poisição se encontra o elemento procurado\n",
        "print(lista22.index(\"quatro\"))\n"
      ]
    }
  ]
}
