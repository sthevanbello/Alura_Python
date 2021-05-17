import random

def jogar():
    
    mensagem_inicio()
    
    palavra_secreta = carrega_palavra_secreta()
    
    lista = inicializa_letras_acertadas(palavra_secreta)
    
    print(lista)

    testa_chute(palavra_secreta=palavra_secreta,lista=lista)

    print("End of game!")

def mensagem_inicio():
    print("*********************************")
    print("***Bem vindo ao jogo de Forca!***")
    print("*********************************\n")


    
def carrega_palavra_secreta():
    lista_palavras = []
    with open("palavras.txt") as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            lista_palavras.append(linha)
        numero = random.randrange(0, len(lista_palavras))

    palavra_secreta = lista_palavras[numero].lower()
    
    return palavra_secreta
    # arquivo = open("palavras.txt", "r")
    # lista_palavras = []
    # for linha in arquivo:
    #     linha = linha.strip()
    #     lista_palavras.append(linha)
    # arquivo.close()
def pede_chute():
    return input("Digite uma letra: ").lower().strip()
    
def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra]

def testa_chute(palavra_secreta, lista):
    enforcou = False
    acertou = False
    tentativas = 7
    erros = 0
    while not enforcou and not acertou:
        chute = pede_chute()
        index = 0
        if not (chute in palavra_secreta):
            erros += 1
            desenha_forca(erros)
            enforcou = marca_erro(tentativas, erros)
        for letra in palavra_secreta:
            if chute == letra:
                # print(f"Acertou a letra {chute} na posição {index+1}")
                lista[index] = letra
            index += 1
        print(lista)
        if lista.count("_") == 0:
            acertou = True

def marca_erro(tentativas, erros):
    print(f"Tentativa {erros}/{tentativas}")
    if erros == tentativas:
        return True

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

if __name__ == "__main__":
    jogar()
