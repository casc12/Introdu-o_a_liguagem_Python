{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPjSL90B/bMjdPh/l8mqmQQ",
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
      "execution_count": 18,
      "metadata": {
        "id": "u3HO42xrDssk",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "ad681e9c-ee3d-4d99-a2a1-2659d72afbde"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "carlos\n",
            "34\n",
            "superior\n",
            "<class 'dict'>\n",
            "{'nome': 'carlos', 'idade': 34, 'escolaridade': 'superior'}\n",
            "{'nome': 'carlos', 'idade': 25, 'escolaridade': 'superior'}\n",
            "carlos\n",
            "None\n"
          ]
        }
      ],
      "source": [
        "dicionario1 = {\"nome\":\"carlos\", \"idade\":34, \"escolaridade\":\"superior\"}\n",
        "print(dicionario1[\"nome\"])\n",
        "print(dicionario1[\"idade\"])\n",
        "print(dicionario1[\"escolaridade\"])\n",
        "print(type(dicionario1))\n",
        "print(dicionario1)\n",
        "dicionario1[\"idade\"]= 25\n",
        "print(dicionario1)\n",
        "#print(dicionario1[\"altura\"])\n",
        "print(dicionario1.get(\"nome\"))\n",
        "print(dicionario1.get(\"altura\"))"
      ]
    }
  ]
}