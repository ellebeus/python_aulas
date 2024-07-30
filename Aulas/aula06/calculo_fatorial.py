import math

def calcular_fatorial(numero):
    return math.factorial(numero)

numero = int(input("Digite um valor para calcular o fatorial: "))
print(f"O fatorial de {numero} é {calcular_fatorial(numero)}")