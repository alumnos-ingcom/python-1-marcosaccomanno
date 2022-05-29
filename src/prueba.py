def conversion_peso_sol(pesos):
    '''
    Esta funcion convierte una cantidad de pesos argentinos a soles peruanos.
    '''
    return pesos * 0.041929412

def conversion_sol_peso(soles):
    '''
    Esta funcion convierte una cantidad de soles peruanos a pesos argentinos.
    '''
    return soles / 0.041929412    

def saldo():
    saldo_soles = conversion_peso_sol(SALDO)
    saldo_pesos = conversion_sol_peso(SALDO)
    print(f"Saldo en Pesos: {saldo_pesos:.2f}")
    print(f"Saldo en Soles: {saldo_soles:.2f}")
 
SALDO = 1000
    
saldo()