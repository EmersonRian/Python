valor_a = input("diga o valor de A; ")
valor_b = input("diga o valor de B; ")
valor_c = input("diga o valor de C; ")



def soma(A,B,C):
    valor = A + B
    if valor < C:
        print(f" {valor_a} + {valor_b} é {valor}")
        print(f" {valor} é menor que {valor_c}")
    elif valor == C:
        print(f" {valor_a} + {valor_b} é {valor}")
        print(f" {valor} é igual a {valor_c}")
    else:
        print(f" {valor_a} + {valor_b} é {valor}")
        print(f" {valor} é maior que {valor_c}")
        

try:
    resultado = soma(float(valor_a),float(valor_b),float(valor_c))
except ValueError:
    print("Valor colocado é invalido")


