################
# Marco Saccomanno - @marcosaccomanno
# UNRN Andina - Introducción a la Ingenieria en Computación
################

'''
Precondiciones: La entrada debe ser un numero natural.

Poscondiciones: La salida debe ser un numero natural o una tupla de numeros
naturales.
'''

def sexadecimal_a_decimal(horas, minutos, segundos):
    '''
    Esta funcion toma como entrada horas, minutos y segundos y los convierte
    a segundos.
    '''
    horas_a_segundos = horas * 60 * 60
    minutos_a_segundos = minutos * 60
    total_segundos = horas_a_segundos + minutos_a_segundos + segundos
    return total_segundos

def decimal_a_sexadecimal(numero):
    '''
    Esta funcion toma como entrada un numero (segundos) y lo convierte
    a horas, minutos y segundos.
    '''
    horas_convertidas = int(numero / 60 / 60)
    numero -= horas_convertidas * 60 * 60
    minutos_convertidos = int(numero / 60)
    numero -= minutos_convertidos * 60
    return(horas_convertidas, minutos_convertidos, numero)

def principal():
    '''
    Funcion principal
    '''
    # Entrada
    horas = int(input("Horas: "))
    minutos = int(input("Minutos: "))
    segundos = int(input("Segundos: "))
    numero = int(input("Segundos (para convertir a horas, minutos y segundos): "))
    # Algoritmo
    segundos_convertidos = sexadecimal_a_decimal(horas, minutos, segundos)
    numero_convertido = decimal_a_sexadecimal(numero)
    # Salida
    print(f"Segundos: {segundos_convertidos}")
    print(f"Horas/Minutos/Segundos: {numero_convertido}")
    
if __name__ == "__main__":
    principal()