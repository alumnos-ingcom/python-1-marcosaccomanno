################
# Marco Saccomanno - @marcosaccomanno
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from src.ejercicio6 import ordenar_mayor_a_menor, ordenar_menor_a_mayor

'''
Los siguientes tests se encargan de probar las funciones del archivo 'ejercicio5.py'
ubicado en 'src'.
'''

def test_ordenar_mayor_a_menor():
    '''
    Prueba de la funcion ordenar_mayor_a_menor()
    '''
    uno = 7
    dos = 8
    tres = 2
    resultado = ordenar_mayor_a_menor(uno, dos, tres)
    assert isinstance(resultado, tuple), "La salida debe ser una tupla"
    assert resultado == (dos, uno, tres), "Para los numeros 7, 8 y 2 la salida debe ser (8, 7, 2)"
    
def test_ordenar_menor_a_mayor():
    '''
    Prueba de la funcion ordenar_menor_a_mayor()
    '''
    uno = 7
    dos = 8
    tres = 2
    resultado = ordenar_menor_a_menor(uno, dos, tres)
    assert isinstance(resultado, tuple), "La salida debe ser una tupla"
    assert resultado == (tres, uno, dos), "Para los numeros 7, 8 y 2 la salida debe ser (2, 7, 8)"
    