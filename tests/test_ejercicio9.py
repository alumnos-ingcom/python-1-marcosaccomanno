################
# Marco Saccomanno - @marcosaccomanno
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from src.ejercicio9 import factores_primos

'''
Los siguientes tests se encargan de probar las funciones del archivo 'ejercicio9.py'
ubicado en 'src'.
'''

def test_factores_primos():
    '''
    Prueba de la funcion factores_primos()
    '''
    numero = 84
    resultado = factores_primos(numero)
    assert isinstance(resultado, tuple), "El resultado debe ser una tupla"
    assert resultado == (2, 3, 7), "Para el numero 84 la salida debe ser (2, 3, 7)"
    