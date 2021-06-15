################
# Katherina Soto - @ktyfer
# Plantilla tp4ej5
# UNRN Andina - Introducción a la Ingenieria en Computación
################


#numeros positivos y negativos


def signo(numero):
    """Esta funcion me devuelve si u
el numero ingresado es positivo o negativo"""
    
    if numero < 0:
        
        return ('negativo')
     
       
    elif numero > 0:
        
        return ('positivo')
        
    else:
        
        return ('cero')
    
    

def prueba():
    numero = int(input('Ingrese un numero: '))
    valor_ingresado = signo(numero)
    
    print (f'El signo del numero ingresado es {signo(numero)}')
    
    
if __name__ == "__main__":
    prueba()