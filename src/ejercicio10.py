################
# Marco Saccomanno - @marcosaccomanno
# UNRN Andina - Introducción a la Ingenieria en Computación
################

'''
Precondiciones: La entrada debe ser de tipo string.

Poscondiciones: La salida debe ser un valor booleano (True o False).
'''

def es_palindromo(texto):
    '''
    Esta funcion toma como entrada texto_plano que retorna la funcion aplanar_texto().
    Recorre cada letra de la cadena y la agrega de atras hacia adelante a la variable
    texto_comparado. Por ultimo hace la comparacion con el texto original y determina
    si es o no es un palindromo.
    '''
    indice = 0
    texto_plano = texto.lower().replace(" ", "")
    texto_comparado = ""
    largo = len(texto)
    while largo > 0:
        texto_comparado += texto_plano[indice - 1]
        indice -= 1
        largo -=1
        
    if texto_comparado == texto_plano:
        respuesta = True
    else:
        respuesta = False
    return respuesta
         
def principal():
    '''Funcion principal'''
    # entrada
    texto_ingresado = input("Texto: ")
    # algoritmo
    resultado = es_palindromo(texto_ingresado)
    # salida
    print(resultado)
    
if __name__ == "__main__":
    principal()
    