################
# Marco Saccomanno - @marcosaccomanno
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from src.ejercicio10 import es_palindromo

'''
Los siguientes tests se encargan de probar las funciones del archivo 'ejercicio10.py'
ubicado en 'src'.
'''

def test_es_palindromo_true():
    '''
    Prueba de la funcion es_palindromo() para un texto que es palindromo.
    '''
    texto = "neuquen"
    resultado = es_palindromo(texto)
    assert isinstance(resultado, bool), "El resultado debe ser un valor booleano"
    assert resultado is True, "Si el texto es palindromo el resultado debe ser True"
    
def test_es_palindromo_false():
    '''
    Prueba de la funcion es_palindromo() para un texto que no es palindromo.
    '''
    texto = "camion"
    resultado = es_palindromo(texto)
    assert isinstance(resultado, bool), "El resultado debe ser un valor booleano"
    assert resultado is False, "Si el texto no es palindromo el resultado debe ser False"    
    