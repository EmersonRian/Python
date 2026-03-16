import os


palavra_jogo_da_forca = "Hipopotamo"
erros = 0
acertos = 0
letras_tentadas = []


def falhas(erro):
    if erro == 0:
        print("Joguinho da Forca\n"
                "______    \n"
                "|    |    \n"
                "|         \n"
                "|         \n"
                "|         \n"
                "          ")
    if erro == 1:
        print("Joguinho da Forca\n"
            "______    \n"
            "|    |    \n"
            "|    O    \n"
            "|         \n"
            "|         \n"
            "")
        
    if erro == 2:
        print("Joguinho da Forca\n"
            "______    \n"
            "|    |    \n"
            "|    O    \n"
            "|    |    \n"
            "|         \n"
            "")

    if erro == 3:
        print("Joguinho da Forca\n"
            "______    \n"
            "|    |    \n"
            "|    O    \n"
            "|   /|    \n"
            "|         \n"
            "")

    if erro == 4:
        print("Joguinho da Forca\n"
            "______    \n"
            "|    |    \n"
            "|    O    \n"
            "|   /|\\  \n"
            "|         \n"
            "")

    if erro == 5:
        print("Joguinho da Forca\n"
            "______    \n"
            "|    |    \n"
            "|    O    \n"
            "|   /|\\  \n"
            "|   /     \n"
            "")

    if erro == 6:
        print("Joguinho da Forca\n"
            "______    \n"
            "|    |    \n"
            "|    O    \n"
            "|   /|\\  \n"
            "|   / \\  \n"
            "")

def jogo(tentativa,erro):

    falhas(erro)

    for letra in palavra_jogo_da_forca:
        if letra in tentativa:
            print(letra,end=" ")
        if letra not in tentativa:
            print("_", end=" ")
    if tentativas not in palavra_jogo_da_forca:
        print("Errou")
    if tentativas in palavra_jogo_da_forca:
         print(" Acertou")


    

def letras(letras):
    if letras in letras_tentadas:
        print()
        print("Essa letra ja foi ultilizada")
        print()
        letras_tentadas.remove(letras)
    letras_tentadas.append(tentativas)




    
def comecar():

    print("Bom dia,Boa tarde,Boa noite vamos começar um joguinho de forca?\n" "(1)Sim (2)Não")
    questao1 = input()

    if questao1 == "2":
        print("tudo bem entao. Irei finalizar aqui.")

    if questao1 == "1":
        print("Vamos começar então.")
        falhas(erros)

        for letra in palavra_jogo_da_forca:
            print("_", end=" ")
            letra





    



while True:
    if len(letras_tentadas) == 0:
        comecar()

    print()
    print()
    

    tentativas = input()
    os.system("cls")


    letras(tentativas)

    jogo(letras_tentadas,erros)


    if erros == 6:
        print("Infelizmente Tu Perdeu pivete")
        break
    if acertos == len(palavra_jogo_da_forca):
        print("PARABENS VC ACERTOU TUDO")
        break



    print()
    print("_tabela de letras tentadas_")
    for iten in letras_tentadas:
        print(iten,end="-")

    


