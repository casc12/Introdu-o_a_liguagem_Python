{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNa9i6234+4kztZ0GDZ/kV8",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/casc12/Introdu-o_a_liguagem_Python/blob/Cap08/lista.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 20,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Cbh9h9bc5Dln",
        "outputId": "fb84186b-791b-4f9a-b0bd-efb4ee0757f1"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[1, 2, 3, 4, 5]\n",
            "2\n",
            "5\n",
            "<class 'list'>\n",
            "5\n",
            "9\n",
            "1\n",
            "7\n",
            "[2, 4, 6, 8]\n",
            "[2, 4, 9, 8]\n",
            "[11, 22, 33, 44, 55]\n",
            "[11, 22, 33, 44, 55]\n",
            "[99, 22, 33, 44, 55, 66, 'alo']\n",
            "[99, 22, 33, 44, 55, 66, 'alo']\n"
          ]
        }
      ],
      "source": [
        "lista1 = [1,2,3,4,5]\n",
        "\n",
        "#chamando a lista1\n",
        "print(lista1)\n",
        "\n",
        "#pegando o segundo elemento da lista\n",
        "print(lista1[1])\n",
        "\n",
        "#pegando o quinto elemento da lista\n",
        "print(lista1[4])\n",
        "\n",
        "#saber o tipo de objeto python\n",
        "print(type(lista1))\n",
        "\n",
        "#erro de indexação posição inexistente na lista\n",
        "#print(lista1[5])\n",
        "\n",
        "\n",
        "#trabalhando com a lista2\n",
        "lista2 = [1,3,5,7,9]\n",
        "print(lista2[2])\n",
        "#usando um index negtivo\n",
        "print(lista2[-1])\n",
        "#pegando o valor da primeira posição da lista\n",
        "print(lista2[0])\n",
        "\n",
        "#pegando um valor negativo\n",
        "print(lista2[-2])\n",
        "\n",
        "#tabalhando com a lista3, em que se mostra que os valores dentro de uma poisção ou index podem ser trocados\n",
        "lista3 = [2,4,6,8]\n",
        "print(lista3)\n",
        "lista3[2]=9\n",
        "print(lista3)\n",
        "\n",
        "\n",
        "# trabalhando com a lista4 & lista5, copias com lista cópia espelhada\n",
        "lista4 = [11,22,33,44,55]\n",
        "print(lista4)\n",
        "#lista5 vai receber lista4 e vai refencia a mesma memoria tb\n",
        "lista5 = lista4\n",
        "print(lista5)\n",
        "lista4.append(66)\n",
        "lista4[0] = 99\n",
        "lista5.append('alo')\n",
        "print(lista4)\n",
        "print(lista5)\n",
        "\n",
        "# trabalhando com a lista6 & lista7 , cópia independente\n",
        "\n"
      ]
    }
  ]
}