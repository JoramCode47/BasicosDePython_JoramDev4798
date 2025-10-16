# *ARGS
'''
variables positional arguments
args
permite que una funcion recopile un numero variado de argumentos posisionales
en una tupla por su posicionamiento
'''

#generalmente se le llama *args

'''
Todo lo que se pase como *args es una tupla
por lo que internamente se podria iterar  esta tupla e ir sumando
'''

def suma(*args):
    print(args)
    # return sum(args)
    resultado = 0
    for number in args:
        resultado += number
    
    return resultado

res = suma(1,2,4,5,6,7,8,9,10,11,15,15)
print(f'El resultado de la operación con *args es: {res}')




