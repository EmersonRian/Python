# Faça um algoritmo que calcule o IMC (Índice de Massa Corporal) de uma pessoa, leia o seu peso e sua altura e imprima na tela sua condição 

# de acordo com a tabela abaixo:

# Fórmula do IMC = peso / (altura) ²

# Tabela Condições IMC

  

#  Abaixo de 18,5   | Abaixo do peso          

#  Entre 18,6 e 24,9 | Peso ideal (parabéns)  

#  Entre 25,0 e 29,9 | Levemente acima do peso

#  Entre 30,0 e 34,9 | Obesidade grau I 

#  Entre 35,0 e 39,9 | Obesidade grau II (severa)

#  Maior ou igual a 40 | Obesidade grau III (mórbida)



peso = input("Informe seu peso: ")
altura = input("Informe sua altura: ")



def imc_tabela(peso,altura):
    imc = peso / altura ** 2
    return imc

imc = imc_tabela(float(peso),float(altura))

if imc < 18.5 :
    print("Abaixo do peso")
elif imc > 18.6 :
    print("peso ideal (Parabens)")
    