def calcular_peso_total(payasos, munecas):
    peso_payaso = 112  
    peso_muneca = 75  

    peso_total = (peso_payaso * payasos) + (peso_muneca * munecas)
    return peso_total

num_payasos = int(input("Ingrese el numero de payasos vendidos: "))
num_munecas = int(input("Ingrese el numero de muuecas vendidas: "))

peso_total_paquete = calcular_peso_total(num_payasos, num_munecas)

print("El peso total del paquete a enviar es:", peso_total_paquete, "gramos")