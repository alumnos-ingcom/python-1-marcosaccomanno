################
# Marco Saccomanno - @marcosaccomanno
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from src.ejercicio3 import compara

'''
Los siguientes tests se encargan de probar las funciones del archivo 'ejercicio3.py'
ubicado en 'src'.
'''

def test_compara_menor():
    '''
    Prueba de la funcion compara() para un primer valor menor que el segundo valor.
    '''
    numero = 3
    otro_numero = 12
    resultado = compara(numero, otro_numero)
    assert isinstance(resultado, int), "El resultado debe ser un numero entero"
    assert resultado == -1, "El resultado para un primer valor menor que el segundo debe ser -1"
    
def test_compara_mayor():
    '''
    Prueba de la funcion compara() para un primer valor mayor que el segundo valor.
    '''
    numero = 12
    otro_numero = 3
    resultado = compara(numero, otro_numero)
    assert isinstance(resultado, int), "El resultado debe ser un numero entero"
    assert resultado == 1, "El resultado para un primer valor mayor que el segundo debe ser 1"
    
def test_compara_igual():
    '''
    Prueba de la funcion compara() para un primer valor igual que el segundo valor.
    '''
    numero = 3
    otro_numero = 3
    resultado = compara(numero, otro_numero)
    assert isinstance(resultado, int), "El resultado debe ser un numero entero"
    assert resultado == 0, "El resultado para un primer valor igual que el segundo debe ser 0"
    