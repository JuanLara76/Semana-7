a=input("Tienes pasaporte vigente? (si/no):")
b=input("Tienes visa? (si/no)")
c=input("Tu pais esta exento de visa? (si/no):")
if a== 'si' and (b== 'si' or c== 'si'):
    print("'Puede viajar. tenga buen viaje!")
else :
    print("No puede viajar. favor revisa tus documentos.")
