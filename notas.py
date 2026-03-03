
#  11 - Faça um algoritmo que leia quatro notas obtidas por um aluno, calcule a média das nota obtidas,
#  imprima na tela o nome do aluno e 

#nota do {semetre}° semestre :

semestre = 1
notas = []


print("Qual nome do aluno?")
aluno = input()

while semestre < 5:
    notas.append(float(input(f"nota do {semestre}° semestre: ")))
    semestre += 1

def media_das_notas():
    media_das_notas = sum(notas) / len(notas)

    if media_das_notas >= 7:
        print(f"Aluno {aluno} passou de ano")

        for a, b in enumerate(notas, start=1):   
            print(f"Nota {b} no {a}° semestre")

        print(f"Com media de {media_das_notas}")

    if media_das_notas < 7:
        print(f"Aluno {aluno} esta de recuperação")

        for a, b in enumerate(notas, start=1):   
            print(f"Nota {b} no {a}° semestre")
            
        print(f"Com media de {media_das_notas}")

media_das_notas()









