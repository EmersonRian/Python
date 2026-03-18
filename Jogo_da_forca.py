import os
import random

palavras_aleatorias = ["Cogumelo","Hipopotamo","Passageiro","Pokemon","Jornada","açogueiro"]
palavra_escolhida = random.choice(palavras_aleatorias).lower()

erros = 0
acertos = 0
letras_tentadas = []


    



while True:

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
        


    print()
    falhas(erros)


    for letra in palavra_escolhida:
        if letra in letras_tentadas:
            print(letra.upper(), end=" ")
        
        if letra not in letras_tentadas:
            print("_", end=" ")

    print()
    print()
    print("_Tabela_de_letras_Usadas_")
    for iten in letras_tentadas:
        print(iten,end="-")
    print()

    if erros == 6:
        print("infelizmente vc nao conseguiu. Sorte na proxima")
        break
    if acertos == len(list(set(palavra_escolhida))):
        print("Parabens vc Ganhou!!!!! <3")
        break

    print()
    pergunta = input().lower()
    os.system("cls")


    if pergunta in letras_tentadas:
        print("Essa letra ja foi tentada")
        continue

    if pergunta.isdigit():
        print("Não coloque numeros")
        continue

    if pergunta in list(set(palavra_escolhida)):
        acertos += 1

    if len(pergunta) > 1:
        print("por favor, coloque somente uma letra.")
        continue

    if pergunta not in palavra_escolhida:
        erros += 1
    
    if pergunta not in letras_tentadas:
        letras_tentadas.append(pergunta)





    





    


