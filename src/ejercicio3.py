################
# Marco Saccomanno - @marcosaccomanno
# UNRN Andina - Introducción a la Ingenieria en Computación
################

'''
Precondiciones: Los valores de entrada deben ser numeros reales.

Poscondiciones: La salida es un numero entero -1, 1 o 0.
'''

def compara(numero, otro_numero):
    '''
    Esta funcion toma como entrada dos numeros y mediante restas entre los dos numeros
    retorna:
    * -1 si el primero es menor que el segundo
    * 1 si el primero es mayor que el segundo
    * 0 si ambos son iguales
    '''
    if numero - otro_numero < 0:
        resultado = -1
    elif numero - otro_numero > 0:
        resultado = 1
    else:
        resultado = 0
    return resultado
        
def principal():
    ''' Funcion principal '''
    # entrada
    numero = float(input("Numero 1: "))
    otro_numero = float(input("Numero 2: "))
    # algoritmo
    comparacion = compara(numero, otro_numero)
    # salida
    print(comparacion)
        
if __name__ == "__main__":
    principal()
    