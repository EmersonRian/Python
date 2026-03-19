#  12 - Faça um algoritmo que leia o valor de um produto e determine o valor que deve ser pago, conforme a escolha da forma de pagamento

#  pelo comprador e imprima na tela o valor final do produto a ser pago. Utilize os códigos da tabela de condições de pagamento para efetuar o cálculo adequado.

 

#  Tabela de Código de Condições de Pagamento

 

#  1 - À Vista em Dinheiro ou Pix, recebe 15% de desconto

#  2 - À Vista no cartão de crédito, recebe 10% de desconto

#  3 - Parcelado no cartão em duas vezes, preço normal do produto sem juros

#  4 - Parcelado no cartão em três vezes ou mais, preço normal do produto mais juros de 10%


valor = float(input("valor do produto: "))

while True:

    print(
        "Qual a forma de pagamento? \n"
        "Digite: (1)Pix (2)Cartão a Vista (3)Parcelado"
        )

    pagamneto = input()

    def pix(valor):
        desconto = valor - (valor / 100 * 15)
        return desconto

    def cartao(valor):
        desconto = valor - (valor / 100 * 10)
        return desconto

    def parcelado(valor):
        montante = valor + (valor / 100 * 10)
        return montante



    if pagamneto == "3":
        print("Quantas parcelas? ")
        try:
            parcelas = float(input())
        except ValueError:
            print("coloque numeros")
            continue
        if parcelas <= 2:
            print(f"Valor Final:{valor}")
            break
        if parcelas > 2:
            print(f"Produto sai com 10% de juros.\n Valor Final:{parcelado(valor):.2f}")
            break
            
        
    if pagamneto == "2":
        print(f"Produto sai com 10% de desconto.\n Valor Final:{cartao(valor)}")
        break

    if pagamneto == "1":
        print(f"Produto sai com 15% de desconto. \n Valor Final:{pix(valor)}")
        break
        
    if pagamneto != "1" and "2" and "3":
        print("porfavor coloque um numero conrespondente com a forma de pagamento")
        continue

    