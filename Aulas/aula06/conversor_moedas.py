def converter_moeda(quantia, taxa_cambio):
    return quantia * taxa_cambio

# Solicita ao usuário que digite a quantia e a taxa de câmbio
quantia = float(input("Digite a quantia a ser convertida: "))
taxa_cambio = float(input("Digite a taxa de câmbio: "))

quantia_convertida = converter_moeda(quantia, taxa_cambio)
print(f"A quantia convertida é: {quantia_convertida}")