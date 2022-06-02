################
# Marco Saccomanno - @marcosaccomanno
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from src.ejercicio11 import es_multiplo

'''
Los siguientes tests se encargan de probar las funciones del archivo 'ejercicio11.py'
ubicado en 'src'.
'''

def test_es_multiplo_true():
    '''
    Prueba de la funcion es_multiplo() para un resultado True
    '''
    numero = 10
    multiplo = 5
    resultado = es_multiplo(numero, multiplo)
    assert isinstance(resultado, bool), "La salida debe ser un valor booleano"
    assert resultado is True, "Para numeros que sean multiplos, la salida debe ser True"
    
def test_es_multiplo_false():
    '''
    Prueba de la funcion es_multiplo() para un resultado False
    '''
    numero = 10
    multiplo = 3
    resultado = es_multiplo(numero, multiplo)
    assert isinstance(resultado, bool), "La salida debe ser un valor booleano"
    assert resultado is False, "Para numeros que sean multiplos, la salida debe ser False"
    