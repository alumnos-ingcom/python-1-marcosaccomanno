################
# Marco Saccomanno - @marcosaccomanno
# UNRN Andina - Introducción a la Ingenieria en Computación
################

'''
Precondiciones: Los valores de entrada deben ser tres numeros enteros.

Poscondiciones: La salida debe ser una tupla con los tres valores ordenados
de mayor a menor y de menor a mayor.
'''

def ordenar_mayor_a_menor(uno, dos, tres):
    '''
    Esta funcion toma como entrada tres numeros y retorna una
    tupla con los tres numeros ordenados de mayor a menor
    '''
    if uno > dos:
        if dos > tres:
            numeros_ordenados = (uno, dos, tres)
        elif tres > dos:
            numeros_ordenados = (uno, tres, dos)
    elif dos > uno:
        if uno > tres:
            numeros_ordenados = (dos, uno, tres)
        elif tres > uno:
            numeros_ordenados = (dos, tres, uno)
    elif tres > uno:
        if uno > dos:
            numeros_ordenados = (tres, uno, dos)
        elif dos > uno:
            numeros_ordenados = (tres, dos, uno)
    return numeros_ordenados
    
def ordenar_menor_a_mayor(uno, dos, tres):
    '''
    Esta funcion toma como entrada tres numeros y retorna una
    tupla con los tres numeros ordenados de menor a mayor
    '''
    if uno > dos:
        if dos > tres:
            numeros_ordenados = (tres, dos, uno)
        elif tres > dos:
            numeros_ordenados = (dos, tres, uno)
    elif dos > uno:
        if uno > tres:
            numeros_ordenados = (tres, uno, dos)
        elif tres > uno:
            numeros_ordenados = (uno, tres, dos)
    elif tres > uno:
        if uno > dos:
            numeros_ordenados = (dos, uno, tres)
        elif dos > uno:
            numeros_ordenados = (uno, dos, tres)
    return numeros_ordenados

def principal():
    '''
    Funcion principal
    '''
    # Entrada
    uno = int(input("Numero uno: "))
    dos = int(input("Numero dos: "))
    tres = int(input("Numero tres: "))
    # Algoritmo
    mayor_a_menor = ordenar_mayor_a_menor(uno, dos, tres)
    menor_a_mayor = ordenar_menor_a_mayor(uno, dos, tres)
    # Salida
    print(mayor_a_menor)
    print(menor_a_mayor)

if __name__ == "__main__":
    principal()
