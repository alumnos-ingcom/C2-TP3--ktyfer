################
# Katherina Soto - @ktyfer
# Plantilla tp4ej3
# UNRN Andina - Introducción a la Ingenieria en Computación
################

# conversion de temperaturas

  
def convertir_a_fahrenheit(centigrados):
    '''convierte a grados fahrenheit'''
    
    return ((centigrados *9/5) + 32)
    
     
        
   
def convertir_a_centigrados(fahrenheit):
    '''convierte a grados centigrados'''
    
    return ((fahrenheit - 32) * 5/9)
    
     
    

def prueba():
    centigrados = float(input('ingrese grados fahrenheit # '))
    valor1 = convertir_a_fahrenheit(centigrados)
    
    fahrenheit = int(input('ingrese grados centigrados # '))
    valor2 = convertir_a_centigrados(fahrenheit)
   
    print (f'El resultado en centigrados es: {valor1} \nEl resultado en fahrenheit es :{valor2}')
    

if __name__ == "__main__":
    prueba()