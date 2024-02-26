print("Hola usuario, porfavor digíta tu información copmleta para la entrevista: ")


nombre=input("Nombre: ")
edad=input("Edad: ")
altura=input("Altura: ")

ciudad=input("Ciudad donde vive: ")
país=input("País: ")
dirección=input("Dirección: ")

educación=input("Educación:")
título=input("Que título posees: ")

expercia=input("Que experiencia laboral tienes: ")
código=input("Que nivel sientes que posees en código: ")

infousuario=tuple((nombre,edad,altura))
direcUsuario=tuple((ciudad,país,dirección))
estudioOusuario=tuple((educación,título))
expLaboral=tuple((expercia,código))


print(F"""
      
El usuario de nombre {infousuario[0]} con edad de {infousuario[0]} años y una
altura aproximadamente de {infousuario[2]},vive en la ciudad de {direcUsuario[0]} 
en {direcUsuario[1]} con la dirección {direcUsuario[2]}.

Posee la siguiente educación: {estudioOusuario[0]}, obteniendo titulos como: {estudioOusuario[1]}

Desea entrar a la instituación de campuslands con un conocimiento de código de nivel


""")