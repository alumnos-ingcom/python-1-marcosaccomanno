################
# Marco Saccomanno - @marcosaccomanno
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from src.ejercicio7 import sexadecimal_a_decimal, decimal_a_sexadecimal

'''
Los siguientes tests se encargan de probar las funciones del archivo 'ejercicio7.py'
ubicado en 'src'.
'''

def test_sexadecimal_a_decimal():
    '''
    Prueba de la conversion de horas, minutos y segundos a segundos
    '''
    horas = 4
    minutos = 45
    segundos = 23
    resultado = sexadecimal_a_decimal(horas, minutos, segundos)
    assert isinstance(resultado, int), "La salida debe ser un numero entero positivo"
    assert resultado == 17123, "Para 4 horas, 45 minutos y 23 segundos la salida debe ser 17123"
    
def test_decimal_a_sexadecimal():
    '''
    Prueba de la conversion de un numero a horas, minutos y segundos
    '''
    numero = 4620
    resultado = decimal_a_sexadecimal(numero)
    assert isinstance(resultado, tuple), "La salida debe ser una tupla"
    assert resultado == (1, 17, 0), "Para 4620 segundos la salida debe ser (1, 17, 0)"
