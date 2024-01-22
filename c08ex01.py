{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyN2BnT618XAP7Kh/r+eiTCa",
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
        "<a href=\"https://colab.research.google.com/github/casc12/Introdu-o_a_liguagem_Python/blob/Cap08/c08ex01.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 7,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "OzbcvnoOclg6",
        "outputId": "19bbe10e-fb03-4615-ae13-8226e7b339e8"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Exemplo de checagem de índice\n",
            " \n",
            "Entre como  1º valor: 0\n",
            "0\n",
            "Entre como  2º valor: 1\n",
            "1\n",
            "Entre como  3º valor: 2\n",
            "2\n",
            "Entre como  4º valor: 3\n",
            "3\n",
            "Entre como  5º valor: 4\n",
            "4\n",
            "Entre como  6º valor: 5\n",
            "5\n",
            "Entre como  7º valor: 6\n",
            "6\n",
            "Entre como  8º valor: 7\n",
            "7\n",
            "Entre como  9º valor: 8\n",
            "8\n",
            "Entre como 10º valor: 9\n",
            "9\n",
            "\n",
            "\n",
            "A[ 1] =    0 na posição  0.\n",
            "A[ 2] =    1 na posição  1.\n",
            "A[ 3] =    2 na posição  2.\n",
            "A[ 4] =    3 na posição  3.\n",
            "A[ 5] =    4 na posição  4.\n",
            "A[ 6] =    5 na posição  5.\n",
            "A[ 7] =    6 na posição  6.\n",
            "A[ 8] =    7 na posição  7.\n",
            "A[ 9] =    8 na posição  8.\n",
            "A[10] =    9 na posição  9.\n",
            "\n",
            "B[ 1] =    0 na  posição  0\n",
            "B[ 2] =    6 na  posição  1\n",
            "B[ 3] =   10 na  posição  2\n",
            "B[ 4] =    8 na  posição  3\n",
            "B[ 5] =   20 na  posição  4\n",
            "B[ 6] =   10 na  posição  5\n",
            "B[ 7] =   30 na  posição  6\n",
            "B[ 8] =   12 na  posição  7\n",
            "B[ 9] =   40 na  posição  8\n",
            "B[10] =   14 na  posição  9\n",
            "\n",
            "Pressione <Enter> para encerrar ...\n"
          ]
        }
      ],
      "source": [
        "a = []\n",
        "b = []\n",
        "\n",
        "\n",
        "print(\"Exemplo de checagem de índice\\n \")\n",
        "\n",
        "#Entrada de dados\n",
        "\n",
        "for i in range(10):\n",
        "  valor = int(input(\"Entre como {0:2}º valor: \".format(i+1)))\n",
        "  a.append(valor)\n",
        "  print(a[i])\n",
        "\n",
        "#Processamento par ou impar\n",
        "\n",
        "print()\n",
        "for i in range(10):\n",
        "  if( i % 2 == 0):\n",
        "    b.append(a[i] * 5)\n",
        "  else:\n",
        "    b.append(a[i] + 5)\n",
        "\n",
        "\n",
        "#Apresentações da listas\n",
        "print()\n",
        "for i in range(10):\n",
        "  print(\"A[{0:2}] = {1:4} na posição {2:2}.\".format(i + 1, a[i], i ))\n",
        "\n",
        "print()\n",
        "for i in range(10):\n",
        "  print(\"B[{0:2}] = {1:4} na  posição {2:2}\".format(i + 1, b[i], i))\n",
        "\n",
        "enter = input(\"\\nPressione <Enter> para encerrar ...\")"
      ]
    }
  ]
}