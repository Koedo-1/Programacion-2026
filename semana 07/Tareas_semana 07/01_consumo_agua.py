"""Caso 1: cambio del consumo diario de agua. Complete el programa."""

consumos_litros = [120, 115, 108, 102, 96]

# TODO: Calcule el consumo total y el promedio diario.
consumo_total = sum(consumos_litros)
promedio_diario = consumo_total / len(consumos_litros)

# TODO: Compare el primer día con el último: litros ahorrados y porcentaje
#       de reducción respecto al primer día.
primer_dia = consumos_litros[0]
ultimo_dia = consumos_litros[4]

litros_ahorrados = primer_dia - ultimo_dia
porcentaje_reduccion = litros_ahorrados / primer_dia * 100

# TODO: Clasifique: >=15 % reducción alta; >0 % reducción moderada;
#       de lo contrario, sin reducción.

if porcentaje_reduccion >=15:
    clasificacion = ("Reducción alta")
elif porcentaje_reduccion >0:
    clasificacion = ("Reducción moderada")
else:
    clasificacion = ("sin reducción")

# TODO: Muestre los cinco resultados.

print("Consumo total:", consumo_total)
print("Promedio diario:", promedio_diario)
print("Litros ahorrados:", litros_ahorrados)
print("Porcentaje de reduccion:", porcentaje_reduccion)
print("Clasificación:", clasificacion)



# Control: total 541 L; promedio 108,2 L; ahorro 24 L; reducción 20 %;
#          reducción alta.
# Prueba: use temporalmente cinco consumos iguales. Debe indicar 0 % y
# "Sin reducción". Restaure la lista antes de entregar.
