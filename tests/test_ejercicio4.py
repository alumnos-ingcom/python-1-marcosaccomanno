################
# Marco Saccomanno - @marcosaccomanno
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from src.ejercicio4 import suma_lenta

'''
Los siguientes tests se encargan de probar las funciones del archivo 'ejercicio4.py'
ubicado en 'src'.
'''

def test_suma_lenta_pos_pos():
    '''
    Prueba la suma lenta con los dos numeros positivos
    '''
    numero = 5
    otro_numero = 7
    resultado = suma_lenta(numero, otro_numero)
    assert isinstance(resultado, int), "El resultado debe ser un numero entero"
    assert resultado == 12, "Para 5 + 7 el resultado debe ser 12"
    
def test_suma_lenta_pos_neg():
    '''
    Prueba la suma lenta con el primer numero positivo y el segundo negativo
    '''
    numero = 5
    otro_numero = -2
    resultado = suma_lenta(numero, otro_numero)
    assert isinstance(resultado, int), "El resultado debe ser un numero entero"
    assert resultado == 3, "Para 5 + (-2) el resultado debe ser 3"
    
def test_suma_lenta_neg_pos():
    '''
    Prueba la suma lenta con el primer numero negativo y el segundo positivo
    '''
    numero = -2
    otro_numero = 8
    resultado = suma_lenta(numero, otro_numero)
    assert isinstance(resultado, int), "El resultado debe ser un numero entero"
    assert resultado == 6, "Para -2 + 8 el resultado debe ser 6"
    
def test_suma_lenta_neg_neg():
    '''
    Prueba la suma lenta con los dos numeros negativos
    '''
    numero = -3
    otro_numero = -4
    resultado = suma_lenta(numero, otro_numero)
    assert isinstance(resultado, int), "El resultado debe ser un numero entero"
    assert resultado == -7, "Para -3 + (-4) el resultado debe ser -7"
