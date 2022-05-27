################
# Marco Saccomanno - @marcosaccomanno
# UNRN Andina - Introducción a la Ingenieria en Computación
################

'''
Precondiciones: Los valores de entrada deben ser dos numeros enteros.

Poscondiciones: La salida es un numero entero resultante de la suma
de ambos numeros de entrada.
'''

def suma_lenta(numero, otro_numero):
    '''
    Esta funcion toma como entrada dos numeros enteros y realiza una
    suma lenta (de +1) hasta llegar al resultado de la suma entre ambos numeros.
    '''
    largo = otro_numero
    suma = numero
    while largo > 0:
        print(f"{suma} + 1")
        suma += 1
        largo -= 1
    return suma
    
def principal():
    ''' Funcion principal '''
    # entrada
    numero = int(input("Numero 1: "))
    otro_numero = int(input("Numero 2: "))
    # algoritmo
    operacion = suma_lenta(numero, otro_numero)
    # salida
    print(operacion)
    
if __name__ == "__main__":
    principal()
    