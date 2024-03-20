#Programador Igor Oliveira
#Data 26/09/23
#Jogo da Forca




#Biblioteca---------------------------------
import random
#-------------------------------------------




def jogar():

    cabecalho()
    palavraSecreta = carregaPalavraSecreta()
    letrasAcertadas = incializaLetrasAcertadas(palavraSecreta)
    print(letrasAcertadas)
    
    
    enforcou = False
    acertou = False
    erros = 0

  
    while(not enforcou and not acertou):
        chute = pedeChute()
        if chute in palavraSecreta:
            marcaChuteCorreto(chute, letrasAcertadas, palavraSecreta)
        else:
            erros = erros + 1
            desenha_forca(erros)
        enforcou = erros == 7
        acertou = "-" not in letrasAcertadas
        print(letrasAcertadas)
    if acertou:
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor()
    print("Fim do Jogo.")


def cabecalho():
    cabec = "="*80
    print(cabec)
    print("Bem vindo ao Jogo da Forca")
    print(cabec)

def carregaPalavraSecreta():
    arquivo = open("palavras.txt", "r",  encoding="utf-8")
    palavras = []

    for linha in arquivo:
        linha.strip()
        palavras.append(linha)
    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavraSecreta = palavras[numero].upper().strip()
    return palavraSecreta
    
def incializaLetrasAcertadas(palavra):
    return ["-" for letra in palavra]

def pedeChute():
    chute = input("Qual letra: ")
    chute = chute.strip().upper()
    return chute

def marcaChuteCorreto(chute, letrasAcertadas, palavraSecreta):
    index = 0
    for letra in palavraSecreta:
        if (chute == letra):
            letrasAcertadas[index] = letra
        index = index + 1


def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


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
