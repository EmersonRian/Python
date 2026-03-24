import random
"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""
for i in range(10):

    cpf = ""


    numeros_cpf_separados = []
    multiplicavel_1 = 10
    multiplicavel_2 = 11
    soma_numeros_primeiro_digito = []
    soma_numeros_sugundo_digito = []


    for _ in range(9):
        cpf += str(random.randint(0, 9))


    if len(cpf) > 11:
        for i in cpf:
            if i == "." or i == "-":
                continue 

            numeros_cpf_separados.append(int(i))
            
    else:
        for i in cpf:
            numeros_cpf_separados.append(int(i))
        

    for a in numeros_cpf_separados[:9]:
        x = int(a) * multiplicavel_1
        multiplicavel_1 -= 1
        soma_numeros_primeiro_digito.append(x)

    valor_primeiro =  sum(soma_numeros_primeiro_digito) * 10 % 11
    primeiro_digito_cpf = valor_primeiro if valor_primeiro <= 9 else 0
 

    numeros_cpf_separados.append(primeiro_digito_cpf)



    for i in numeros_cpf_separados[:10]:
        x = int(i) * multiplicavel_2
        multiplicavel_2 -= 1
        soma_numeros_sugundo_digito.append(x)

    valor_segundo = sum(soma_numeros_sugundo_digito) * 10 % 11
    segundo_digito_cpf = valor_segundo if valor_segundo <= 9 else 0

    numeros_cpf_separados.append(segundo_digito_cpf)

    cpf_regularizado = numeros_cpf_separados

    for i in cpf_regularizado:
            print(i,end="")
    print()

    


