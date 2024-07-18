{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMcJE21q/bBAWtMWak+qYKl",
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
        "<a href=\"https://colab.research.google.com/github/casc12/Introdu-o_a_liguagem_Python/blob/Cap08/c08ex07.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "u3HO42xrDssk",
        "outputId": "ad4eb9df-6863-4563-c590-cc4de368f555"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Quantos elementos a entrar: 2\n",
            "\n",
            "Digite com  1º valor: 1\n",
            "Digite com  2º valor: 2\n",
            "\n",
            "A[ 1] =    1 na posição  0\n",
            "A[ 2] =    2 na posição  1\n",
            "\n",
            "Pressione <ENTER> para encerrar ...\n"
          ]
        }
      ],
      "source": [
        "a = []\n",
        "#entrada de dados\n",
        "quantidade = int(input(\"Quantos elementos a entrar: \"))\n",
        "\n",
        "print()\n",
        "for i in range(quantidade):\n",
        "  valor = int(input(\"Digite com {0:2}º valor: \" .format(i+1)))\n",
        "  a.append(valor)\n",
        "\n",
        "\n",
        "#Apresentação de listas\n",
        "print()\n",
        "\n",
        "for i in range(len(a)):\n",
        "  print(\"A[{0:2}] = {1:4} na posição {2:2}\" .format(i+1 , a[i], i))\n",
        "\n",
        "\n",
        "enter = input(\"\\nPressione <ENTER> para encerrar ...\")"
      ]
    }
  ]
}