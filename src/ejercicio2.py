################
# Marco Saccomanno - @marcosaccomanno
# UNRN Andina - Introducción a la Ingenieria en Computación
################

'''
Precondiciones: La entrada debe ser un numero real.

Poscondiciones: La salida es un numero entero 1, 0 o -1.
'''

def signo(numero):
    '''
    Esta funcion toma como entrada un numero real y devuelve
    el signo del mismo calculandolo mediante sumas (positivo, negativo o neutro).
    Si el numero es positivo retorna 1, si es negativo -1 y si es neutro 0.
    ''' 
    if numero + numero > numero:
        # si a un numero positivo se le suma ese mismo numero, siempre sera mayor que si mismo.
        sgn = 1
    elif numero + numero < numero:
        # si a un numero negativo se le suma ese mismo numero sera igual que hacer una resta, 
        # por lo tanto el resultado sera menor que si mismo.
        sgn = -1
    else:
        sgn = 0
    return sgn

def principal():
    ''' Funcion principal '''
    # entrada
    numero = float(input("Ingrese un numero: "))
    # algoritmo
    signo_numero = signo(numero)
    # salida
    print(signo_numero)
    
if __name__ == "__main__":
    principal()
    