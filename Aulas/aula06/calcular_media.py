def calcular_media(numeros):
    return sum(numeros) / len(numeros)

# Solicita ao usuário que digite os números
numeros = input("Digite uma lista de números separados por espaço: ").split()
numeros = [float(numero) for numero in numeros]

print(f"A média dos números digitados é {calcular_media(numeros)}")