"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

numero_inteiro = input("digite um numero inteiro: ")

try:
    if int(numero_inteiro) % 2 == 0:
        print("numero par")
    else:
        print("numero impar")
except:
    print("isso nao é uma numero interio")

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

hora_do_dia = input("que horas são? somente hora: ")
try:
    if int(hora_do_dia) >= 0 and int(hora_do_dia) <= 4:
        print("Boa madrugada")
    if int(hora_do_dia) >= 5 and int(hora_do_dia) <= 11:
        print("Bom Dia")
    if int(hora_do_dia) >= 12 and int(hora_do_dia) <= 17:
        print("Boa Tarde")
    if int(hora_do_dia) >= 18 and int(hora_do_dia) <= 23:
        print("Boa noite")
except:
    print("somente hora")


"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome_usuario = input("me fale seu nome: ")

if len(nome_usuario) <= 4:
    print("seu nome é curto")
if len(nome_usuario) ==5 or len(nome_usuario) == 6:
    print("nome é de um tamanho normal")
if len(nome_usuario) > 6:
    print("seu nome é enorme hoooo")
