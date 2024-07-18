{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "name": "c08ex06.py",
      "authorship_tag": "ABX9TyNJeAbDlkFtCpRXVcyktaa4",
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
        "<a href=\"https://colab.research.google.com/github/casc12/Introdu-o_a_liguagem_Python/blob/Cap08/c08ex06.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "linhas = 5\n",
        "colunas = 4\n",
        "\n",
        "a = []\n",
        "\n",
        "for linha in range(linhas):\n",
        "  a.append( [])\n",
        "  for coluna in range(colunas):\n",
        "    a[linha].append(int(0))\n",
        "\n",
        "b = []\n",
        "for linha in range(linhas):\n",
        "  b.append([])\n",
        "  for coluna in range(colunas):\n",
        "    b[linha].append(float(0.0))\n",
        "\n",
        "print(\"Entrada de Dados\")\n",
        "\n",
        "for linha in range(linhas):\n",
        "  print(\"\\nLinha ...: {:2} \".format(linha + 1))\n",
        "  for coluna in range(colunas):\n",
        "    a[linha][coluna] = int(input(\"Coluna ...: {0:2} \".format(coluna + 1)))\n",
        "\n",
        "for linha in range(linhas):\n",
        "  for coluna in range(colunas):\n",
        "    b[linha][coluna] = a[linha][coluna] ** (1/3)\n",
        "\n",
        "print()\n",
        "\n",
        "print(\"Saída dos dados\\n\")\n",
        "\n",
        "for linha in range(linhas):\n",
        "  for coluna in range(colunas):\n",
        "    print(\"A[{0},{1}] = {2:4} | B[{0},{1}] = {3:0.8f}\".format(linha + 1, coluna +1, a[linha][coluna], b[linha][coluna]))\n",
        "\n",
        "enter = input(\"\\nPressione <Enter> para encerrar... \")"
      ],
      "metadata": {
        "id": "1qe81z5Fhs0g",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "24b77072-c2a0-45ed-eeea-cf2e107f6921"
      },
      "execution_count": 1,
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Entrada de Dados\n",
            "\n",
            "Linha ...:  1 \n",
            "Coluna ...:  1 1\n",
            "Coluna ...:  2 23\n",
            "Coluna ...:  3 5\n",
            "Coluna ...:  4 7\n",
            "\n",
            "Linha ...:  2 \n",
            "Coluna ...:  1 7\n",
            "Coluna ...:  2 8\n",
            "Coluna ...:  3 9\n",
            "Coluna ...:  4 9\n",
            "\n",
            "Linha ...:  3 \n",
            "Coluna ...:  1 9\n",
            "Coluna ...:  2 9\n",
            "Coluna ...:  3 9\n",
            "Coluna ...:  4 9\n",
            "\n",
            "Linha ...:  4 \n",
            "Coluna ...:  1 9\n",
            "Coluna ...:  2 9\n",
            "Coluna ...:  3 9\n",
            "Coluna ...:  4 9\n",
            "\n",
            "Linha ...:  5 \n",
            "Coluna ...:  1 9\n",
            "Coluna ...:  2 9\n",
            "Coluna ...:  3 9\n",
            "Coluna ...:  4 9\n",
            "\n",
            "Saída dos dados\n",
            "\n",
            "A[1,1] =    1 | B[1,1] = 1.00000000\n",
            "A[1,2] =   23 | B[1,2] = 2.84386698\n",
            "A[1,3] =    5 | B[1,3] = 1.70997595\n",
            "A[1,4] =    7 | B[1,4] = 1.91293118\n",
            "A[2,1] =    7 | B[2,1] = 1.91293118\n",
            "A[2,2] =    8 | B[2,2] = 2.00000000\n",
            "A[2,3] =    9 | B[2,3] = 2.08008382\n",
            "A[2,4] =    9 | B[2,4] = 2.08008382\n",
            "A[3,1] =    9 | B[3,1] = 2.08008382\n",
            "A[3,2] =    9 | B[3,2] = 2.08008382\n",
            "A[3,3] =    9 | B[3,3] = 2.08008382\n",
            "A[3,4] =    9 | B[3,4] = 2.08008382\n",
            "A[4,1] =    9 | B[4,1] = 2.08008382\n",
            "A[4,2] =    9 | B[4,2] = 2.08008382\n",
            "A[4,3] =    9 | B[4,3] = 2.08008382\n",
            "A[4,4] =    9 | B[4,4] = 2.08008382\n",
            "A[5,1] =    9 | B[5,1] = 2.08008382\n",
            "A[5,2] =    9 | B[5,2] = 2.08008382\n",
            "A[5,3] =    9 | B[5,3] = 2.08008382\n",
            "A[5,4] =    9 | B[5,4] = 2.08008382\n",
            "\n",
            "Pressione <Enter> para encerrar... \n"
          ]
        }
      ]
    }
  ]
}