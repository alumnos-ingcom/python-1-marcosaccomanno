################
# Marco Saccomanno - @marcosaccomanno
# UNRN Andina - Introducción a la Ingenieria en Computación
################

'''
Precondiciones: La entrada debe ser un numero real.

Poscondiciones: La salida es un string "neutro", "positivo" o "negativo".
'''

def signo(numero):
    '''
    Esta funcion toma como entrada un numero real y devuelve
    el signo del mismo calculandolo mediante sumas (positivo, negativo o neutro). 
    ''' 
    if numero + numero == numero:
        # si un numero es 0 y se le suma ese mismo numero, el resultado siempre sera 0.
        return "neutro"
    elif numero + numero > numero:
        # si a un numero positivo se le suma ese mismo numero, siempre sera mayor que si mismo.
        return "positivo"
    elif numero + numero < numero:
        # si a un numero negativo se le suma ese mismo numero sera igual que hacer una resta, 
        # por lo tanto el resultado sera menor que si mismo.
        return "negativo"

def principal():
    ''' Funcion principal '''
    # entrada
    numero = float(input("Ingrese un numero: "))
    
    # algoritmo
    signo_numero = signo(numero)

    # salida
    print(f"{numero} es {signo_numero}")
    
if __name__ == "__main__":
    principal()
    