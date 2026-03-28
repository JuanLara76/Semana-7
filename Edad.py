edad=int(input("ingrese su edad:"))
licencia=input("¿tiene licencia de conducir? (si/no):")
if edad >= 18 and licencia== "si":
    print("¡puedes conducir con cuidado!, maneja con cuidado")
else:
    print("no puedes conducir, necesitas tenr al menos 18 años y una licencia de conduccion")
