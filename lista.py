{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyP45iKuuhehWFkDsb/AJ0q7",
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
      "execution_count": 16,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Cbh9h9bc5Dln",
        "outputId": "012b9c01-3400-46f1-e55c-e4f7995a368a"
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
            "[2, 4, 9, 8]\n"
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
        "\n"
      ]
    }
  ]
}