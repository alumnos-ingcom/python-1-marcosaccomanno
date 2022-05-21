################
# Marco Saccomanno - @marcosaccomanno
# UNRN Andina - Introducción a la Ingenieria en Computación
################

'''
Precondiciones: La entrada debe ser un numero real. Puede ser entero o decimal,
que represente una temperatura en grados centigrados o fahrenheit.

Poscondiciones: La salida debe ser tambien un numero real, resultado de la conversion
de centigrados a fahrenheit (°C * 1.80 + 32) o de fahrenheit a centigrados ((°F - 32) / 1.80).
'''


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
    ''' Se solicita al usuario el ingreso de una temperatura en grados centigrados y otra en grados fahrenheit. '''
    
    centigrados = float(input("Centigrados: "))
    fahrenheit = float(input("Fahrenheit: "))
                       
    # algoritmo
    ''' Se realiza la conversion de °C a °F y de °F a °C. '''
    
    fahrenheit_convertido = convertir_a_fahrenheit(centigrados) 
    centigrados_convertido = convertir_a_centigrados(fahrenheit)
    
    # salida
    ''' Se imprimen las temperaturas convertidas. '''
    
    print(f"{centigrados} °C son {fahrenheit_convertido:.2f} °F")
    print(f"{fahrenheit} °F son {centigrados_convertido:.2f} °C")
    

if __name__ == "__main__":
    principal()