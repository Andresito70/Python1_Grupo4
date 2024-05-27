nom= str(input("Ingresa el nombre del estudiante : "))
cod= int(input("Ingresa el codigo del estudiante : "))
pripa= int(input("Digita cuanto se saco el estudiante en el primer parcial : "))
if pripa > 5 or pripa < 0:
 print("No se permiten datos mayores de 5 y negativos ")


else:
 primerpa=(pripa*35)/100
 segpa= int(input("Digita cuanto se saco el estudiante en el segundo parcial : "))
if segpa > 5 or segpa < 0:
    print("No se permiten datos mayores de 5 y negativos ")
else:
    
    
    segundopa=(segpa*35)/100
    exf= int(input("Digita cuanto se saco el estudiante en el examen final : "))
if exf > 5 or exf < 0:
     print("No se permiten datos mayores de 5 y negativos ")
     
else:
    finalpa=(exf*30)/100
    sum=primerpa+segundopa+finalpa
    round(sum)
    print ("El estudiante ",nom," de codigo",cod," tuvo una definitiva de",sum," en la materia de logica")
    '''SE TIENE QUE SACAR EL LIMITE PARA LA NOTA'''
if sum > 3.5:
    print("El estudiante paso la materia de logica")
else:
    print("El estudiante no pasó la materia")