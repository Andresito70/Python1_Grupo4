n1= int(input("Digite el primer numero:\n"))
n2= int(input("Digite el segundo numero: \n"))

#Creamos una lista vacia donde entraran los dos numeros a ordenar
lista = [n1,n2]
print(f"Los numeros ingresados son {lista}\n")

#.sort() para ordenar la lista
lista.sort()
print(f"Los numeros ordenados son: {lista}\n")
#Finalmente se muestra la lista previamente ordenada
print (lista)