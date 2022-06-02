################
# Marco Saccomanno - @marcosaccomanno
# UNRN Andina - Introducción a la Ingenieria en Computación
################

'''
Precondiciones: La entrada deben ser dos numeros enteros. El segundo numero debe
ser distinto de 0.

Poscondiciones: La salida es una tupla con (Cociente, Resto). Si el divisor es 0
la salida es None.

* De momento este programa NO funciona con numeros negativos.
'''

def division_lenta(dividendo, divisor):
    '''
    Esta funcion toma como entrada dos numeros enteros y realiza
    la division de ambos mediante restas. Retorna el cociente y
    el resto
    '''
    while divisor != 0:
        cociente = 0
        while dividendo > 1:
            dividendo -= divisor
            cociente += 1
            resto = dividendo
        return cociente, resto
        
def principal():
    '''
    Funcion principal
    '''
    # Entrada
    dividendo = int(input("Dividendo: "))
    divisor = int(input("Divisor: "))
    # Algoritmo
    resultado = division_lenta(dividendo, divisor)
    # Salida
    print(resultado)
   
if __name__ == "__main__":
    principal()
    