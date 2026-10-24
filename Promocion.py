#              0      1    2 
producto = ["Cafe", 5000, 20]

# precio actual × 15 ÷ 100.
porcentaje_aumento = 20
descuento = (producto[1] * 15 / 100)
precio_promocional = (producto[1] - descuento)

#unidades actuales × porcentaje de aumento ÷ 100
aumento_unidades = (producto[2] * porcentaje_aumento / 100)
unidades_totales = (producto[2] + aumento_unidades)

# precio actual × unidades actuales.
ingreso_actual = producto[1] * producto[2] 

# precio promocional × unidades proyectadas.
ingreso_proyectado = (precio_promocional * unidades_totales)

diferencia = ingreso_proyectado - ingreso_actual

# >0 recomienda lanzar <= 0 no lanzar
if diferencia > 0:
    lanzar = ("Se recomienda lanzar la promoción")
else:
    lanzar = ("No se recomienda lanzar la promoción  ")

#Salida
print("ANÁLISIS DE PROMOCIÓN", "\n")

