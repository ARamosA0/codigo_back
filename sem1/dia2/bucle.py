lados = int(input("Inserte la medida del lado del cuadrado: "))

# for x in range (1,lados+1):
#     for y in range(1,lados+1):
#         print("*", end=" ")
#     print("")
        

for i in range(1, lados):
    print("* ", end="")

for i in range(1, lados):
    print("* "+" "*(lados+1)+"*")

for i in range(1, lados+1):
    print("* ", end="")

