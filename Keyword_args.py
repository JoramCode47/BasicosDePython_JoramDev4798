#  KEYWORD **ARGS
'''
keyword arguments **kwargs
permite que una funcion recopile un numero variado de argumentos
en un diccionario, solo que en este caso si va estar identificado 
el argumento por una clave
'''

#generalmente se le llama **kwargs

def conectar_bd(**kwargs):
    # print(type(kwargs))
    # print(kwargs)
    user_db = kwargs['user_name']
    pass_db = kwargs['password']
    port = kwargs['port']

    nombre_db = kwargs.get('db_name', 'default_valor')
    host = kwargs.get('host_name')
    query_sql = kwargs.get('query')

    print(nombre_db, user_db, pass_db)

conectar_bd(host_name='localhost', port=3304, user_name='user1234', password='12345r98', query = "SELECT * FROM table_name")
conectar_bd(db_name = 'Tiendita', host_name='localhost', port=3304, user_name='user1234', password='12345r98', query = "SELECT * FROM table_name")

