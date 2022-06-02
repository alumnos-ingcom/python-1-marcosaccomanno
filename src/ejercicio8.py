################
# Marco Saccomanno - @marcosaccomanno
# UNRN Andina - Introducción a la Ingenieria en Computación
################

'''
Precondiciones: La entrada debe ser un numero entero positivo.

Poscondiciones: La salida debe ser un valor booleano True (en caso de
que el numero sea primo) o False (en caso de que no lo sea).
'''

def es_primo(numero):
    '''
    Esta funcion recibe como entrada un numero y devuelve True
    en caso de que sea primo y False en caso de que no lo sea.
    '''
    divisor = 2
    if numero in (1, 2):
        resultado = True
    while divisor < numero:
        if numero % divisor == 0:
            resultado = False
            break
        divisor += 1
        resultado = True
    return resultado
    
def principal():
    '''
    Funcion principal
    '''
    # Entrada
    numero = int(input("Numero: "))
    # Algoritmo
    resultado = es_primo(numero)
    # Salida
    print(resultado)
    
if __name__ == "__main__":
    principal()
    