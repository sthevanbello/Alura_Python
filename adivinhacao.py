def jogar():
    
    import random

    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************\n")

    numero_secreto = random.randrange(1,101)
    tentativa = 0
    pontos = 1000



    print("Qual é o nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    dificuldade = int(input("Defina um nível: "))
    if dificuldade == 1:
        tentativa = 20
    elif (dificuldade == 2):
        tentativa = 10
    elif (dificuldade == 3):
        tentativa = 5



    for rodada in range(1,tentativa+1):
        print(f"Tentativa {rodada} de {tentativa}")
        chute = int(input("Digite o seu número entre 1 e 100!: "))
        tentativa -= 1

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if (chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue
        if (acertou):
            print(f"Acertou em {rodada} tentativas")
            print(f"Sua pontuação foi de {pontos} pontos")
            break
        else:
            if (maior):
                print("Você errou! O seu chute foi maior que o número secreto.")
            elif (menor):
                print("Você errou! O seu chute foi menor que o número secreto.")
            pontos_perdidos = numero_secreto - chute
            pontos = pontos - abs(pontos_perdidos)


        print(f"Total de tentativas restantes: {tentativa}")

    print("\n*********************************")
    print(f"O número secreto era {numero_secreto}")
    print("End of game!")
    
if (__name__ == "__main__"):
    jogar()
        