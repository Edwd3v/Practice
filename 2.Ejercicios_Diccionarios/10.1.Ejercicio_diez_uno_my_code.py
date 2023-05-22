
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

        name_ID = name
        nif_ID = nif
        customers_ID[nif_ID] = name_ID

        if vip == 'True' or vip == 'T':
            preference_customers[name] = nif
 
        customers_data = {}

        customers_data['Address'] = address
        customers_data['Tel'] = tel
        customers_data['E-mail'] = e_mail
        customers_data['VIP'] = vip

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

    #print(data_base_customers)
    #print(preference_customers)
    #print(customers_ID)

    while True:
            
            action = input('''

    What do you want to do?

        1 - Add: add customer
        2 - Delete: Delete customer
        3 - Show: Show informatión customer
        4 - All: Show all customers
        5 - VIP: VIP customers
        6 - Finish
        7 - Update 


    : ''')
            action = action.upper() # Transformamos lo ingresado en asction a mayusculas por si se ingreso texto.

            if action == '1' or action == 'ADD':
                name = input('Name: ')
                nif = input('NIF Number: ')
                customers_ID[nif] = name
                address = input('Address: ')
                tel = input('Tel: ')
                e_mail = input('E-mail: ')
                vip = input('VIP (T/F?): ' )

                if vip == 'True' or vip == 'T':
                    preference_customers[name] = nif
          
                # Añadimos los datos
                # Creamos el diccionario provicional donde ingresaremos los datos del ultimo cliente que estamos registrando.
                customers_data = {}
                customers_data['Address'] = address
                customers_data['Tel'] = tel
                customers_data['E-mail'] = e_mail
                customers_data['VIP'] = vip
                data_base_customers[name] = customers_data

            # Eliminar Clientes
            elif action == '2' or action == 'DELETE':
                nif_customer_delete = input('NIF to delete: ')
                if nif_customer_delete in customers_ID:
                    # Declaramos los datos del clientes antes de que sean borrados para poder mostrar el mensaje de que la operación de delated concluyo con exito.
                    value_deleted = customers_ID[nif_customer_delete]
                    print(value_deleted)
                    del customers_ID[nif_customer_delete]
                    print('Customer {} deleted whit NIF {}'.format(value_deleted,nif_customer_delete))                                                 
                else:
                    print('The customer registered with the number {} does not exist in our database.'.format(nif_customer_delete))

            # Buscar Clientes                       
            elif action == '3' or action == 'SHOW':
                nif_show = input('Nif search: ')
                if nif_show in customers_ID:
                    name_search = customers_ID[nif_show]
                    if name_search in data_base_customers:
                        customer_data = data_base_customers[name_search]
                        print(name_search)
                        for key, value in customer_data.items():
                            print(key, ':', value)

                    else:
                        print('The customer registered with the number {} does not exist in our database.'.format(nif_show))
                else:
                    print('The customer registered with the number {} does not exist in our database.'.format(nif_show))

            # Todos los clientes:
            elif action == '4' or action == 'ALL':
                for key, values in customers_ID.items():
                    #print(f'{values} : {key}')
                    print("{:<10} {} {:<10}".format(values, ':', key))

            # Clientes preferenciales
            elif action == '5' or action == 'VIP':
                if len(preference_customers) > 0:
                    for key, values in preference_customers.items():
                        print("{:<10} {} {:<10}".format(key, ':', values))
                else:
                    print('There are no preferred customers in our database.')

            elif action == '6' or action == 'FINISH':
                print(data_base_customers)
                print('FINISH')
                break
        
            else:
                break           


if __name__ == '__main__':
    run()