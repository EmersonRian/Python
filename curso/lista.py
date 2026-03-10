lista_de_compras = []
dicionario_listas_criadas = []

while True:
    print("O que deseja fazer?\n" "(1)Criar lista   (2)Ver Lista  (3)Excluir Lista  (4)Sair ")
    resposta = input()

    def criar_lista(nome,itens):
        dicionario_listas_criadas.append({"nome": nome, "itens": itens})

    if resposta == "1":
        nome_lista = input("Qual o nome da lista? ")
        itens = input()
        criar_lista(nome_lista,itens)













    if resposta == "4":
        print("sistema finalizado")
        break

for coisas in dicionario_listas_criadas:
    print(coisas["nome"])
