#LIBRERIAS USADAS:
from pyrecord import Record
from random import *
import numpy as np
import os
from funciones_metodos_utiles_registros_archivos import *

# COMIENZA EL EJERCICIO #1

def cargadatos():

    #ESTA FUNCION BUSCARA CARGAR LOS DATOS QUE SE ENCUENTRAN EN EL ARCHIVO A UN VECTOR DE REGISTROS
    #CADA CUENTA TENDRA UN REGISTRO; COMPUESTO POR: (NRO CUENTA, APELLIDO, NOMBRE, DNI, TIPO DE CUENTA, SALDO, ESTADO)
    #TAMBIEN DEVUELVE EL NUMERO DE CUENTAS HABILES CARGADAS EN EL VECTOR_CUENTAS

    archivocuentas = open("cuentas.txt", "r")
    a2 = open("cajeros.txt","r")

    #Creo el registro que contendra las cuentas:
    cuenta = Record.create_type("cuenta", "numero", "apellido", "nombre", "dni", "tipocuenta", "saldo", "estado",
                                numero = 0, apellido = " ", nombre = " ", dni = " ", tipocuenta = 0, saldo = 0.0, estado = " ")
                        
    rcajero = Record.create_type("rcajero","num","ubi","mov",
                                 num = 0, ubi = "", mov = 0)
                                           
    v_caj = np.array([rcajero]*120)    
    
    linea_caj = a2.readline().strip()
    lista_caj = linea_caj.split(",")    
    i = 0                              
                                           
    while linea_caj != "":
        
        v_caj[i] = rcajero()
        v_caj[i].num = int(lista_caj[0])
        v_caj[i].ubi = lista_caj[1]
        v_caj[i].mov = int(lista_caj[2])
        i+=1
        linea_caj = a2.readline().strip()
        lista_caj = linea_caj.split(",")  
    
    a2.close()
        
                        
    #creo el vector de cuentas sobredimensionado:
    vector_cuentas = np.array([cuenta]* 1000)
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

    return vector_cuentas, cuentashabiles, v_caj




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

# COMIENZA EL EJERCICIO # 2:


def ejercicios_A_y_C(vec_cuenta, cuentashabiles, v_caj):
    
    a1 = open("operaciones.txt","r")
    
    linea_ope = a1.readline().strip()
    lista_ope = linea_ope.split(",")
    
    i = 0
    v_num_cajeros = np.array([0]*121)

    
    while linea_ope != "":
        camp_ante = lista_ope[0]
        
        saldo_total = 0.0 
        
        v_num_cajeros[int(lista_ope[4])]+=1 
        
        
        while camp_ante == lista_ope[0] and linea_ope != "":
            
            if lista_ope[5] == "1":
                saldo_total+= float(lista_ope[6])
            else:
                saldo_total = saldo_total - float(lista_ope[6])
            
            linea_ope = a1.readline().strip()
            lista_ope = linea_ope.split(",")
        
        saldo_actualizado = vec_cuenta[i].saldo + saldo_total 
        vec_cuenta[i].saldo = saldo_actualizado
        
        i+=1
        
        print("El total de los movimientos anuales de la cuenta:", camp_ante, "es de $", saldo_total, "pesos")
        
    a1.close()
    
    
    
    return vec_cuenta, cuentashabiles, v_caj, v_num_cajeros
    

    
def ejercicio_B(v_num_cajeros):
    
    mayor = 0
    
    for i in range(len(v_num_cajeros)):
        
        if v_num_cajeros[i] > mayor:
            mayor = v_num_cajeros[i]
            posicion = i
    
    cajero_mayor = posicion 
    
    
    print("        El cajero con mayor cantidad de movimientos en el a??o es el:", cajero_mayor)
    
    

def ejercicio_D(v_cajeros,v_num_cajeros):
    
    for i in range(len(v_num_cajeros)-1):
    
            v_cajeros[i].mov+= v_num_cajeros[i+1]
    
 
    
    return v_cajeros


# Comienza el ejercicio #3


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
    
    salir = "N"

    #Inicio de ciclo del menu:
    while salir == "N":
        
        #ESTA FUNCION REALIZA ALTAS, BAJAS Y MODIFICACIONES DE LAS CUENTAS. 

        #MENU PARA ELEJIR QUE DESEA HACER EL USUARIO:
        print(" "*10, "1- Si desea dar de alta una nueva cuenta.")
        print(" "*10, "2- Si desea dar de baja una cuenta.")
        print(" "*10, "3- Si desea realizar una modificacion en su cuenta.")
        print(" "*10, "4- Si desea salir al menu principal.")
        decision = int(input("Ingrese una opci??n: "))
        os.system("cls")

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
        
        elif decision == 4:
            salir = "S"
        
        #VUELVO A MOSTRAR PARA SABER SI QUIERE SALIR O REALIZAR OTRA OPERACION: 
    
    return vector_cuentas, cuentashabiles

# Funciones de menu

def mensaje(m):
    print()
    print(" "*8,m+'...')

def elegir(ultimo):
    print()
    print(" "*22,end=" ")
    opc=int(input(" Elija una opci??n: "))
    while((opc>ultimo) or (opc<0)):
        print(" "*20,"Lo siento, la Opci??n es inv??lida")
        print(" "*22,end=" ")
        opc=int(input(" Elija una opci??n: "))
    return opc

def pausa():
    print()
    print(" "*20,end=" ") # Fijate como ponemos "*20" para multiplicar los espacios vacios.
    input(" Presione Enter para continuar...")

def limpiar_pantalla():
    if (os.name)=='posix':
        os.system('clear')
    if (os.name)=='nt':
        os.system('cls')
    return None


def menu():
                               
    lista = cargadatos()
    bandera = 1
    salir = "N"
    
    while salir == "N":
    
    
        if bandera == 1:
            
            print("                            MENU PRINCIPAL")
            print()
            print("      1_CONSULTAR SALDO DE CUENTA")
            print("      2_ACTUALIZAR SALDO DE CUENTAS Y MOSTRAR TOTAL DE MOVIMIENTOS ANUALES")
            print("      3_AMB DE CUENTAS")
            print("      4_SALIR")
            print()
            
            opcion = elegir(4)
            
            if opcion == 1:
                
                consultacuenta(lista[0],lista[1])
                
                pausa()
            
            if opcion == 2:
                
                lista = ejercicios_A_y_C(lista[0],lista[1],lista[2])
                bandera = 2
            
            if opcion == 3:
                
                print("AMB DE CUENTAS")
                abm = ABMcuentas(lista[0],lista[1])
                aux = lista[2]
                lista = [abm[0],abm[1],aux]
            
            if opcion == 4:
                salir = "S"
                limpiar_pantalla()
        
        if bandera == 2:
            
            pausa()
            
            limpiar_pantalla()
            
            print("                          MENU PRINCIPAL")
            print()
            print("      1_CONSULTAR SALDO DE CUENTA")
            print("      2_AMB DE CUENTAS")
            print("      3_CONSULTAR CAJERO CON MAYOR CANTIDAD DE MOVIMIENTOS EN EL A??O")
            print("      4_ACTUALIZAR CANTIDAD HISTORICA DE MOVIMIENTOS DE LOS CAJEROS")
            print("      5_SALIR")
            print()
            
            opcion = elegir(5)
            
            if opcion == 1:
                
                consultacuenta(lista[0],lista[1])
                
                pausa()
            
            if opcion == 2:
                
                print("AMB DE CUENTAS")
                abm = ABMcuentas(lista[0],lista[1])
                aux1 = lista[2]
                aux2 = lista[3]
                lista = [abm[0],abm[1],aux1,aux2]
                
        
            if opcion == 3:
                
                ejercicio_B(lista[3])
                
            if opcion == 4:
                
                cajeros = ejercicio_D(lista[2],lista[3])
                aux1 = lista[0]
                aux2 = lista[1]
                aux3 = lista[3]
                lista = [aux1,aux2,cajeros,aux3]
                
                mensaje("CANTIDAD HISTORICA DE MOVIMIENTOS DE CAJEROS ACTUALIZADA")
            
            if opcion == 5:
                
                salir = "S"
                limpiar_pantalla()
            
menu()         
            
            
                
            
        
    
    
    
    