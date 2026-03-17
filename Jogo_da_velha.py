import os


palavra_escondida = "Hipopotamo".lower()
erros = 0

letras_tentadas = []
palavras_acertadas = []



# def falhas(erro):
#     if erro == 0:
#         print("Joguinho da Forca\n"
#                 "______    \n"
#                 "|    |    \n"
#                 "|         \n"
#                 "|         \n"
#                 "|         \n"
#                 "          ")
#     if erro == 1:
#         print("Joguinho da Forca\n"
#             "______    \n"
#             "|    |    \n"
#             "|    O    \n"
#             "|         \n"
#             "|         \n"
#             "")
        
#     if erro == 2:
#         print("Joguinho da Forca\n"
#             "______    \n"
#             "|    |    \n"
#             "|    O    \n"
#             "|    |    \n"
#             "|         \n"
#             "")

#     if erro == 3:
#         print("Joguinho da Forca\n"
#             "______    \n"
#             "|    |    \n"
#             "|    O    \n"
#             "|   /|    \n"
#             "|         \n"
#             "")

#     if erro == 4:
#         print("Joguinho da Forca\n"
#             "______    \n"
#             "|    |    \n"
#             "|    O    \n"
#             "|   /|\\  \n"
#             "|         \n"
#             "")

#     if erro == 5:
#         print("Joguinho da Forca\n"
#             "______    \n"
#             "|    |    \n"
#             "|    O    \n"
#             "|   /|\\  \n"
#             "|   /     \n"
#             "")

#     if erro == 6:
#         print("Joguinho da Forca\n"
#             "______    \n"
#             "|    |    \n"
#             "|    O    \n"
#             "|   /|\\  \n"
#             "|   / \\  \n"
#             "")


# def comecar():

#     print("Bom dia,Boa tarde,Boa noite vamos começar um joguinho de forca?\n" "(1)Sim (2)Não")
#     questao1 = input()

#     if questao1 == "2":
#         print("tudo bem entao. Irei finalizar aqui.")
#         return 1

#     if questao1 == "1":
#         print("Vamos começar então.")
#         falhas(erros)

#         for letra in palavra_jogo_da_forca:
#             print("_", end=" ")
#             letra


# def jogo(tentativa,erro):

#     falhas(erro)

#     for letra in palavra_jogo_da_forca:
#         if letra == tentativa:
#             print(letra,end=" ")
#         if letra != tentativa:
#             print("_", end=" ")
#     if tentativas not in palavra_jogo_da_forca:
#         print("Errou")
#     if tentativas in palavra_jogo_da_forca:
#         print(" Acertou")


    
# def letras(letras):
#     if letras in letras_tentadas:
#         print()
#         print("Essa letra ja foi ultilizada")
#         print()
#     if letras not in letras_tentadas:
#         letras_tentadas.append(letras)




    





    



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

    falhas(erros)

    for letra in palavra_escondida:
        if letra in letras_tentadas:
            print(letra.upper(), end=" ")
        
        if letra not in letras_tentadas:
            print("_", end=" ")

    if erros == 6:
        print("infelizmente vc nao conseguiu. Sorte na proxima")
        break
    if len(palavras_acertadas) == len(palavra_escondida):
        print("Parabens vc Ganhou!!!!! <3")
        break

    print(len(palavras_acertadas), len(palavra_escondida))
    pergunta = input().lower()
    os.system("cls")


    if pergunta in letras_tentadas:
        print("Essa letra ja foi tentada")
        continue

    if len(pergunta) > 1:
        print("por favor, coloque somente uma letra.")
        continue

    if pergunta not in palavra_escondida:
        erros += 1
    
    if pergunta not in letras_tentadas:
        letras_tentadas.append(pergunta)





    





    


