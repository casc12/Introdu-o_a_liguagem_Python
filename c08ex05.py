{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPPHsQ7scTPyVAsJo92gFCr",
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
        "<a href=\"https://colab.research.google.com/github/casc12/Introdu-o_a_liguagem_Python/blob/Cap08/c08ex05.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "L1j7V9cR-P0L",
        "outputId": "b4af569f-bf4a-40ce-d21e-7a15226672a8"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Média da sala:   5.98\n"
          ]
        }
      ],
      "source": [
        "notas = [[2.5, 5.5, 7.0, 8.0],\n",
        "         [3.7, 6.5, 6.0, 2.0],\n",
        "         [7.5, 7.5, 7.0, 9.0],\n",
        "         [1.5, 2.5, 5.3, 1.2],\n",
        "         [4.5, 5.5, 6.8, 5.5],\n",
        "         [6.5, 9.5, 7.5, 8.5],\n",
        "         [8.5, 7.5, 7.2, 3.9],\n",
        "         [8.5, 2.5, 7.8, 8.4],\n",
        "         ]\n",
        "soma = 0\n",
        "\n",
        "for i in range(8):\n",
        "  for j in range(4):\n",
        "    soma += notas[i][j]\n",
        "  media = soma/32\n",
        "\n",
        "#´\n",
        "print(\"Média da sala: {0:6.2f}\" .format(media))\n",
        "enter = input(\"\\nPressione <Enter> para encerrar...\")"
      ]
    }
  ]
}