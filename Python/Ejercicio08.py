cantidad_inicial = float(input("Por favor, introduce la cantidad de dinero depositada en la cuenta de ahorros: "))

tasa_interes = 0.04

ahorros_1er_ano = cantidad_inicial * (1 + tasa_interes)


ahorros_2do_ano = ahorros_1er_ano * (1 + tasa_interes)

ahorros_3er_ano = ahorros_2do_ano * (1 + tasa_interes)


print(f"Cantidad de ahorros tras el primer año: {ahorros_1er_ano:.2f}")
print(f"Cantidad de ahorros tras el segundo año: {ahorros_2do_ano:.2f}")
print(f"Cantidad de ahorros tras el tercer año: {ahorros_3er_ano:.2f}")
