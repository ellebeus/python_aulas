import math
def calcular():

    angulo = float(input("Digite o ângulo em graus: "))
    angulo_radiano = math.radians(angulo)
    seno_valor = math.sin(angulo_radiano)
    cos_valor = math.cos(angulo_radiano)
    tang_valor = math.tan(angulo_radiano)

    print(f"O valor de seno é: {seno_valor}")
    print(f"O valor de cosseno é: {cos_valor}")
    print(f"O valor da tangende é: {tang_valor}")

calcular()