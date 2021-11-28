#LIBRERIAS USADAS:
from pyrecord import Record
import os 

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
