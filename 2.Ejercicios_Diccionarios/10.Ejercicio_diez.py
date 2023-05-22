
# Escribir un programa que permita gestionar la base de datos de clientes de una empresa. Los clientes se guardarán en un diccionario en el que la clave de cada cliente será su NIF, y el valor será otro diccionario con los datos del cliente (nombre, dirección, teléfono, correo, preferente), donde preferente tendrá el valor True si se trata de un cliente preferente. El programa debe preguntar al usuario por una opción del siguiente menú: (1) Añadir cliente, (2) Eliminar cliente, (3) Mostrar cliente, (4) Listar todos los clientes, (5) Listar clientes preferentes, (6) Terminar. En función de la opción elegida el programa tendrá que hacer lo siguiente:

#1 - Preguntar los datos del cliente, crear un diccionario con los datos y añadirlo a la base de datos.
#2 - Preguntar por el NIF del cliente y eliminar sus datos de la base de datos.
#3 - Preguntar por el NIF del cliente y mostrar sus datos.
#4 - Mostrar lista de todos los clientes de la base datos con su NIF y nombre.
#5 - Mostrar la lista de clientes preferentes de la base de datos con su NIF y nombre.
#6 - Terminar el programa.

def run():

    data_base_customers = {}
    customers_ID = {}
    preference_customers = {}

    def add_customer(name, nif, address, tel, e_mail, vip):
        customers_ID[nif] = name

        if vip == 'True' or vip == 'T':
            preference_customers[name] = nif

        customers_data = {
            'Address': address,
            'Tel': tel,
            'E-mail': e_mail,
            'VIP': vip
        }

        data_base_customers[name] = customers_data

    add_customer('Oliver', '8765432109', '987 Willow Avenue', '123-4567', 'oliver@gmail.com', 'True')
    add_customer('Emma', '1098765432', '345 Pine Street', '234-5678', 'emma@hotmail.com', 'False')
    add_customer('Liam', '2109876543', '678 Elm Court', '345-6789', 'liam@yahoo.com', 'True')
    add_customer('Ava', '4321098765', '901 Oak Road', '456-7890', 'ava@outlook.com', 'False')
    add_customer('John', '1234567890', '456 Pine Street', '555-1234', 'john@gmail.com', 'True')
    add_customer('Emma', '9876543210', '789 Elm Avenue', '555-4321', 'emma@yahoo.com', 'False')
    add_customer('Daniel', '5555555555', '321 Maple Lane', '444-5678', 'daniel@hotmail.com', 'True')
    add_customer('Sophia', '9998887777', '654 Birch Court', '333-8765', 'sophia@gmail.com', 'False')
    add_customer('Liam', '1112223333', '987 Oak Street', '222-6789', 'liam@yahoo.com', 'True')
    add_customer('Sarah', '5551112222', '123 Cherry Lane', '111-2222', 'sarah@gmail.com', 'True')
    add_customer('Michael', '9990001111', '456 Elm Street', '333-4444', 'michael@hotmail.com', 'False')
    add_customer('Olivia', '7778889999', '789 Oak Avenue', '555-6666', 'olivia@yahoo.com', 'True')
    add_customer('Noah', '2223334444', '321 Pine Road', '777-8888', 'noah@gmail.com', 'False')
    add_customer('Isabella', '4445556666', '654 Maple Lane', '999-0000', 'isabella@yahoo.com', 'True')
    add_customer('Ethan', '8889990000', '987 Birch Street', '111-2222', 'ethan@gmail.com', 'False')
    add_customer('Mia', '6667778888', '123 Oak Avenue', '333-4444', 'mia@hotmail.com', 'True')
    add_customer('James', '1112223333', '456 Elm Road', '555-6666', 'james@yahoo.com', 'False')
    add_customer('Charlotte', '3334445555', '789 Pine Lane', '777-8888', 'charlotte@gmail.com', 'True')
    add_customer('Benjamin', '5556667777', '321 Birch Street', '999-0000', 'benjamin@hotmail.com', 'False')


    while True:
        action = input('''
            What do you want to do?

            1 - Add: Add customer
            2 - Delete: Delete customer
            3 - Show: Show customer information
            4 - All: Show all customers
            5 - VIP: VIP customers
            6 - Finish

            : ''').strip().upper() # Se utilizó el método strip() en la entrada del usuario para eliminar espacios en blanco adicionales al inicio o al final del texto.Transformamos lo ingresado en asction a mayusculas por si se ingreso texto.

        # 1 - Add: Add customer
        if action in ('1', 'ADD'):
            name = input('Name: ')
            nif = input('NIF Number: ')
            address = input('Address: ')
            tel = input('Tel: ')
            e_mail = input('E-mail: ')
            vip = input('VIP (T/F?): ')

            add_customer(name, nif, address, tel, e_mail, vip) # Vuelvo a invocar la función para añadir el nuevo cliente teniendo en cuenta los pasos.

        # 2 - Delete: Delete customer
        elif action in ('2', 'DELETE'):
            nif_customer_delete = input('NIF to delete: ')
            if nif_customer_delete in customers_ID:
                name_deleted = customers_ID.pop(nif_customer_delete) 
                # ASISTENCIA DE CHAT GPT EN LA MEJORA DE MI CODIGO INICIAL (Vease el mismo ejercicio resuelto en el archivo 10.1.Ejercicio_diez_uno_my_code.py)
                # Se utilizó el método pop() para eliminar un cliente del diccionario customers_ID y el operador del para eliminarlo del diccionario data_base_customers en lugar de hacerlo por separado.
                # El cambio que hice en el código fue en la sección donde se eliminan clientes. Originalmente, se utilizaba el operador del para eliminar un cliente del diccionario customers_ID, y luego se buscaba y eliminaba el cliente correspondiente del diccionario data_base_customers. En lugar de hacerlo por separado, opté por utilizar el método pop() para eliminar un cliente tanto del diccionario customers_ID como del diccionario data_base_customers en un solo paso.
                # La razón detrás de esta modificación es principalmente por eficiencia y consistencia. Al utilizar el método pop(), podemos eliminar directamente el cliente deseado del diccionario y obtener su valor al mismo tiempo. Esto evita tener que buscar nuevamente el cliente en el diccionario data_base_customers después de eliminarlo de customers_ID.
                del data_base_customers[name_deleted]
                print(f'Customer {name_deleted} with NIF {nif_customer_delete} deleted.')
            else:
                print(f'The customer registered with the number {nif_customer_delete} does not exist in our database.')

        # 3 - Show: Show customer information
        elif action in ('3', 'SHOW'):
            nif_show = input('NIF to search: ')
            if nif_show in customers_ID:
                name_search = customers_ID[nif_show]
                customer_data = data_base_customers.get(name_search) 
                # ASISTENCIA DE CHAT GPT EN LA MEJORA DE MI CODIGO INICIAL (Vease el mismo ejercicio resuelto en el archivo 10.1.Ejercicio_diez_uno_my_code.py)
                # Se utilizó el método get() para obtener los datos del cliente del diccionario data_base_customers en lugar de verificar si existe la clave antes de acceder a ella.
                # Aplicamos el cambio de utilizar el método get() para obtener los datos del cliente del diccionario data_base_customers en lugar de verificar si existe la clave antes de acceder a ella porque es una forma más segura y conveniente de acceder a los valores de un diccionario.
                # El método get() nos permite obtener el valor asociado a una clave en un diccionario de manera segura. Si la clave existe en el diccionario, el método devuelve el valor correspondiente. Sin embargo, si la clave no existe, en lugar de generar un error, el método get() devuelve un valor predeterminado que podemos especificar como argumento.
                #En el contexto del código, en lugar de verificar si un cliente existe en el diccionario data_base_customers antes de acceder a sus datos, podemos simplemente utilizar el método get() para obtener los datos del cliente y, en caso de que el cliente no exista, obtener un valor predeterminado o un mensaje indicando que el cliente no está registrado.
                # Esto simplifica el código y evita la necesidad de escribir condiciones adicionales para verificar la existencia de claves antes de acceder a los valores. Además, nos permite especificar un valor predeterminado que se utilizará si la clave no existe, lo cual puede ser útil en diversas situaciones.
                if customer_data:
                    print(name_search)
                    for key, value in customer_data.items():
                        print(key, ':', value)
                else:
                    print(f'The registered with the number {nif_show} does not exist in our database.')
            else:
                print(f'The customer registered with the number {nif_show} does not exist in our database.')

        # 4 - All: Show all customers
        elif action in ('4', 'ALL'):
            for nif, name in customers_ID.items():
                print("{:<10} {} {:<10}".format(name, ':', nif))

        # 5 - VIP: VIP customers
        elif action in ('5', 'VIP'):
            if preference_customers:
                for name, nif in preference_customers.items():
                    print("{:<10} {} {:<10}".format(name, ':', nif))
            else:
                print('There are no preferred customers in our database.')

        # 6 - Finish
        elif action in ('6', 'FINISH'):
            print(data_base_customers)

            print('FINISH')
            break

        else:
            break


if __name__ == '__main__':
    run()
