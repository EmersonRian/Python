valor_1 = input("digite um valor: ")
valor_2 = input("digite um valor: ")


def Impar_Par(A,B):
    impa_par = A + B   

    if impa_par % 2 == 0:
        print("Par")
        print(impa_par)
    else:
        print("Ímpar")
        print(impa_par)

def pst_neg(A,B):
    soma = A + B
    if soma < 0:
        print("Numero Negativo")
    else:
        print("Numero Positivo")

try:
    Impar_Par(float(valor_1),float(valor_2))
    pst_neg(float(valor_1),float(valor_2))
except ValueError:
    print("Valor colocado invalido")