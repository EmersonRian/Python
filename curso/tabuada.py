numero = 1

while True:

    print(f"Tabuada Do {numero}")

    for i in range(1,11):
        mult = numero * i  
        print(f"{numero} * {i} = {mult}")

    numero += 1
    print()

    if numero == 11:
        break

