################
# Katherina Soto - @ktyfer
# Plantilla tp4ej5
# UNRN Andina - Introducción a la Ingenieria en Computación
################

#comparacion de numeros

'''Esta funcion me dice si el numero 1 es menor que numero2'''

def compara(num1, num2):
    if num1 < num2:
        return ('-1')
    
    elif num1 > num2:
        return ('+1')
    
    else:
        return ('0')
    

def prueba():
    num1 = int(input('Ingrese un numero: '))
    num2  = int(input('ingrese un numero: '))
    num_ingresado = compara(num1, num2)
    print (f'La comparacion de numeros es: {compara(num1, num2)}')
    

if __name__ == "__main__":
    prueba()

