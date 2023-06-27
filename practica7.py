def calcular_costo_total(barras_no_frescas, precio_regular):
    descuento = 0.6  
    precio_descuento = precio_regular * descuento
    costo_total = barras_no_frescas * precio_descuento
    return costo_total

barras_no_frescas = int(input("Ingrese el numero de barras vendidas que no son frescas: "))

precio_regular = 3000

precio_descuento = precio_regular * 0.6
costo_total = calcular_costo_total(barras_no_frescas, precio_regular)

print("Precio regular de una barra de pan: ", precio_regular)
print("Descuento aplicado por no ser fresca: ", precio_descuento)
print("Costo total final: ", costo_total)