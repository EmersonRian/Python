# estoque = [

#     ["fab1"], [70,70,70,70,70,70],
#     ["fab2"], [70,70,40,70,70,40],
#     ["fab3"], [70,70,70,70,70,70],
#     ["fab4"], [70,70,70,70,70,30],
#     ["fab5"], [70,70,70,70,70,70], 

# ]

# fabricas = ["fab1","fab2","fab3","fab4","fab5"]


# estoque = [
    
#     [70,70,70,70,70,70],
#     [70,70,40,70,70,40],
#     [70,70,70,70,70,70],
#     [70,70,70,70,70,30],
#     [70,70,70,70,70,70], 

# ]

# fabrica_baixo_nivel = []

# class Verificar_nivel_estoque:

#         lista = 0
#         lugar_lista = 0
#         while lista < 7:
#             if estoque[lista][lugar_lista] == 70:
#                 print("nivel estavel")
#                 lugar_lista + 1
#                 if lugar_lista == 7:
#                      lista + 1
#             elif estoque[lista][lugar_lista] < 70:
#                 print("baixo do nivel")
#                 lugar_lista + 1
#                 if lugar_lista == 7:
#                      lista + 1
                
                
#         else:
#              print("acabou")
            

    
# teste1 = Verificar_nivel_estoque("a")


# class Verificar_nivel_estoque:

#         lista = 0
#         lugar_lista = 0
#         fab = 0
        
#         while True:

#             if estoque[lista][lugar_lista] > 50:
#                 lugar_lista += 1
#                 if lugar_lista  == 6:
#                     fab += 1
#                     lista += 1
#                     lugar_lista = 0
#                     if lista == 5:
#                         break
                    
#             else:
#                  fabrica_baixo_nivel.append(fabrica[fab])
#                  print(fabrica_baixo_nivel)


# for nivel in enumerate(estoque[1], start=1):
#     print(nivel)

# fab = 0
# while True:


#     def nivel_estoque(fab):
#         for nivel in estoque[fab]:
#             if nivel < 50:
#                 fabrica_baixo_nivel.append(fabrica[fab])
#                 fabrica_baixo_nivel.append(nivel)

#             if nivel > 50:
#                 continue   

#     nivel_estoque(fab)
#     fab += 1
#     if fab == 5:
#         print(fabrica_baixo_nivel)
            
#         break

fabricas = ["fab1","fab2","fab3","fab4","fab5"]


estoque = [
    
    [70,70,70,70,70,70],
    [70,70,40,70,70,40],
    [70,70,70,70,70,70],
    [70,70,70,70,70,30],
    [70,70,70,70,70,70], 

]

fabrica_baixo_nivel = []

          
fabrica = 0
while True:


    def nivel_estoque(fabrica):
        for setor, nivel in enumerate(estoque[fabrica], start=1):
            if nivel < 50:
                fabrica_baixo_nivel.append([fabricas[fabrica],setor,nivel])
            if nivel > 50:
                continue   

    nivel_estoque(fabrica)
    fabrica += 1
    if fabrica == 5:
        for fabrica,setor, nivel in fabrica_baixo_nivel:
            print(f"Na fabrica {fabrica}, o setor {setor} esta abaixo da media: {nivel}")

            
        break

    






# nivel_minimo = 50
# fabricas_abaixo_nivel_50 = [] #lista auxiliar

# for i, lista in enumerate(estoque):
#     for a, quantidade in enumerate(lista):
#         if quantidade < nivel_minimo:
#             if fabrica[i] in fabricas_abaixo_nivel_50:
#                 pass
#             else:
#                 fabricas_abaixo_nivel_50.append(fabrica)


# print(fabricas_abaixo_nivel_50)
# numero = 1
# print(estoque)
# print(len(estoque))

# estoque.insert(0,fabrica)
# print(estoque[3][2])