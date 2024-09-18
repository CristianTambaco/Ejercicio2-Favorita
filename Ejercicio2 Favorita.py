# Tabla de incrementos
tabla_incrementos = {
    'A': 0.03,  # 3%
    'B': 0.10,  # 10%
    'C': 0.25,  # 25%
    'D': 0.45   # 45%
}

# Solicitar datos del empleado
nombre_empleado = input("Ingrese el nombre del empleado: ")
salario_actual = float(input("Ingrese el salario actual del empleado: "))
tipo_contrato = input("Ingrese el tipo de contrato (A, B, C o D): ")

# Calcular el nuevo salario
if tipo_contrato in tabla_incrementos:
    incremento = tabla_incrementos[tipo_contrato]
    nuevo_salario = salario_actual * (1 + incremento)
    aumento_porcentual = incremento * 100
    print(f"El nuevo salario de {nombre_empleado} será de ${nuevo_salario:.2f} ({aumento_porcentual:.2f}% de incremento).")
else:
    print("Tipo de contrato no válido. Por favor, ingrese A, B, C o D.")