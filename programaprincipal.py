#LIBRERIAS USADAS:
from pyrecord import Record
import os

def cargadatos():

    #ESTA FUNCION BUSCARA CARGAR LOS DATOS QUE SE ENCUENTRAN EN EL ARCHIVO A UN VECTOR DE REGISTROS
    #CADA CUENTA TENDRA UN REGISTRO; COMPUESTO POR: (NRO CUENTA, APELLIDO, NOMBRE, DNI, TIPO DE CUENTA, SALDO, ESTADO)
    #TAMBIEN DEVUELVE EL NUMERO DE CUENTAS HABILES CARGADAS EN EL VECTOR_CUENTAS

    archivocuentas = open("cuentas.txt", "r")

    #Creo el registro que contendra las cuentas:
    cuenta = Record.create_type("cuenta", "numero", "apellido", "nombre", "dni", "tipocuenta", "saldo", "estado", 
                numero = 0, apellido = " ", nombre = " ", dni = " ", tipocuenta = 0, saldo = 0.0, estado = " ")
    
    #creo el vector de cuentas sobredimensionado:
    vector_cuentas = [cuenta]* 1000
    vector_cuentas[0] = cuenta()

    #CARGO LOS DATOS AL VECTOR: 

    #Leo una linea para entrar al ciclo e inicializo el indice:
    indice = 0
    linea = archivocuentas.readline().strip().split(",")

    while len(linea) == 7:

        vector_cuentas[indice] = cuenta()
        vector_cuentas[indice].numero = int(linea[0])
        vector_cuentas[indice].apellido = linea[1]
        vector_cuentas[indice].nombre = linea[2]
        vector_cuentas[indice].dni = linea[3]
        vector_cuentas[indice].tipocuenta = int(linea[4])
        vector_cuentas[indice].saldo = float(linea[5])
        vector_cuentas[indice].estado = bool(linea[6])

        #Leo otra linea e incremento indice:
        linea = archivocuentas.readline().strip().split(",")
        indice += 1
    
    
    
    #El indice me dara la cantidad de cuentas que tengo cargadas en el vector:
    cuentashabiles = indice

    #Cierro el archivo:
    archivocuentas.close()
    

    #RETORNO LAS CUENTAS, Y LA CANTIDAD DE CUENTAS HABILES:

    return vector_cuentas, cuentashabiles

def consultacuenta(vector_cuentas, cuentashabiles):

    #ESTA FUNCION AL LLAMARLA ME PERMITE CONSULTAR EL SALDO DE LA CUENTA DESEADA(INGRESANDOSE EL NUMERO DE LA MISMA POR TECLADO)

    #PIDO NUMERO DE CUENTA QUE SE DESEA CONSULTAR:
    cuenta = int(input(f"Ingrese el numero de la cuenta que desea consultar(entre 1.000 y {cuentashabiles+1000}): "))
    direccion = cuenta - 1000   #LO DECREMENTO EN 1.000 PARA OBTENER LA POSICION DE LA CUENTA EN EL VECTOR_CUENTAS.

   #BUSCO LA CUENTA EN EL VECTOR DE CUENTAS: 
    saldo = vector_cuentas[direccion].saldo

    #Limpio pantalla:
    os.system("cls")

    #INFORMO POR PANTALLA:
    print(" "*20, f"CUENTA NUMERO: {cuenta}")
    print(" "*20, f"SALDO: {round(saldo, 2)}") #Uso round para que me muestre solo dos decimales luego de la coma. 

    #Muestro espacios en blanco para bajar el simbolo del sistema:
    print()
    print()
    print()

    return 


