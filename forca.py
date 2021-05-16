import random


def jogar():
    
    mensagem_inicio()
    palavra_secreta = carrega_palavra_secreta()
    

    enforcou = False
    acertou = False
    tentativas = 5
    erros = 0

    lista = inicializa_letras_acertadas()

    # for letra in palavra_secreta:
    #     lista.append("_")

    print(lista)

    while not enforcou and not acertou:
        chute = input("Digite uma letra: ").lower().strip()

        index = 0

        if not (chute in palavra_secreta):
            erros += 1
            print(f"Tentativa {erros}/{tentativas}")
            if erros == tentativas:
                enforcou = True

        for letra in palavra_secreta:
            if chute == letra:
                print(f"Acertou a letra {chute} na posição {index+1}")
                lista[index] = letra
            index += 1
        print(lista)

        if lista.count("_") == 0:
            acertou = True
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
    
def inicializa_letras_acertadas():
    ["_" for letra in carrega_palavra_secreta()]
    
if __name__ == "__main__":
    jogar()
