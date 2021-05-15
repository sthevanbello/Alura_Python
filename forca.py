def jogar():

    print("*********************************")
    print("***Bem vindo ao jogo de Forca!***")
    print("*********************************\n")

    palavra_secreta = "banana"
    enforcou = False
    acertou = False
    lista = []
    
    while (not enforcou and not acertou):
        chute = input("Digite uma letra: ").lower().strip()
        
        index = 0
        
        for letra in palavra_secreta:
            if (chute == letra):
                print(f"Acertou a letra {chute} na posição {index+1}")
                lista.insert(index, letra)
            index += 1
        print(lista)    
            
    print("End of game!")


if __name__ == "__main__":
    jogar()
