# Faça um algoritmo que leia um valor qualquer e imprima na tela com um reajuste de 5%.

print("Reajuste de preço com desconto ou com aumento de preço?")
reajuste = input("(1)Desconto     (2)Aumento: ")

if reajuste == "2":
    valor_qualquer = input("Digiteo valor: ")
    mult = float(valor_qualquer) / 100 * 5
    soma = mult + float(valor_qualquer)
    print(soma)
elif reajuste == "1":
    valor_qualquer = input("Digiteo valor: ")
    mult = float(valor_qualquer) / 100 * 5
    soma = float(valor_qualquer) - mult
    print(soma)
else:
    print("por favor, digite 1 ou 2 para sabermos qual sua inteção")
    


