import random


print("--------------------")
print("Jogo De Adivinhação ")
print("--------------------")

numero_secreto = random.randrange(1, 101)
Tentativas = 0

print("Qual o nível de dificuldade?")
print("(1) Fácil (2) Médio (3) Difícil")

nivel = int(input("Defina o nível: "))

if (nivel == 1):
    Tentativas = 20
elif (nivel == 2):
    Tentativas = 10
else:
    Tentativas = 5



while (Tentativas > 0):
    print("Número de Tentativas: ", Tentativas)
    chute_str = input("Digite seu Número: ")

    print("Você Digitou o Número: ", chute_str)

    chute = int(chute_str)

    Acertou = numero_secreto == chute
    maior = chute > numero_secreto
    menor = chute < numero_secreto


    if (Acertou):
        print("Você acertou ")
        break
    else :
        if(maior):
            print("O Número Secreto é Menor ")
        elif(menor):
            print("O Número Secreto é Maior ")
        print("Você errou ")

    Tentativas = Tentativas - 1



    print("Fim Do Jogo")