################
# Marco Saccomanno - @marcosaccomanno
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from src.ejercicio4 import suma_lenta

'''
Los siguientes tests se encargan de probar las funciones del archivo 'ejercicio4.py'
ubicado en 'src'.
'''

def test_suma_lenta():
    numero = 5
    otro_numero = 7
    resultado = suma_lenta(numero, otro_numero)
    assert isinstance(resultado, int), "El resultado debe ser un numero entero"
    assert resultado == 12, "Para 5 + 7 el resultado debe ser 12"
    
test_suma_lenta()