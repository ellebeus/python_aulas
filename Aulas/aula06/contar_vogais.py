from collections import Counter

def contar_vogais(texto):
    vogais = "aeiouAEIOU"
    contador = Counter(char for char in texto if char in vogais)
    return sum(contador.values())

# Exemplo de uso
texto = input("Digite uma string: ")
print(f"O número de vogais em '{texto}' é {contar_vogais(texto)}")