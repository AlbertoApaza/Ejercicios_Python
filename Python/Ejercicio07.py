peso_payaso = 112

peso_muneca = 75

num_payasos = int(input("Por favor, introduce el número de payasos vendidos: "))

num_munecas = int(input("Por favor, introduce el número de muñecas vendidas: "))

peso_total = (num_payasos * peso_payaso) + (num_munecas * peso_muneca)

print(f"El peso total del paquete que será enviado es de {peso_total} gramos")
