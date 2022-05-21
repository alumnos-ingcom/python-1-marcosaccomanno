################
# Marco Saccomanno - @marcosaccomanno
# UNRN Andina - Introducción a la Ingenieria en Computación
################

'''
Precondiciones: La entrada debe ser de tipo string.

Poscondiciones: La salida sera un string "es palindromo" o "no es palindromo".
'''

def aplanar_texto(texto):
    '''
    Esta funcion toma como entrada una cadena, la convierte a minuscula y elimina los espacios.
    '''
    return texto.lower().replace(" ", "")

def es_palindromo(texto, texto_plano):
    '''
    Esta funcion toma como entrada texto_plano que retorna la funcion aplanar_texto().
    Recorre cada letra de la cadena y la agrega de atras hacia adelante a la variable
    texto_comparado. Por ultimo hace la comparacion con el texto original y determina
    si es o no es un palindromo.
    '''
    indice = 0
    texto_comparado = ""
    for letra in texto:
        texto_comparado += texto_plano[indice - 1]
        indice -= 1
        
    if texto_comparado == texto_plano:
        return "es palindromo"
    else:
        return "no es palindromo"
         
def principal():
    # entrada
    ''' Se solicita al usuario el ingreso de una palabra o frase '''
    texto_ingresado = input("Texto: ")
    
    # algoritmo
    ''' Se aplana el texto y se verifica si es palindromo '''
    texto_plano = aplanar_texto(texto_ingresado)
    resultado = es_palindromo(texto_ingresado, texto_plano)
    
    # salida
    ''' Se imrpime si es o no es palindromo '''
    print(f"'{texto_ingresado}' {resultado}.")
    
if __name__ == "__main__":
    principal()