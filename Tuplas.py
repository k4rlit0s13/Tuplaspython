print("Hola usuario, porfavor digíta tu información copmleta: ")


nombre=input("Nombre: ")
edad=input("Edad: ")
altura=input("Altura: ")

ciudad=input("Ciudad: ")
país=input("País: ")
dirección=input("Dirección: ")

educación=input("Educación(título):")
experciaLaboral=input("Experiencia laboral en: ")


infousuario=tuple((nombre,edad,altura,ciudad,país,dirección,educación,experciaLaboral))
print(F"""El usuario de nombre {infousuario[0]} con edad de {infousuario[0]} años""")