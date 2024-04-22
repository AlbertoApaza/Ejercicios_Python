nombre_producto = input("Por favor, introduce el nombre del producto: ")

precio_unitario = float(input("Por favor, introduce el precio unitario del producto: "))

num_unidades = int(input("Por favor, introduce el número de unidades: "))

coste_total = precio_unitario * num_unidades

print(f"{nombre_producto}: {precio_unitario:06.2f} {num_unidades:03d} {coste_total:08.2f}")
