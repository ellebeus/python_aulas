def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_para_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def celsius_para_kelvin(celsius):
    return celsius + 273.15

def kelvin_para_celsius(kelvin):
    return kelvin - 273.15

def fahrenheit_para_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_para_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

# Solicitar valores do usuário
print("Escolha a conversão desejada:")
print("1: Celsius para Fahrenheit")
print("2: Fahrenheit para Celsius")
print("3: Celsius para Kelvin")
print("4: Kelvin para Celsius")
print("5: Fahrenheit para Kelvin")
print("6: Kelvin para Fahrenheit")

opcao = int(input("Digite o número da conversão desejada: "))
valor = float(input("Digite o valor da temperatura: "))

if opcao == 1:
    print(f"{valor}°C é igual a {celsius_para_fahrenheit(valor)}°F")
elif opcao == 2:
    print(f"{valor}°F é igual a {fahrenheit_para_celsius(valor)}°C")
elif opcao == 3:
    print(f"{valor}°C é igual a {celsius_para_kelvin(valor)}K")
elif opcao == 4:
    print(f"{valor}K é igual a {kelvin_para_celsius(valor)}°C")
elif opcao == 5:
    print(f"{valor}°F é igual a {fahrenheit_para_kelvin(valor)}K")
elif opcao == 6:
    print(f"{valor}K é igual a {kelvin_para_fahrenheit(valor)}°F")
else:
    print("Opção inválida")

