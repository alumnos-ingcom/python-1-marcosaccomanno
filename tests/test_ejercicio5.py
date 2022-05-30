################
# Marco Saccomanno - @marcosaccomanno
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from ejercicio5 import division_lenta

'''
Los siguientes tests se encargan de probar las funciones del archivo 'ejercicio5.py'
ubicado en 'src'.
'''

def test_division_lenta():
    '''
    Esta funcion prueba la division lenta entre dos numeros.
    '''
    dividendo = 12
    divisor = 2
    resultado = division_lenta(dividendo, divisor)
    assert isinstance(resultado, tuple), "La salida debe ser una tupla con el cociente y el resto"
    assert resultado == (6, 0), "Para dividendo 12 y divisor 2, el cociente debe ser 6 y el resto 0"
