import forca
import adivinhacao

print("*********************************")
print("*******Escolha o seu jogo!*******")
print("*********************************")

print("(1) Forca (2) Adivinhação")

escolha = int(input("Qual jogo? "))

if (escolha == 1):
    print("\nJogando forca\n")
    forca.jogar()
elif (escolha == 2):
    print("\nJogando o jogo da Adivinhação\n")
    adivinhacao.jogar()
else:
    print("Jogo não encontrado!")    


