# SCOPES

'''
En Python los scopes son los alcances que va a tener una funcion, hay 3 tipos de scopes
 - Locales
 - Enclosing
 - Globales
 
  '''
nombre = "Joram"

def imprimir_nombre():
    # se usa para utilizar la variable con scope global
    global nombre
    nombre = "Eduardo"
    print(f'Hola como estas {nombre}')

imprimir_nombre()
print(f"El valor de mi variable global es : {nombre}")

def imprimir():
    name = "Joel"
    age = 27
    def imprimir_edad():
        nonlocal age
        age = 70
        print(f"mi edad es: {age}")
    imprimir_edad()
    print(f"mi edad es: {age}")

imprimir()

'''
********** Scope Global ***********
Las variables con un scope global son las que son definidas 
fuera del cuerpo de la funcion, en caso de requerir modificar la variable global se
asigna la palabra 'global' antes del nombre de la variable y posteriormente se le puede dar 
otra asignacion como normalmente se realiza. p.ej

global nombre
nombre = "Eduardo"

********** Scope Local ***********
Este solo esta disponible dentro de la funcion, pero si se manda a llamar fuera de ella 
causara un error el cual dice que la variable no esta definida, esto es porque solo esta 
definida dentro del cuerpo de la funcion

********** Scope Enclosing ***********
Para enclosing es como una variante para poder ocupar una variable local en lugar de una global
es decir que puede ser modificada y seguir estando alterada despues de esta modificacion 

se utiliza la palabra 'nonlocal' seguido del nombre de la variable, posteriormente se puede modificar
y seguir trabajando pero tomando en cuenta que si se manda a llamar esta variable en otro momento, esta ya estara 
modificada. p.ej

nonlocal age
age = 70

'''
