# Elaborar un script que lea N consumos de una cafetería, si el consumo total excede los 
# $100.000, el descuento será del 5%, si el total excede de los $ 300.000, el descuento 
# seria del 10%, mostrar el pago total sin descuento y con descuento.
print ("Bienvenido al calculador de Descuento de consumos en la cafeteria")
consumos = int(input("ingrese el valor de su factura: "))
if consumos > 150000: 
    descuento = consumos * (5 / 100)
    valor_con_descuento = consumos - descuento
    print(f" Felicidades pudo acceder al descuento, El valor con descuento es {valor_con_descuento}")
else: print(f"Su deuda no cumple la condicion para acceder al descuento, entonces pagué {consumos}")
print ("Fin")