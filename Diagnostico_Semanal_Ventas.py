"""Plantilla guiada: análisis de ventas de dos tiendas, sin ciclos."""

ventas_centro = [125000, 98000, 147000, 132000, 110000]
ventas_norte = [140000, 135000, 150000, 145000, 155000]
meta_centro = 640000
meta_norte = 700000

# TODO: calcula total, cantidad, mayor y menor para Centro.
total_centro = sum(ventas_centro)#Total de ventas semanal
cantidad_centro = len(ventas_centro) #cantidad de elementos en lista o coleccion 


menor_centro = min(ventas_centro)#Venta minimo
mayor_centro = max(ventas_centro)#venta maximo 
promedio_centro = total_centro / cantidad_centro

porcentaje_centro = total_centro * 100 / meta_centro

#print(porcentaje_centro)

# TODO: repite los indicadores para Norte.
total_norte = sum(ventas_norte)#Total de ventas semanal
cantidad_norte = len(ventas_norte) #cantidad de elementos en lista o coleccion 


menor_norte = min(ventas_norte)#Venta minimo
mayor_norte = max(ventas_norte)#venta maximo 
promedio_norte = total_norte / cantidad_norte

porcentaje_norte = total_norte * 100 / meta_norte

#print(porcentaje_norte)

# 

# TODO: decide si cada tienda superó, igualó o no alcanzó su meta.

if total_centro > meta_centro:
    estado_centro = ("Meta superada!")
elif total_centro == meta_centro:
    estado_centro == "meta alcanzada exactamente"
else:
    estado_centro = "meta No alcanzada"


if total_norte > meta_centro:
    estado_norte = ("Meta superada!")
elif total_norte == meta_norte:
    estado_norte == "meta alcanzada exactamente"
else:
    estado_norte = "meta No alcanzada"
    

# TODO: compara los totales y los rangos.


if total_centro > total_norte:
    tienda_gano = "Tienda Centro"
elif total_norte > total_centro:
    tienda_gano = "Tienda del Norte"
else:
    tienda_gano = "Ambas tiendas tienen el mismo total"

# TODO: presenta un reporte con etiquetas claras y f-strings.
# TODO: escribe las tres conclusiones solicitadas en la guía.

print("\t\tCOMPARACION SEMANAL DE TIENDAS")
print("-" * 70,"\n")
print(f"Centro | total ₡{total_centro:,.2f} | meta  ₡{meta_centro:,.2f} | cumplimiento {porcentaje_centro:.0f}% ")
print(f"Centro logro: {estado_centro}")

print("-" * 60,"\n")
print(f"NORTE | Total  ₡{total_norte:,.2f} || meta  ₡{meta_norte:,.2f} | cumplimiento {porcentaje_norte:.0f}% ")
print(f"Norte logro: {estado_norte}")

#list es una caja organizadora []
#indexar es numerar [] tambien selecciona que quiere print
#indicadores contexto 
