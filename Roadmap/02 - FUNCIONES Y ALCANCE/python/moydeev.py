#funciones

#argumentos de entrada
# def di_hola():
#     print("HOLA")

# di_hola()

#si hay argumentos se deben colocar al colocaelo
def di_hola(nombre):
    print("Hola", nombre)

di_hola("Samuel")

#argumentos por posición
def resta (a, b):
    return a-b
resta(5,3) #2
#otra forma de llamar a una funcion
#argumentoss por nombre
resta(a=3, b=5)
#el orden de llamar, ya no importa
resta(b=5, a=3)

#Argumentos por defecto
def suma (a,b,c=0):
    return a+b+c
suma(5,5,3)

#dado que c tiene el valor de 0, la funcion puede ser llamada sin la c
suma(5,5)

#cuando la funcion ya tiene declaradas las variables puede ser llamada sin argumentos
def suma2(a = 2, b= 4,c = 3):
    return a+b+c
suma()

#argumentos de longitud variable
def suma3_1(numeros):
    total = 0
    for n in numeros:
        total += n
        return total
    suma3_1([1,2,3,5,4])


# usar * en el argumento hace que se pase empaquetado en una tupla 
def suma3(*numeros):
    print(type(numeros))
    total = 0
    for n in numeros:
        total += n
        return total
suma3(1,3,5,4)

#usar ** se hace una lista de elementos almacenados en forma de clave y valor
# se puede iterar usando items()

def suma4(**kwargs):
    suma = 0
    for key, value in kwargs.item():
        print(key, value)
        suma += value
    return suma

suma4(a=5, b=20, c=23)