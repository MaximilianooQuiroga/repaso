def contar_palabra(frase):
    lista = frase.split()
    cantidad = len(lista)
    return cantidad

cant = contar_palabra("Estudiando para los examenes")
print(cant)
