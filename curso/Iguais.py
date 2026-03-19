# Faça um algoritmo que leia dois valores inteiros A e B, se os valores de A e B forem iguais, deverá somar os dois valores, 

# caso contrário devera multiplicar A por B. Ao final de qualquer um dos cálculos deve-se atribuir o resultado a uma variável C e

# imprimir seu valor na tela.

a = input("diga: ")
b = input("diga: ")


def Numeros_Iguais(A,B):
    if A == B:
        soma = A + B
        print(f"C = {A} + {B}")
        print(f"C = {soma}")
    else:
        multi = A * B
        print(f"C = {A} * {B}")
        print(f"C = {multi}")


try:
    Numeros_Iguais(int(a),int(b))
except ValueError:
    print("Este valor não é um numero inteiro")


