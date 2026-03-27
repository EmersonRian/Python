

def soma(nacimento):
    anos = 2026 - int(nacimento)
    mes = anos * 12
    dias = mes * 30
    print(f"Em media voce viveu:\n {anos} Anos\n {mes} Meses\n {dias} Dias")

while True:
    ano_de_nacismento = input("Digite seu ano de nacimento: ")

    if ano_de_nacismento.isdigit() and len(ano_de_nacismento) == 4:
        soma(ano_de_nacismento)
        break
    else:
        print("Ano invalido")
        continue

    
