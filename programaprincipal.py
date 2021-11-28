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


def altacuentas(vector_cuentas, cuentashabiles):

    #ESTA FUNCION ME PERMITIRA DAR DE ALTA UNA CUENTA SI Y SOLO SI EL DNI INGRESADO NO ESTA REGISTRADO. 

    #PRIMERO CORROBORO SI EL DNI INGRESADO TIENE UNA CUENTA ACTIVA EN EL BANCO
    documento = input("Ingrese su DNI(sin puntos): ")
    seguir = True

    #Recorro todo el vector buscando si ya posee una cuenta activa en el banco. 
    for i in range(0,cuentashabiles):

        if (vector_cuentas[i].dni == documento) and (vector_cuentas[i].estado == True):

            print("Usted ya posee una cuenta activa en el banco. ")
            #SI POSEE UNA CUENTA ACTIVA EN EL BANCO SE LE INFORMARA, Y NO SE PODRA REGISTRAR
            
            seguir = False
    
    #SI NO POSEE UNA CUENTA SE CONTINUARA CON EL REGISTRO. 
    if seguir == True:

        cuentashabiles += 1 #Crece la cantidad de cuentas habiles
        vector_cuentas[cuentashabiles].numero = cuentashabiles + 1000 #Creo el numero de cuenta. 
        vector_cuentas[cuentashabiles].apellido = input("Ingrese su apellido: ")
        vector_cuentas[cuentashabiles].nombre = input("Ingrese su nombre: ")
        vector_cuentas[cuentashabiles].dni = documento
        vector_cuentas[cuentashabiles].tipocuenta = int(input("Ingrese el tipo de cuenta: "))
        vector_cuentas[cuentashabiles].estado = True 
        #El saldo no se modifica ya que este se lo hara cuando se realice una transaccion.

        #LE INFORMO AL USUARIO SU NUMERO DE CUENTA:
        print(f"Gracias por elegirnos {vector_cuentas[cuentashabiles].nombre}, su numero de cuenta es: {vector_cuentas[cuentashabiles].numero} ")

    return vector_cuentas, cuentashabiles
        
def modificacioncuentas(vector_cuentas, cuentashabiles):


    print(" "*10, "1- Si desea cambiar su DNI.")
    print(" "*10, "2- Si desea cambiar su apellido.")
    print(" "*10, "3- Si desea cambiar su nombre.")
    print(" "*10, "4- Si desea cambiar su tipo de cuenta.")
    decision = int(input("Ingrese el cambio que desee realizar: "))
    os.system("cls")
    numerocuenta = int(input("Ingrese el numero de su cuenta: "))
    seguir = True

    for i in range(0,cuentashabiles):

        if (vector_cuentas[i].numero == numerocuenta) and (vector_cuentas[i].estado == True):

            seguir = True

    if seguir == True:

        if decision == 1:

            vector_cuentas[numerocuenta-1000].dni = input("Ingrese su nuevo DNI: ")
            print(vector_cuentas[numerocuenta-1000].dni)
        
        if decision == 2:

            vector_cuentas[numerocuenta-1000].apellido = input("Ingrese su nuevo apellido: ")
        
        if decision  == 3:

            vector_cuentas[numerocuenta-1000].nombre = input("Ingrese su nuevo nombre: ")

        if decision == 4:

            vector_cuentas[numerocuenta-1000].tipocuenta = int(input("Ingrese el nuevo tipo de cuenta: "))
    
    return vector_cuentas




def ABMcuentas(vector_cuentas, cuentashabiles):

    #ESTA FUNCION REALIZA ALTAS, BAJAS Y MODIFICACIONES DE LAS CUENTAS. 

    #MENU PARA ELEJIR QUE DESEA HACER EL USUARIO:
    print(" "*10, "1- Si desea dar de alta una nueva cuenta.")
    print(" "*10, "2- Si desea dar de baja una cuenta.")
    print(" "*10, "3- Si desea realizar una modificacion en su cuenta.")
    print(" "*10, "4- Si desea salir al menu principal.")
    decision = int(input("Ingrese una opción: "))
    os.system("cls")

    #Inicio de ciclo del menu:
    while decision != 4:

        if decision == 1:

            #DOY DE ALTA UNA CUENTA NUEVA: 
            vector_cuentas, cuentashabiles = altacuentas(vector_cuentas, cuentashabiles)
           

        elif decision == 2:
            
            #DOY DE BAJA UNA CUENTA: 
            cuentabaja = int(input(f"Ingrese el numero de la cuenta que desea darle de baja (entre 1.000 y {1000+cuentashabiles}): "))
            vector_cuentas[cuentabaja-1000].estado = False 
            os.system("cls")
            print(f"LA CUENTA {cuentabaja} SE HA DADO DE BAJA")
        
        elif decision == 3:
            
            #CAMBIO ALGUN DATO DE LA CUENTA: 
            vector_cuentas = modificacioncuentas(vector_cuentas, cuentashabiles)
        
        #VUELVO A MOSTRAR PARA SABER SI QUIERE SALIR O REALIZAR OTRA OPERACION: 
        input("Presione enter para continuar...")
        os.system("cls")
        print(" "*10, "1- Si desea dar de alta una nueva cuenta.")
        print(" "*10, "2- Si desea dar de baja una cuenta.")
        print(" "*10, "3- Si desea realizar una modificacion en su cuenta.")
        print(" "*10, "4- Si desea salir al menu principal.")
        decision = int(input("Ingrese una opción: "))
    
    return vector_cuentas, cuentashabiles



vector, cuentashabiles = cargadatos()
print(vector[599].nombre)