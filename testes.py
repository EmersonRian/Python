import random
import os


palavras_aleatorias = [
    
    {"name": "aleatorio", "itens": ["Cogumelo","Hipopotamo","Passageiro","Pokemon","Jornada","açogueiro"]},

    {"nome": "animais", "itens": ["aguia","papagaio","leoa","tataruga"]},
                       
    {"nome": "comidas", "itens": ["cogumelo","pipoca","suchi","macarronada"]},

    {"nome": "empregos", "itens": ["Farmaceutico", "Policial", "Dentista", "Açogueiro"]},

    {"nome": "Animes", "itens": ["Naruto", "Pokemon", "Dragon Ball", "One Piece"]},
                       
                       
]

erros = 0
acertos = 0
letras_tentadas = []
while True:
    print("Qual categoria de jogo vai ser? \n" "(1)Animais (2)Comidas (3)Empregos (4)Anime")
    escolher = input()

    if escolher.isdigit():
        break
    else:
        os.system("cls")
        print("Por favor coloque um numero correspondente as alternativas")
        continue

alternativa = int(escolher) - 1

palavra_escolhida = random.choice(palavras_aleatorias[alternativa]["itens"]).lower()

print(palavra_escolhida)


