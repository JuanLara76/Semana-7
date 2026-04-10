a=int(input("Ingresa tu edad:"))
b=input("Tienes carnet de socio vigente (si/no):")
if a > 14 and b== 'si':
    print ("puedes ingresar a el gimnasio")
    
else :
    c=input("Tienes pase de invitado(si/no):")
    d=input("Vienes con un socio activo?(si/no):")
    if c== 'si' or d == 'si':
        print ("puedes ingresar al gimnasio")
    else :
        print ("No puedes ingresar al gimnasio")
