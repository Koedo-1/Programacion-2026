#TODO: solicita los datos.
#TRY // EXCEPT

nombre = input("Ingrese su nombre: ").upper().strip()

kit = input("Tipo de kit: ").strip().lower()

autorizacion = input("Tiene autorizacion? SI/NO: ").strip().lower() == "si"
try:
    cantidad = int(input("Cantidad de kits?"))
    if cantidad <1:
        print("Error: La cantidad minima es 1")
    
except ValueError:
    print("Cantidad de kits invalidas, digite del 1 al 100")
    cantidad = -1


try:
    dias = int(input("Dias de prestamo?:"))
except ValueError:
    print("Dias invalidos , Digite de 0 a 10")
    dias = 0


#Proceso
#nombre vacio o numeros invalidos
resultado = ""

if not nombre or not kit or cantidad <1 or dias <1:
    resultado = "Registro Rechazado: Revise los datos ingresados!"
    
#autorizado 3 kits 7 dias
    
elif (autorizacion) and (cantidad <= 3 ) and not (dias > 7):
    resultado = f("Solicitud aprobada para {nombre}: {cantidad} kit(s) de {dias}")
else:
    resultado = ("Solicitud envidada a revision")
 

print("-" * 50, "\n")
print(f"{nombre}, su {resultado}")

