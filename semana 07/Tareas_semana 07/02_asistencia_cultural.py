"""Caso 2: asistencia por bloques. Complete el análisis con un ciclo for."""

asistencias = [120, 180, 210, 250, 230]
capacidad = 300

# TODO: Recorra asistencias con for para acumular el total y contar los bloques
#       que SUPERAN el 70 % de la capacidad (210 no cuenta).

contador = 0 
acumulador = 0 


for asistencia in asistencias:
    acumulador += asistencia
    if asistencia >210:
        contador +=1



# TODO: Calcule el promedio y su porcentaje de ocupación.
cantidad = len(asistencias)
promedio = acumulador / cantidad
porcentaje_de_ocupacion = promedio / 300 * 100


# TODO: Clasifique el promedio: >=80 % alta; >=50 % media; si no, baja.
if porcentaje_de_ocupacion >=80:
    estado = ("Alta")
elif porcentaje_de_ocupacion >=50:
    estado = ("Media")
else:
    estado = ("Baja")

# TODO: Muestre total, promedio, porcentaje, cantidad de bloques y estado.
# Con los datos base: total 990, promedio 198, 66 %, 2 bloques, ocupación media.
# Prueba de código: use temporalmente cinco bloques con 240 asistentes cada uno
# para comprobar el límite del 80 %. Después restaure la lista.

print (f"Total de asistencias: {acumulador}\n"
f"Bloques que superan el 70%: {contador}\n"
f"Promedio: {promedio}\n"
f"Porcentaje de ocupación: {porcentaje_de_ocupacion}%\n"
f"Estado: {estado}")