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
frutas.append('piñas')
frutas.append('limones')
frutas.append('sandias')
print(frutas)

frutas.remove("manzanas")
print(frutas)

print("Obteniendo el elemento 4: ", frutas[4])
print("Obteniendo el elemento 0: ", frutas[0])
print("Obteniendo el ultimo elemento: ", frutas[-1])

frutas.reverse()
print('frutas: ', frutas)

frutas.sort()
print('frutas: ', frutas)

nuevo_subtema("if-else")
numero2 = 8
if numero2 > 6:
    print("numero2 es mayor a 6")
else:
    print("numero2 no es mayor a 6")

if frutas:
    print("Algo sucedio")

if temperatura:
    print("En temperatura hay algo ")

edad =0
if edad:
    print("Edad es diferente de cero")
else:
    print("Edad es igual a cero")

if []:
    print("La lista contine algo")
else:
    print('La lista esta vacia')

nuevo_subtema('Ejemplo factorial')

fac = 50
resultado = 1
for num in range(fac):
    aux = fac - num
    resultado = resultado * aux
print(resultado)


nuevo_tema("diccionarios")

carro = {}
print ('carro: ', carro)

carro = {
    "marca" : "volkswagen",
    "anio" : 2024,
    "color": "gris",
    "cilindraje": 4,
    "llantaDeRepuesto": True
}

print ('carro: ', carro)
print ('obteniendo un elemento: ', carro.get('marca'))
print ('obteniendo un elemento: ', carro.get('puertas'))

# print ('obteniendo un elemento: ', carro['marca'])
# print ('obteniendo un elemento: ', carro['puertas'])

print('carro.items()): ', carro.items())
print('carro.values()): ', carro.values())
print('carro.keys()): ', carro.keys())

for key, value in carro.items():
    print(f" {key} -  {value}")

carro.update({"color": "rojo"})
print ('carro: ', carro)

carro.clear()
print ('carro: ', carro)

