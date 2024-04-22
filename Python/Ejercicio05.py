peso = float(input("Por favor, intriduce tu peso en kg: "))

estatura = float(input("Por favor, introduce tu estatura en metros: "))

imc = peso / (estatura ** 2)

imc_redondeado = round(imc, 2)

print(f"Tu indeice de masa corporal es {imc_redondeado}")