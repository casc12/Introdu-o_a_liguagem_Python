{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNQdycBYRv1WyiV+kr4t4+R",
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
      "source": [
        " a = []\n",
        " b = []\n",
        " print(\"Exemplo de checagem de índice\\n\")\n",
        "\n",
        " # Entrada de dados\n",
        " for i in range(10):\n",
        "  valor = int(input(\"Entre o {0:2}o. valor: \".format(i+1)))\n",
        "  a.append(valor)\n",
        "\n",
        "\n",
        " # processamento par ou ímpar\n",
        "print()\n",
        "for i in range(10):\n",
        "  if(i % 2 ==0):\n",
        "    b.append(a[i] * 5)\n",
        "  else:\n",
        "    b.append(a[i] + 5)\n",
        "\n",
        "# Apresentação das lista\n",
        "\n",
        "print()\n",
        "for i in range(10):\n",
        "  print(\"A[{0:2}] = {1:4} na posição {2:2}.\".format(i+1,a[i], i))\n",
        "\n",
        "print()\n",
        "for i in range(10):\n",
        "  print(\"B[{0:2}] = {1:4} na posição {2:2}\".format(i+1, b[i], i))\n",
        "enter"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 783
        },
        "id": "mEXYFuQzV1M3",
        "outputId": "dbf46065-6ab8-4036-d622-8f4566cdba0b"
      },
      "execution_count": 2,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Exemplo de checagem de índice\n",
            "\n",
            "Entre o  1o. valor: 1\n",
            "Entre o  2o. valor: 2\n",
            "Entre o  3o. valor: 3\n",
            "Entre o  4o. valor: 4\n",
            "Entre o  5o. valor: 5\n",
            "Entre o  6o. valor: 6\n",
            "Entre o  7o. valor: 7\n",
            "Entre o  8o. valor: 8\n",
            "Entre o  9o. valor: 9\n",
            "Entre o 10o. valor: 0\n",
            "\n",
            "\n",
            "A[ 1] =    1 na posição  0.\n",
            "A[ 2] =    2 na posição  1.\n",
            "A[ 3] =    3 na posição  2.\n",
            "A[ 4] =    4 na posição  3.\n",
            "A[ 5] =    5 na posição  4.\n",
            "A[ 6] =    6 na posição  5.\n",
            "A[ 7] =    7 na posição  6.\n",
            "A[ 8] =    8 na posição  7.\n",
            "A[ 9] =    9 na posição  8.\n",
            "A[10] =    0 na posição  9.\n",
            "\n",
            "B[ 1] =    5 na posição  0\n",
            "B[ 2] =    7 na posição  1\n",
            "B[ 3] =   15 na posição  2\n",
            "B[ 4] =    9 na posição  3\n",
            "B[ 5] =   25 na posição  4\n",
            "B[ 6] =   11 na posição  5\n",
            "B[ 7] =   35 na posição  6\n",
            "B[ 8] =   13 na posição  7\n",
            "B[ 9] =   45 na posição  8\n",
            "B[10] =    5 na posição  9\n"
          ]
        },
        {
          "output_type": "error",
          "ename": "NameError",
          "evalue": "name 'enter' is not defined",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mNameError\u001b[0m                                 Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-2-3453c5736bad>\u001b[0m in \u001b[0;36m<cell line: 28>\u001b[0;34m()\u001b[0m\n\u001b[1;32m     26\u001b[0m \u001b[0;32mfor\u001b[0m \u001b[0mi\u001b[0m \u001b[0;32min\u001b[0m \u001b[0mrange\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;36m10\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     27\u001b[0m  \u001b[0mprint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"B[{0:2}] = {1:4} na posição {2:2}\"\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mformat\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mi\u001b[0m\u001b[0;34m+\u001b[0m\u001b[0;36m1\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mb\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0mi\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mi\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 28\u001b[0;31m \u001b[0menter\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
            "\u001b[0;31mNameError\u001b[0m: name 'enter' is not defined"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "39mRZIyqYVC_"
      },
      "execution_count": null,
      "outputs": []
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