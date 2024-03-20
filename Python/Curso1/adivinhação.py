#Programador Igor Oliveira
#Data 20/09/23
#Jogo da Adivinhação




#Biblioteca
import random
#----------------------------------------


def jogar():


    #Inicializando Variaveis
    cabec = "="*80
    numero_secreto = random.randrange(1,101)
    totalTentativas = 0
    rodada = 1
    pontos = 1000
    #----------------------------------------


    #Cabeçalho
    print(cabec)
    print("Bem vindo ao jogo de Adivinhação!")
    print(cabec)
    #----------------------------------------




    #Aplicação
    print("Qual a dificuldade que deseja: Fácil(1) Médio(2) Díficil(3)")

    nivel = int(input("Digite a Dificuldade: "))
    print(numero_secreto)

    if nivel == 1:
        totalTentativas = 10
    elif nivel == 2:
        totalTentativas = 7
    else:
        totalTentativas = 5
    while(rodada <= totalTentativas):
        print("Total ", rodada, "de ", totalTentativas)
        chute_str = input("Digite um número entre 1 e 100: ")
        print("Você digitou " , chute_str)
        chute = int(chute_str)

        if chute < 1 or chute > 100:
            print("Você deve digitar um número entre 1 e 100:")
            continue


        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

    
        if(acertou):
            print(f"Parabéns! Você acertou! E fez", pontos, "pontos.")
            break
        else:
            if(maior):
                print("O seu chute foi maior do que o número secreto!")
            elif(menor):
                print("O seu chute foi menor do que o número secreto!")
        rodada = rodada + 1
        pontos_perdidos = abs(numero_secreto - chute)
        pontos = pontos - pontos_perdidos
    print("Fim do jogo")
if __name__ == "__main__":
    jogar()
    #----------------------------------------