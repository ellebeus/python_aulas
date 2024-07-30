strings = ["Olá", "Mundo", "Python", "Copilot"]
comprimentos = [len(s) for s in strings]
for i, s in enumerate(strings):
    print(f"O comprimento da string '{s}' é {comprimentos[i]} caracteres.")