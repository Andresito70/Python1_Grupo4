#Le pedimos al usuario que digite el numero del año
año = int(input("Digite el numero del año que desea saber si es bisiesto o no\n"))

#Ahora le pedimos que digite el numero de dias que tiene ese año
dias = int(input("Digite el numero de dias que tiene ese año\n"))

#Realizamos las condiciones para determinar si el año es bisiesto o no

if dias == 366:
    print (f"El año {año} que contiene {dias} si es bisiesto\n")
    
elif dias == 365:
    print (f"El año {año} que contiene {dias} no es bisiesto\n")

else:
    print("error")