print("Hola usuario, porfavor digíta tu información copmleta: ")


nombre=input("Nombre: ")
edad=input("Edad: ")
altura=input("Altura: ")

ciudad=input("Ciudad: ")
país=input("País: ")
dirección=input("Dirección: ")

educación=input("Educación:")
título=input("Que título posees: ")

expercia=input("Que experiencia laboral tienes: ")
código=input("Experiencia en código: ")

infousuario=tuple((nombre,edad,altura))
direcUsuario=tuple((ciudad,país,dirección))
estudioOusuario=tuple((educación,título)
expLaboral=tuple((expercia,código))


print(F"""
El usuario de nombre {infousuario[0]} con edad de {infousuario[0]} años, proveniente 
del país{direcUsuario[1]} {[]}{[]}
""")