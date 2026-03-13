import os


lista_de_compras = []
dicionario_listas_criadas = []

while True:
    print("O que deseja fazer?\n" "(1)Criar lista  (2)Ver Lista  (3)Sair ")
    resposta = input()
    os.system('cls')#limpar terminal


    def criar_lista(nome,itens):#funçao para adicionar um dicionario com o nome e uma lista com os itens
        dicionario_listas_criadas.append({"nome": nome, "itens": itens})

    def colocar_itens_lista():#funçao para colocar itens na lista
        while True:
            itens_da_lista = input()
            if itens_da_lista != "s":
                lista_de_compras.append(itens_da_lista)
            else:
                break

    def mostrar_lista():
            for lugar, numero in enumerate(dicionario_listas_criadas,start= 1):
                print(f"({lugar}) {numero["nome"]}")
            


    def manusear_lista():
        """Mostrar produtos da lista"""
        for produto, itens in enumerate(dicionario_listas_criadas[acessar_lista]["itens"], start=1):
            print(f"Itens {produto}: {itens}")


    def mudar_nome_lista():
        print("Qual novo nome da lista?")
        novo_nome = input()

        dicionario_listas_criadas[acessar_lista]["nome"] = novo_nome
        #limpar terminal
        os.system('cls')

        print("Nome Alterado")
            
    def mudar_iten():

        print("deseja mexer na sua lista?\n" "(1)Alterar nome (2)Mudar iten (3)Excluir lista (4)Sair")
        alterar = input()#Alterar coisas na lista
        if alterar == "1":
            mudar_nome_lista()
        if alterar == "2":
            local_iten = int(input("Qual itens alterar? Coloque o numero corespondente ao iten: ")) - 1
            novo_iten = input("qual o novo iten? ")

            dicionario_listas_criadas[acessar_lista]["itens"][local_iten] = novo_iten

            #limpar terminal
            os.system('cls')
            print("iten alterado")

        if alterar == "3":
            print("deseja excluir essa lista? lista excluida não voltara.\n" " (1)Sim (2)Não")
            excluir = input()
            if excluir == "1":
                excluir_lista()
        

        

    def excluir_lista():
        dicionario_listas_criadas.pop(acessar_lista)
        print("lista Excluida")
        #limpar terminal
        os.system('cls')

        


                
        






    if resposta != "1" and resposta != "2" and resposta != "3":
        print("ERRO:Caractere Invalido. Coloque o numero indicado para fazer o que deseja ")

    if resposta == "1":#Criar lista
        lista_de_compras = []

        nome_lista = input("Qual o nome da lista? ")
        print("O que deseja colocar em sua lista? se deseja (s)air")

        colocar_itens_lista()
        criar_lista(nome_lista,lista_de_compras)


    #Mostrar todas as listas criadas
    if resposta == "2": 

        if len(dicionario_listas_criadas) == 0:
            print("Não á listas criadas")

        else:
            lista_de_compras = []
            mostrar_lista()
            print("Qual lista deseja ver? digite o numero respectivo para ver a lista:")
            acessar_lista = int(input()) - 1

            if (len(dicionario_listas_criadas) - 1) < acessar_lista:
                #limpar terminal
                os.system('cls')

                print("numero invalido: lista nao existe")

            else:
                manusear_lista()
                mudar_iten()
            



        
    #Terminar o sistema
    if resposta == "3":
        print("Programa Finalizado")
        break


# dicionario_listas_criadas = [{"nomes": "emerson", "itens": [1,2,3,4]}]


# print(len(lista_de_compras))






#     if resposta == "4":
#         print("sistema finalizado")
#         break
# dicionario_listas_criadas.append({"nome": "emerson", "itens": lista_de_compras})




# for numero, itens in enumerate(dicionario_listas_criadas["itens"]):
#     print(itens)

# for produto, itens in enumerate(dicionario_listas_criadas[0]["itens"], start=1):
#     print(f"Produto {produto}: {itens}")

