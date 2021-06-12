################
# Katherina Soto - @ktyfer
# Plantilla tp4ej3
# UNRN Andina - Introducción a la Ingenieria en Computación
################

# conversion de temperaturas

def convertir_a_fahrenheit(centigrados):
    
    return ((centigrados *9/5) + 32)
'''convierte a grados fahrenheit'''   
        
    
def convertir_a_centigrados(fahrenheit):
    
    return ((fahrenheit - 32) * 5/9)
  '''convierte a grados centigrados'''  
    

def prueba():
    centigrados = float(input('ingrese grados fahrenheit # '))
    valor1 = convertir_a_fahrenheit(centigrados)
    
    fahrenheit = int(input('ingrese grados centigrados # '))
    valor2 = convertir_a_centigrados(fahrenheit)
   
    print (f'El resultado en centigrados es: {valor1} \nEl resultado en fahrenheit es :{valor2}')
    

if __name__ == "__main__":
    prueba()