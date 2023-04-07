
# Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en un diccionario. Después debe mostrar por pantalla el mensaje <nombre> tiene <edad> años, vive en <dirección> y su número de teléfono es <teléfono>.

def run():

    # Declaramos un diccionario vacio
    user_information = {
        'name':'',
        'age':'',
        'address':'',
        'tel':''
    }

    # Solicitamos los datos al usuario
    name = input('What is your name?: ')
    user_information['name'] = name

    age = int(input('What is you age: '))
    user_information['age'] = age

    address = input('What is you address: ')
    user_information ['address'] = address

    tel = input('What is your tel: ')
    user_information['tel'] = tel

    print('Su nombre es {}, tiene {} años, vive en {}, y su numero de telefono es {}'.format(user_information['name'], user_information['age'], user_information['address'], user_information['tel'] ))

    print(f"Su nombre es {user_information['name']}, tiene {user_information['age']} años, vive en {user_information['address']}, y su numero de telefono es {user_information['tel']} ")

    print(user_information)

if __name__ == '__main__':
    run()