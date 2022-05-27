################
# Marco Saccomanno - @marcosaccomanno
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from src.ejercicio1 import convertir_a_fahrenheit, convertir_a_centigrados

'''
Los siguientes tests se encargan de probar las funciones del archivo 'ejercicio1.py'
ubicado en 'src'.
'''

def test_convertir_a_fahrenheit():
    '''
    Esta funcion prueba la conversion de centigrados a fahrenheit.
    '''
    centigrados = 18.2
    resultado = convertir_a_fahrenheit(centigrados)
    assert isinstance(resultado, float), "El resultado debe ser un numero decimal"
    
def test_convertir_a_centigrados():
    '''
    Esta funcion prueba la conversion de fahrenheit a centigrados.
    '''
    fahrenheit = 18.2
    resultado = convertir_a_centigrados(fahrenheit)
    assert isinstance(resultado, float), "El resultado debe ser un numero decimal"
