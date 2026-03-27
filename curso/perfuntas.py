
perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

num = 0

for i in perguntas:
    print(perguntas[num]['Pergunta'])

    for opc in perguntas[num]['Opções']:
        print(f"( ){opc}")

    resp = input()

    if resp == perguntas[num]['Resposta']:
        print("Acertou")
    else:
        print("errou")

    num += 1
