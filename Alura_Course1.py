print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = 42
tentativa = 5
restante = tentativa
for rodada in range(1,tentativa+1):
    
    chute = int(input("Digite o seu número: "))
    restante -= 1
    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto
    if (chute < 1 or chute > 100):
        print("Você deve digitar um número entre 1 e 100!")
        continue
    if (acertou):
        print(f"Acertou em {rodada} tentativas")
        break
    else:
        if (maior):
            print("Você errou! O seu chute foi maior que o número secreto.")
        elif (menor):
            print("Você errou! O seu chute foi menor que o número secreto.")
    print(f"Total de tentativas restantes: {restante}")
print("End of game!")
