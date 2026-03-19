numero = input("digite: ")

def antes(a):
    antecessor = a - 1
    sucessor = a + 1
    print(f"o Sucessor de {a} é {sucessor}")
    print(f"o Antecessor de {a} é {antecessor}")

try:
    antes(int(numero))
except:
    print("numero invalido")