def calcular_ahorros_iniciales(cantidad_dinero, tasa_interes, anos):
    saldo = cantidad_dinero
    for i in range(anos):
        intereses = saldo * tasa_interes / 100
        saldo += intereses
    return saldo

cantidad_dinero = float(input("Ingrese la cantidad de dinero depositada en la cuenta de ahorros: "))

tasa_interes = 4

ahorros_primer = calcular_ahorros_iniciales(cantidad_dinero, tasa_interes, 1)
ahorros_segundo = calcular_ahorros_iniciales(cantidad_dinero, tasa_interes, 2)
ahorros_tercer = calcular_ahorros_iniciales(cantidad_dinero, tasa_interes, 3)

print("Cantidad de ahorros despues del primer ano:", round(ahorros_primer, 2))
print("Cantidad de ahorros despues del segundo ano:", round(ahorros_segundo, 2))
print("Cantidad de ahorros despues del tercer ano:", round(ahorros_tercer, 2))