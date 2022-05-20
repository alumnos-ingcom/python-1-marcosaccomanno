################
# Marco Saccomanno - @marcosaccomanno
# UNRN Andina - Introducción a la Ingenieria en Computación
################


def convertir_a_fahrenheit(centigrados):
    
    '''
    Esta funcion toma como entrada una temperatura
    en grados centigrados y lo convierte a grados fahrenheit.
    Se espera como entrada un numero decimal y la salida
    esperada es tambien un numero decimal.
    '''
    
    return centigrados * 1.80 + 32
    

def convertir_a_centigrados(fahrenheit):
    
    '''
    Esta funcion toma como entrada una temperatura
    en grados fahrenheit y lo convierte a grados centigrados.
    Se espera como entrada un numero decimal y la salida
     esperada es tambien un numero decimal.
    '''

    return (fahrenheit - 32) / 1.80


def principal():
    
    # entrada
    
    centigrados = float(input("Centigrados: "))
    fahrenheit = float(input("Fahrenheit: "))
    
    # algoritmo

    fahrenheit_convertido = convertir_a_fahrenheit(centigrados)
    
    centigrados_convertido = convertir_a_centigrados(fahrenheit)
    
    # salida
    
    print(f"{centigrados} °C son {fahrenheit_convertido:.2f} °F")

    print(f"{fahrenheit} °F son {centigrados_convertido:.2f} °C")
    

if __name__ == "__main__":
    principal()