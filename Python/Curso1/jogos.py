#Programador Igor Oliveira
#Data 26/09/23
#Jogos Menu


#Biblioteca
import forca
import adivinhação
#----------------------------------------

def escolheJogo():
    #Inicializando Variaveis
    cabec = "="*80

    #----------------------------------------


    #Cabeçalho
    print(cabec)
    print("Bem vindo ao IgorGamer`s House!")
    print(cabec)
    #----------------------------------------

    #Aplicação
    print("Nossos Jogos")
    print("Número Secreto(1) Jogo da Forca(2)")

    jogoEscolhido = int(input("Digite qual jogo deseja jogar: "))

    if jogoEscolhido == 1:
        print("Número Secreto")
        adivinhação.jogar()
    elif jogoEscolhido == 2:
        print("Jogo da Forca")
        forca.jogar()
if __name__ == "__main__":
    escolheJogo()


#----------------------------------------
