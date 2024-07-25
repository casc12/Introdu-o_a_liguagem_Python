{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyO7K2r+H1SBKyGkpany3k2K",
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
        "<a href=\"https://colab.research.google.com/github/casc12/Introdu-o_a_liguagem_Python/blob/Cap08/dicionario.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 10,
      "metadata": {
        "id": "u3HO42xrDssk",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "34bdf5de-e4c2-485a-bd51-0c4ff8aa6ddc"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "carlos\n",
            "34\n",
            "superior\n",
            "{'nome': 'carlos', 'idade': '34', 'escolaridade': 'superior'}\n"
          ]
        }
      ],
      "source": [
        "dicionario1 = {\"nome\":\"carlos\", \"idade\":\"34\", \"escolaridade\":\"superior\"}\n",
        "print(dicionario1[\"nome\"])\n",
        "print(dicionario1[\"idade\"])\n",
        "print(dicionario1[\"escolaridade\"])\n",
        "print(dicionario1)\n"
      ]
    }
  ]
}