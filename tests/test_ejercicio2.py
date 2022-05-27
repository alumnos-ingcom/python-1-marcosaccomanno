################
# Marco Saccomanno - @marcosaccomanno
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from src.ejercicio2 import signo

'''
Los siguientes tests se encargan de probar las funciones del archivo 'ejercicio2.py'
ubicado en 'src'.
'''

def test_signo_positivo():
    '''
    Prueba de la funcion signo() para los valores positivos. 
    '''
    numero = 3
    resultado = signo(numero)
    assert isinstance(resultado, int), "El resultado debe ser un numero entero"
    assert resultado == 1, "El resultado para el valor positivo debe ser 1"
    
def test_signo_negativo():
    '''
    Prueba de la funcion signo() para los valores negativos. 
    '''
    numero = -3
    resultado = signo(numero)
    assert isinstance(resultado, int), "El resultado debe ser un numero entero"
    assert resultado == -1, "El resultado para el valor negativo debe ser -1"
    
def test_signo_cero():
    '''
    Prueba de la funcion signo() para el valor cero. 
    '''
    numero = 0
    resultado = signo(numero)
    assert isinstance(resultado, int), "El resultado debe ser un numero entero"
    assert resultado == 0, "El resultado para el valor neutro debe ser 0"


    
