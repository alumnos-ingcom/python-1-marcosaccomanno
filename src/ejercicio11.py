################
# Marco Saccomanno - @marcosaccomanno
# UNRN Andina - Introducción a la Ingenieria en Computación
################

'''
Precondiciones: La entrada deben ser dos numeros enteros.

Poscondiciones: La salida es un valor booleano True si el segundo numero es
multiplo del primero, y False si no lo es.
'''

'''
Para el funcionamiento de la funcion 'es_multiplo' se importa la funcion
'division_lenta' creada en el ejercicio 5 ubicado en 'src'.
'''

from src.ejercicio5 import division_lenta

def es_multiplo(numero, multiplo):
    '''
    Esta funcion toma como entrada dos numeros enteros y devuelve True si
    el segundo es multiplo del primero y False si no lo es
    '''
    cociente, resto = division_lenta(numero, multiplo)
    if resto == 0:
        resultado = True
    else:
        resultado = False
    return resultado

def principal():
    '''
    Funcion principal
    '''
    # Entrada
    numero = int(input("Numero: "))
    multiplo = int(input("Multiplo: "))
    # Algoritmo
    resultado = es_multiplo(numero, multiplo)
    # Salida
    print(resultado)

if __name__ == "__main__":
    principal()
    