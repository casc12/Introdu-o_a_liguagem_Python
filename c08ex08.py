{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOX4O5xtMUprIrLoSZa3XLV",
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
        "<a href=\"https://colab.research.google.com/github/casc12/Introdu-o_a_liguagem_Python/blob/Cap08/c08ex08.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 3,
      "metadata": {
        "id": "u3HO42xrDssk",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "2b75cac1-eaa0-4e23-c05a-6407c7e9b5a2"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Quantas linhas ...:2\n",
            "Quantas colunas ..:2\n",
            "\n",
            "\n",
            "Linha  1 ...: \n",
            "\n",
            "Coluna  1 ..: 3\n",
            "Coluna  2 ..: 2\n",
            "\n",
            "Linha  2 ...: \n",
            "\n",
            "Coluna  1 ..: 1\n",
            "Coluna  2 ..: 2\n",
            "\n",
            "\n",
            "Linha  1 ...:\n",
            "\n",
            "Coluna  1 ..:    3 \n",
            "Coluna  2 ..:    2 \n",
            "\n",
            "Linha  2 ...:\n",
            "\n",
            "Coluna  1 ..:    1 \n",
            "Coluna  2 ..:    2 \n",
            "\n",
            "\n",
            "Pressione <Enter> para encerrar... \n"
          ]
        }
      ],
      "source": [
        "notas = []\n",
        "\n",
        "lin = int(input(\"Quantas linhas ...:\"))\n",
        "col = int(input(\"Quantas colunas ..:\"))\n",
        "\n",
        "\n",
        "for i in range(lin):\n",
        "    notas.append([])\n",
        "    for j in range(col):\n",
        "        notas[i].append(0)\n",
        "\n",
        "print()\n",
        "\n",
        "for i in range(lin):\n",
        "    print(\"\\nLinha {0:2} ...: \\n\".format(i+1))\n",
        "    for j in range(col):\n",
        "        notas[i][j] = int(input(\"Coluna {0:2} ..: \".format(j+1)))\n",
        "print()\n",
        "for i in range(lin):\n",
        "    print(\"\\nLinha {0:2} ...:\\n\".format(i+1))\n",
        "    for j in range(col):\n",
        "        print(\"Coluna {0:2} ..: {1:4} \".format(j+1,notas[i][j]))\n",
        "\n",
        "print()\n",
        "enter = input(\"\\nPressione <Enter> para encerrar... \")\n",
        "\n"
      ]
    }
  ]
}