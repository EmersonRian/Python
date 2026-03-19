salario_minimo = 1512.00

salario_atual = input("diga seu salario: ")

def salarios(a,b):
    if a > b:
        soma = a / b
        print(f"Voce recebe em torno de {int(soma)} salarios minimos")
        multi = a / b * 100
        print(f"Coresponde a {int(multi)}% do salario minimo")
    else:
        multi = a / b * 100
        print(f"Seu salario coresponde a cerca de {int(multi)}% do salario minimo")
    

salarios(float(salario_atual),salario_minimo)