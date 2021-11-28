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
