num_varones = int(input("Ingrese el número de varones en el salón: "))
num_mujeres = int(input("Ingrese el número de mujeres en el salón: "))

total_estudiantes = num_varones + num_mujeres

porcentaje_varones = (num_varones / total_estudiantes) * 100
porcentaje_mujeres = (num_mujeres / total_estudiantes) * 100

print(f"El porcentaje de varones es: {porcentaje_varones:.2f}%")
print(f"El porcentaje de mujeres es: {porcentaje_mujeres:.2f}%")
