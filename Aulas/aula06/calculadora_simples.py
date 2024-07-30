def adicao(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b != 0:
        return a / b
    else:
        return "Divisão por zero não é permitida"

# Solicitar valores do usuário
a = float(input("Digite o primeiro valor: "))
b = float(input("Digite o segundo valor: "))

# Realizar operações
print(f"Adição: {adicao(a, b)}")
print(f"Subtração: {subtracao(a, b)}")
print(f"Multiplicação: {multiplicacao(a, b)}")
print(f"Divisão: {divisao(a, b)}")


