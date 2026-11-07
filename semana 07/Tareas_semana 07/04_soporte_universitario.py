"""Caso 4: analice los registros de soporte sin crear funciones propias."""

from incidencias import incidencias

# Cada incidencia es un diccionario: id, provincia, categoria,
# minutos_atencion y resuelto (True o False).

# TODO: Prepare un acumulador de minutos, un diccionario para contar
#       "Acceso", "Equipo" y "Red", un contador de casos pendientes,
#       un set de provincias con pendientes, una lista de tuplas de casos
#       urgentes y una tupla para el caso con más minutos de atención.


acumulador_minutos = 0 
categorias = {"Acceso": 0 , "Equipo": 0 , "Red": 0 }
contador_casos_pend = 0 
provincias_pend = set()
casos_urgentes = []
caso_m_ate = ()


# TODO: Recorra incidencias una sola vez. Actualice los acumuladores y el
#       conteo de la categoría de cada registro.
max_minutos = -1 
for incidencia in incidencias:
    acumulador_minutos += incidencia["minutos_atencion"]
    categoria = incidencia["categoria"]
    categorias[categoria] += 1
    
    if incidencia["minutos_atencion"] > max_minutos:
        max_minutos = incidencia["minutos_atencion"]
        caso_m_ate = (incidencia["id"], incidencia["provincia"], incidencia["minutos_atencion"])
    if not incidencia["resuelto"]:
        contador_casos_pend += 1
        provincias_pend.add(incidencia["provincia"])
        
        if incidencia["minutos_atencion"] > 60:  
            casos_urgentes.append((incidencia["id"], incidencia["minutos_atencion"]))


# TODO: Si un caso NO está resuelto, cuéntelo y agregue su provincia al set.
#       Si, además, tiene 60 minutos o más, agregue (id, minutos) a la lista
#       de casos urgentes. Actualice la tupla del caso más largo si corresponde.




# TODO: Muestre total y promedio de minutos, conteo por categoría, cantidad
#       de pendientes, provincias con pendientes, casos urgentes y caso más
#       largo. Compruebe también si "San Jose" pertenece al set.

print("Total de minutos:", acumulador_minutos)
if len(incidencias) > 0:
    print("Promedio de minutos:", acumulador_minutos / len(incidencias))

print("Conteo por categoría:", categorias)
print("Cantidad de casos pendientes:", contador_casos_pend)
print("Provincias con pendientes:", provincias_pend)
print("Casos urgentes:", casos_urgentes)
print("Caso más largo:", caso_m_ate)
print("¿San Jose pertenece al set de pendientes?:", "San Jose" in provincias_pend)




# Control: 10 casos; 500 minutos; promedio 50; Acceso 4, Equipo 3, Red 3;
# 4 pendientes en 4 provincias; urgentes INC-02, INC-05 e INC-07;
# más largo INC-07 con 95 minutos; hay pendientes en San Jose.
# Prueba: cambie temporalmente INC-07 a resuelto=True. Debe salir de la
# lista de urgentes, del conteo de pendientes y del set de provincias
# pendientes, pero seguir como caso más largo. Restaure incidencias.py.
