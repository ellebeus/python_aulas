import random

def jogo_adivinhacao():
    numero_secreto = random.randint(1, 100)
    tentativas = 0
    acertou = False

    print("Bem-vindo ao jogo de adivinhação!")
    print("Tente adivinhar o número entre 1 e 100.")

    while not acertou:
        palpite = int(input("Digite seu palpite: "))
        tentativas += 1

        if palpite == numero_secreto:
            acertou = True
            print(f"Parabéns! Você adivinhou o número em {tentativas} tentativas.")
        elif palpite < numero_secreto:
            print("O número é maior. Tente novamente.")
        else:
            print("O número é menor. Tente novamente.")

# Inicia o jogo
jogo_adivinhacao()