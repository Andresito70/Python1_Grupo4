#Diseñe un script que permita solicitar tanto el nombre como la edad de una persona y
#posteriormente indicar si ella es “Mayor de edad” o “Menor de edad” según la información
#ingresada. Si es mayor podrá acceder a votar, una persona se considera mayor de edad si
#tiene 18 años o más. Debe enviar mensaje si cumple la edad o no cumple la edad para votar
print ("Bienvenido al sistema para detectar si puede votar o no")
nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
if edad > 17:
    print(f"Usted {nombre} es mayor de edad, por lo tanto es candidato para votar")
else: print(f"Usted {nombre} no puede ser votante por ser menor de edad")
print("Fin")