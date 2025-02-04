from a02_Utils import nuevo_tema, nuevo_subtema
print("hola mundo")

# Este es un comentario

"""
Hoy es jueves
Falta poco para salir
Este es un comentario multilínea
"""

nuevo_tema("variables")
# Variables
numero = 4              # int
temperatura = 25.12     # float
nombre = 'Daniela'      # str
fuma = True             # bool

print("numero: ", numero)
print("temperatura: ", temperatura)
print("nombre: ", nombre)
print('"fuma: "', fuma)

print("fuma\n" * 5)

nuevo_tema("Listas_1")
frutas = ['manzanas', 'peras', 'guayabas', 'papayas', 'naranjas', 'kiwis']

print("frutas: ", frutas)

varios = ['Daniela', 25, True, 22.23, frutas]
print('varios: ', varios)

nuevo_tema("funciones")

nuevo_tema("Ciclos")
nuevo_subtema("For_1")
for numero in range(10):
    print(numero)

nuevo_subtema("For_2")
for numero in range(-3,10):
    print(numero)

nuevo_subtema("For_3")
for numero in range(-3,10,2):
    print(numero)

nuevo_subtema("For_4")
for indice, fruta in enumerate(frutas):
    print(indice+1, fruta)


nuevo_tema("Listas_2")
frutas.append('Piñas')
frutas.append('Limones')
frutas.append('Sandias')
print(frutas)

frutas.remove("manzanas")
print(frutas)

print("Obteniendo el elemento 4: ", frutas[4])
print("Obteniendo el elemento 0: ", frutas[0])
print("Obteniendo el ultimo elemento: ", frutas[-1])

