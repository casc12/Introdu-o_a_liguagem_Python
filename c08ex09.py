{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyM4x5OZ0k+lsX7ms3iFmHAS",
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
        "<a href=\"https://colab.research.google.com/github/casc12/Introdu-o_a_liguagem_Python/blob/Cap08/c08ex09.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 5,
      "metadata": {
        "id": "u3HO42xrDssk",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "d5bf68d2-0959-4edc-b161-a87c1f545d17"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Entre com o nome  1° aluno: carlos \n",
            "Entre com o nome  2° aluno: joã\n",
            "Entre com o nome  3° aluno: cida\n",
            "Entre com o nome  4° aluno: edmilson\n",
            "Entre com o nome  5° aluno: alessandra\n",
            "Entre com o nome  6° aluno: leila\n",
            "Entre com o nome  7° aluno: emila\n",
            "Entre com o nome  8° aluno: adalto\n",
            "\n",
            "Aluno 1 ...: carlos  \n",
            "Aluno 2 ...: joã \n",
            "Aluno 3 ...: cida \n",
            "Aluno 4 ...: edmilson \n",
            "Aluno 5 ...: alessandra \n",
            "Aluno 6 ...: leila \n",
            "Aluno 7 ...: emila \n",
            "Aluno 8 ...: adalto \n",
            "\n",
            "Pressione <Enter> para encerrar\n"
          ]
        }
      ],
      "source": [
        "escolar = {}\n",
        "\n",
        "#Entrada de dados\n",
        "for i in range(8):\n",
        "  nome = input(\"Entre com o nome {0:2}° aluno: \".format(i+1))\n",
        "  escolar[i] = nome\n",
        "\n",
        "#Apresentação das listas\n",
        "print()\n",
        "for i in range(8):\n",
        "  print(\"Aluno {0} ...: {1} \".format(i+1, escolar[i]))\n",
        "\n",
        "enter = input(\"\\nPressione <Enter> para encerrar\")"
      ]
    }
  ]
}