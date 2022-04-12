#Programa para convertir monedas
#Inputs
#Proceso
opcion = "0"
while(opcion == "0"):
    print ("opcion 1 - soles a dolares")
    print ("opcion 2 - dolares a soles")
    print ("opcion 3 - soles a euros")
    print ("opcion 4 - euros a soles")
    opcion = input("elija una opcion: ")
    montoOrigen = float(input("Ingrese monto"))
    if (opcion == "1"):
        montoDolares = float(montoOrigen) / 3.80
        montoDolaresFormato = "$ {:,.2f}".format(montoDolares)
        print("el monto en dolares es: ", montoDolaresFormato)
    elif (opcion == "3"):
        montoSoles = float(montoOrigen)*3.80
        montoDolaresFormato = "S/. {:,.2f}".format(montoSoles)
        print("el monto en soles es: ", montoDolaresFormato) 
    elif (opcion == "4"):
        montoSoles = float(montoOrigen)/4.05
        montoDolaresFormato = "€ {:,.2f}".format(montoSoles)
        print("el monto en euros es: ", montoDolaresFormato) 
    elif (opcion == "4"):
        montoEuros = float(montoOrigen)*3.80
        montoDolaresFormato = "S/. {:,.2f}".format(montoEuros)
        print("el monto en soles es: ", montoDolaresFormato)
    else:
        print("Opcion Incorrecta")
        opcion2 = input("seguir?")
        if (opcion2 == "si"):
            opcion = input("elija una opcion: ")
        else:
            break

