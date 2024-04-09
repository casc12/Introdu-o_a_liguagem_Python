{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyP94iUmsRt7P2VfXVFqziyj",
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
        "<a href=\"https://colab.research.google.com/github/casc12/Introdu-o_a_liguagem_Python/blob/Cap08/c08ex02.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "a = []\n",
        "s = 0\n",
        "\n",
        "print(\"Exemplo de checagem de elemento\\n\")\n",
        "\n",
        "#Entrada de Dados\n",
        "\n",
        "for i in range(5):\n",
        "  a.append(int(input(\"Entre o {0:2}o. valor: \".format(i+1))))\n",
        "\n",
        "\n",
        "#Processamento par ou impar\n",
        "for i in range(len(a)):\n",
        "  #somatorio do restos que serão par o livro informa que é impar e está errado\n",
        "  if(a[i] % 2 == 0):\n",
        "    s += a[i]\n",
        "\n",
        "\n",
        "# Apresentações das listas\n",
        "print()\n",
        "print(\"Soma dos elementos pares = {0}\".format(s))\n",
        "\n",
        "\n",
        "enter = input(\"\\nPressione <Enter> para encerrar...\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "39mRZIyqYVC_",
        "outputId": "17a9d8b0-0e52-4bdb-c4c1-a60743010d2d"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Exemplo de checagem de elemento\n",
            "\n",
            "Entre o  1o. valor: 1\n",
            "Entre o  2o. valor: 2\n",
            "Entre o  3o. valor: 3\n",
            "Entre o  4o. valor: 4\n",
            "Entre o  5o. valor: 5\n",
            "\n",
            "Soma dos elementos pares = 6\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "8Vosg56GSBnu"
      },
      "outputs": [],
      "source": []
    }
  ]
}