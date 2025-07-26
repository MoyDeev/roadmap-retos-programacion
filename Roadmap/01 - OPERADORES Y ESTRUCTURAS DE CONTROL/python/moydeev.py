# operadores
numero = 2
suma = 2 + 2
resta = 2-1
multiplicacion = 5*5
division = 10/2

print(division)

#condiciones = las condiciones en python nos permiten ejecutar una o varias instrucciones
# si se cumple una condición
a = 4

if (a == 4):
    print("igual")

if(a == 4):
    print("igual")
else:
    print("no es igual")

if(a == 4):
    print("es igual")
elif(a == 1):
    print("no es igual")
else:
    print("es igual")

#bucles
#while: el bucle while se ejecuta mientras se cumpla una condicion. 
edad = 8
while (edad < 10):
    print("menor de edad")

#for
#el bucle for nos permite iterar sobre una condición sobre una consecuencia
#de elementos (listas, tuplas, diccionarios)

for i in range(5):
    print(i)

lista = [1,2,3,4,5]
i = 0
encontrado = False
while i < len(lista) and not encontrado:
    if lista[i] == 3:
        print("Numero encontrado en la posición: ", i)
        encontrado = True
        1 += 1    
