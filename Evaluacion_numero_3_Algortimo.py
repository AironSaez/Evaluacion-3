{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyM3bVOilacmuiF23LPsQdLx",
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
        "<a href=\"https://colab.research.google.com/github/AironSaez/Evaluacion-3/blob/main/Evaluacion_numero_3_Algortimo.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "id": "gvFIByAhjCPA"
      },
      "outputs": [],
      "source": [
        "\n",
        "def registrar(rut,nombre,edad,pais,ciudad):\n",
        "  return(rut,nombre,edad,pais,ciudad)\n",
        "\n",
        "def mostrar_menu():\n",
        "  print(\"-----Menu-----\")\n",
        "  print(\"1. Registrar usuario \")\n",
        "  print(\"2. buscar usuario \")\n",
        "  print(\"3. imprimir documentos \")\n",
        "  print(\"4. eliminar usuario \")\n",
        "  print(\"5. salir \")\n",
        "\n",
        "info_persona = []\n",
        "\n",
        "while True:\n",
        "  mostrar_menu()\n",
        "  opcion=int(input(\"ingrese una persona: \"))\n",
        "\n",
        "  match opcion:\n",
        "    case 1:\n",
        "      print(\"1. registrar usuario\")\n",
        "      registrar()\n",
        "      info_persona.append()\n",
        "    case 2:\n",
        "\n",
        "    case 3:\n",
        "\n",
        "    case 4:\n",
        "\n",
        "\n",
        "\n",
        "\n",
        "\n",
        "\n"
      ]
    }
  ]
}
