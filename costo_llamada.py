# Programa No. 1: Ingresar el tiempo de duración de una llamada y determinar la cantidad a pagar


print("-----------------------------")
print("-------Duración Llamada------")
print("-----------------------------")

# input

t = int(input("Ingrese el tiempo de duración de la llamada en numero entero y minutos: "))

# processing

if t>3:
    t= 300+(t-3)*50

else:
    t= 300

# output

print("-----------------------------")
print("---------RESULTADOS----------")
print("-----------------------------")

print("El valor total a pagar por la llamada es de: $ "+str(t))
