# En este script voy a poner un par de funciones y metodos utiles cuando se trabaja en general.
import os, random

# A continuacion, algunas funciones utiles para usar en un menu.

# Esta simple funcion permite mostrar el mensaje " Presione Enter para continuar..." aisaldo y centrado en la pantalla luego de 
# realizar una operacion e indicar previamente que se realizo satisfactoriamente. Sirve mas que nada para informar cosas al usuario
# antes de pasar a la siguiente operacion.
def pausa():
    print()
    print(" "*20,end=" ") # Fijate como ponemos "*20" para multiplicar los espacios vacios.
    input(" Presione Enter para continuar...")

# Esta funcion es la misma mierda que la anterior, solo que personalizada y no espera q el usuario presione enter para continuar 
# ejecutando el programa. Esta funcion deberia trabajaren conjunto con la anterior (primero iria esta y luego la otra)
def mensaje(m):
    print()
    print(" "*20,m+'...')

#  Esta funcion sirve para limpiar la pantalla.
def limpiar_pantalla():
    if (os.name)=='posix':
        os.system('clear')
    if (os.name)=='nt':
        os.system('cls')
    return None

# El modulo "os" (importado previamente) junto con el metodo "name" nos permite detectar el "nombre" del sistema operativo. Si el 
# nombre es "posix", el sistema operativo es Linux y el comando de limpieza de pantalla es: os.system('clear'). Si el 
# nombre es "nt", el sistema operativo es Windows y el comando de limpieza de pantalla es: os.system('cls').
    
# Esta funcion es simplemente para validar
def elegir(ultimo):
    print()
    print(" "*22,end=" ")
    opc=int(input(" Elija una opción: "))
    while((opc>ultimo) or (opc<0)):
        print(" "*20,"Lo siento, la Opción es inválida")
        print(" "*22,end=" ")
        opc=int(input(" Elija una opción: "))
    return opc


# Vamos con otros codigos utiles. 

# Con esta sentencia podemos obtener un numero fraccionario aleatorio.

variable =random.randint(0,10) + random.random() 

# randint vendria a ser un metodo similar a rangrange (de hecho, aun no encuentro la diferencia) y devuelve un numero entero
# aleatorio seleccionado de un rango. random vendria a ser un metodo para generar un numero fracionario aleatorio entre 0 y 1.



# Esta es una forma de diseñar en forma sofisticada los mensajes que aparecen en pantalla. Para ello debemos escribir todo como esta
# y luego ponemos entre llaves cada uno de los datos que queremos que aparezcan. Si queremos diseñar la impresion ponemos ":" , luego
# una flecha que indique la alineacion "< o >", luego la cantidad de lugares o espacios que queremos que ocupe el mesnaje. En el caso
# que queramos imprimir un numero con parte fraccionaria, podemos indicar con ".numf" la cantidad de digitos fraccionarios q deseamos 
# imprimir.

# print(f'{"hola":<12} {"papa":>4}     {variable:<12} {"papaaa":>12.2f}')



# Podemos usar el metodo choice de la libreria random para escoger en forma aleatoria un elemento dentro de una lista definida previa
# mente.

nombre=['Juan','Maria','Pedro','Claudia','Belen','Veronica','Nahuel','Nicolas']

nom=random.choice(nombre)
