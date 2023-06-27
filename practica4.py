cantidad_invertir = float(input("Ingrese la cantidad a invertir: "))
tasa_interes_anual = float(input("Ingrese la tasa de interes anual (%): "))
num_anios = int(input("Ingrese el numero de anos: "))

tasa_interes_decimal = tasa_interes_anual / 100

capital_obtenido = cantidad_invertir * (1 + tasa_interes_decimal) ** num_anios

print("El capital obtenido en la inversion es:", capital_obtenido)