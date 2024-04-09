{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOIn0m2mqZetFajUUOFWHUI",
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
        "<a href=\"https://colab.research.google.com/github/casc12/Introdu-o_a_liguagem_Python/blob/Cap08/c08ex03.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [],
      "metadata": {
        "id": "6v0v1MlQ71uE"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "a = []\n",
        "s = 0\n",
        "\n",
        "print(\"Somatório de valores informados\")\n",
        "\n",
        "#Entrada de Dados\n",
        "i = 0\n",
        "resp = 'S'\n",
        "while(resp.upper() == 'S'):\n",
        "  a.append(float(input(\"\\nEntre o {3.0})o. valor: \".format(i+1))))\n",
        "  s += a[i]\n",
        "  i += 1\n",
        "  print()\n",
        "  print(\"Deseja continuar?\")\n",
        "  resp = input(\"Tecle [S] para sim / qualquer caractere para NAO: \")\n",
        " # Apresentação dos Dados\n",
        "print()\n",
        "for i in range(len(a)):\n",
        "  print(\"A[{0:3}] = {1:8,.2f} na posição {2:3}.\".format(i + 1,a[i],i))\n",
        "\n",
        "print()\n",
        "print(\"Soma dos valores informados= {0:8,.2f}\".format(s))\n",
        "\n",
        "enter = input(\"\\nPressione <Enter> para encerrar... \")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 228
        },
        "id": "zOEJa7xh72Gn",
        "outputId": "cb476f78-203a-462a-c950-f1e646142700"
      },
      "execution_count": 15,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Somatório de valores informados\n"
          ]
        },
        {
          "output_type": "error",
          "ename": "IndexError",
          "evalue": "Replacement index 3 out of range for positional args tuple",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mIndexError\u001b[0m                                Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-15-ea2f65dacb1f>\u001b[0m in \u001b[0;36m<cell line: 9>\u001b[0;34m()\u001b[0m\n\u001b[1;32m      8\u001b[0m \u001b[0mresp\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;34m'S'\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      9\u001b[0m \u001b[0;32mwhile\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mresp\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mupper\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;34m==\u001b[0m \u001b[0;34m'S'\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 10\u001b[0;31m   \u001b[0ma\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mappend\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mfloat\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0minput\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"\\nEntre o {3.0})o. valor: \"\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mformat\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mi\u001b[0m\u001b[0;34m+\u001b[0m\u001b[0;36m1\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     11\u001b[0m   \u001b[0ms\u001b[0m \u001b[0;34m+=\u001b[0m \u001b[0ma\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0mi\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     12\u001b[0m   \u001b[0mi\u001b[0m \u001b[0;34m+=\u001b[0m \u001b[0;36m1\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mIndexError\u001b[0m: Replacement index 3 out of range for positional args tuple"
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