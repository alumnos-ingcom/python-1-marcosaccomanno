################
# Marco Saccomanno - @marcosaccomanno
# UNRN Andina - Introducción a la Ingenieria en Computación
################

'''
Precondiciones: La entrada debe ser un numero entero positivo.

Postcondiciones: La salida debe ser un valor booleano True (en caso de
que el numero sea primo) o False (en caso de que no lo sea).
'''

def es_primo(numero):
    '''
    Esta funcion recibe como entrada un numero y devuelve True
    en caso de que sea primo y False en caso de que no lo sea.
    '''
    divisor = 2
    if numero in (1, 2):
        return True
    while divisor < numero:
        if numero % divisor == 0:
            return False
        divisor += 1
        return True

def principal():
    '''
    Funcion principal
    '''
    numero = int(input("Numero: "))
    print(es_primo(numero))
    
if __name__ == "__main__":
    principal()
    