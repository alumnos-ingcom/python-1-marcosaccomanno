################
# Marco Saccomanno - @marcosaccomanno
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def es_primo(numero):
    if numero == 1 or numero == 2:
        resultado = True
    else:
        for i in range(2, numero):
            if numero % i == 0:
                resultado = False
                break
            resultado = True
    return resultado

def principal():
    numero = int(input("Numero: "))
    res = es_primo(numero)
    print(res)
    
if __name__ == "__main__":
    principal()

       


        
        