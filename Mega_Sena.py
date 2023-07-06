import random


def gerar_numeros_mega_sena():
    numeros = []

    while len(numeros) < 6:
        numero = random.randint(1, 60)

        if numero not in numeros:
            numeros.append(numero)

    return sorted(numeros)


resultado = gerar_numeros_mega_sena()
print("Números da Mega-Sena:", resultado)