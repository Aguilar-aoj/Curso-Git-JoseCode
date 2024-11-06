rango_inicio = int(input("ingrese un numero a partir de 3 cifras: "))
rango_final = int(input("ingrese un segundo numero a partir de 3 cifras: "))
for rango in range(rango_inicio, rango_final):
    cadenas_de_enteros = []
    for digito in str(rango):
        cadenas_de_enteros += digito
        longitud_la_lista = len(cadenas_de_enteros)
    if longitud_la_lista < 3:
            print("\nTiene que se un numero de 3 cifras")
    else:
        cadena1 = int(cadenas_de_enteros[0]) ** longitud_la_lista
        cadena2 = int(cadenas_de_enteros[1]) ** longitud_la_lista
        cadena3 = int(cadenas_de_enteros[2]) ** longitud_la_lista
        suma_de_enteros = cadena1 + cadena2 + cadena3
        comparador_de_enteros = int("".join(cadenas_de_enteros))
        if comparador_de_enteros == suma_de_enteros:
            print(suma_de_enteros)
            
            
            
"""rango_inicio = int(input("ingrese, por favor, un numero de 3 cifras: "))
rango_final = int(input("ingrese un segundo numero a partir de 3 cifras:"))
for i in range(1):
    lista_armstrong = []
    for rango in range (rango_inicio, rango_final):
        cadenas_de_enteros = []
        for digito in str(rango):
            cadenas_de_enteros += digito
            longitud_la_lista = len(cadenas_de_enteros)
        if longitud_la_lista < 3:
            for i in range(1):
                print("\nTiene que ser un numero de 3 cifras")
        else:
            cadena1 = int(cadenas_de_enteros[0])**longitud_la_lista
            cadena2 = int(cadenas_de_enteros[1])**longitud_la_lista
            cadena3 = int(cadenas_de_enteros[2])**longitud_la_lista
            suma_de_enteros = cadena1 + cadena2 + cadena3
            comparador_de_enteros = int("".join(cadenas_de_enteros))
            if comparador_de_enteros == suma_de_enteros:
                lista_armstrong.append(suma_de_enteros)
print(f"\nEntre {rango_inicio} y {rango_final} \el numero de Armstrong\nque encontramos fue\n{lista_armstrong}")    """