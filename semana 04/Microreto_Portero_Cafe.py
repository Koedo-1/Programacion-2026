#limpieza de datos  .lower() significa pasar a minuscula
#.upper() pasar a mayuscula
#.strip() quita espacios 
"""Microreto: el portero del café."""

nombre = input("como te llamas? : ")
energia = int(input("Cuanta energia tienes de 0 a 100?: "))
trae_cafe = input("Traes cafe (si/no)?").lower().strip() == "si" 






#procesos
mensaje = ""
#si menos <50% de energia y no tiene cafe : descansar
if energia <= 50 and not (trae_cafe):
    mensaje =(" Acceso denegado: Necesita descansar o tomar cafe")
    
# si 50% o mas o tenga cafe : puede ingresar a la clase   
elif energia >= 50 or (trae_cafe):
    mensaje =("Acceso permitido: pasa con gusto pero invita el cafe")
# else : portero confundido : revisar respuestar 
else:
    mensaje =("Portero confundido. revise sus respuestas")

print(f"{nombre} : {mensaje}")