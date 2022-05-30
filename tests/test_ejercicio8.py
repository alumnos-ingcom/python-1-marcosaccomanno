################
# Marco Saccomanno - @marcosaccomanno
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from src.ejercicio8 import es_primo

'''
Los siguientes tests se encargan de probar las funciones del archivo 'ejercicio8.py'
ubicado en 'src'.
'''

def test_es_primo_true():
    '''
    Prueba de la funcion es_primo() para numeros que SI son primos.
    '''
    numero = 3
    resultado = es_primo(numero)
    assert isinstance(resultado, bool), "La salida debe ser un valor booleano"
    assert resultado is True, "Para un numero primo la salida debe ser True"
    
def test_es_primo_false():
    '''
    Prueba de la funcion es_primo() para numeros que NO son primos.
    '''
    numero = 4
    resultado = es_primo(numero)
    assert isinstance(resultado, bool), "La salida debe ser un valor bool"
    assert resultado is False, "Para un numero no primo la salida debe ser False"
    