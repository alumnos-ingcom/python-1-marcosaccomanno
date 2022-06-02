################
# Marco Saccomanno - @marcosaccomanno
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from src.ejercicio8 import es_primo
from src.ejercicio11 import es_multiplo

'''
Para el funcionamiento de la funcion 'factores_primos' se importan las funciones
'es_primo' del ejercicio 8 y 'es_multiplo' del ejercicio 11, ubicados en 'src'.
'''

'''
Precondiciones: La entrada debe ser un numero natural.

Poscondiciones: La salida es una tupla que contiene los factores primos del
numero ingresado.
'''

def factores_primos(numero):
    '''
    Esta funcion toma como entrada un numero natural y devuelve
    una tupla con sus factores primos.
    '''
    factores = ()
    contador = 1
    while contador < numero:
        if es_primo(contador) is True:
            if es_multiplo(numero, contador) is True:
                factores += (contador,)
                contador += 1
            else:
                contador += 1
        else:
            contador += 1
    return factores 
            
def principal():
    '''
    Funcion principal
    '''
    # Entrada
    numero = int(input("Numero: "))
    # Algoritmo
    resultado = factores_primos(numero)
    # Salida
    print(resultado)
     
if __name__ == "__main__":
    principal()
    