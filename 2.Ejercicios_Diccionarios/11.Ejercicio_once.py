# El directorio de los clientes de una empresa está organizado en una cadena de texto como la de más abajo, donde cada línea contiene la información del nombre, email, teléfono, nif, y el descuento que se le aplica. Las líneas se separan con el carácter de cambio de línea \n y la primera línea contiene los nombres de los campos con la información contenida en el directorio.

#nif;nombre;email;teléfono;descuento\n01234567L;Luis González;luisgonzalez@mail.com;656343576;12.5\n71476342J;Macarena Ramírez;macarena@mail.com;692839321;8\n63823376M;Juan José Martínez;juanjo@mail.com;664888233;5.2\n98376547F;Carmen Sánchez;carmen@mail.com;667677855;15.7

#nif;nombre;email;teléfono;descuento
#\n
#01234567L;Luis González;luisgonzalez@mail.com;656343576;12.5
#\n
#71476342J;Macarena Ramírez;macarena@mail.com;692839321;8
#\n
#63823376M;Juan José Martínez;juanjo@mail.com;664888233;5.2
#\n
#98376547F;Carmen Sánchez;carmen@mail.com;667677855;15.7

# Escribir un programa que genere un diccionario con la información del directorio, donde cada elemento corresponda a un cliente y tenga por clave su nif y por valor otro diccionario con el resto de la información del cliente. Los diccionarios con la información de cada cliente tendrán como claves los nombres de los campos y como valores la información de cada cliente correspondientes a los campos. Es decir, un diccionario como el siguiente:

# {'01234567L': {'nombre': 'Luis González', 'email': 'luisgonzalez@mail.com', 'teléfono': '656343576', 'descuento': 12.5}, '71476342J': {'nombre': 'Macarena Ramírez', 'email': 'macarena@mail.com', 'teléfono': '692839321', 'descuento': 8.0}, '63823376M': {'nombre': 'Juan José Martínez', 'email': 'juanjo@mail.com', 'teléfono': '664888233', 'descuento': 5.2}, '98376547F': {'nombre': 'Carmen Sánchez', 'email': 'carmen@mail.com', 'teléfono': '667677855', 'descuento': 15.7}} 

def run():

    basedata_customers = {}
    customers_whit_kv = []

    # SOLUCION CON VARIABLE DECLARADO
    '''
    # Este codigo es posible solo si declaramos la variable con el texto incluido, no funciona si ingresamos este mismo texto por teclado a traves de un intput
    string_whit_all_customers = "nif;nombre;email;teléfono;descuento\n01234567L;Luis González;luisgonzalez@mail.com;656343576;12.5\n71476342J;Macarena Ramírez;macarena@mail.com;692839321;8\n63823376M;Juan José Martínez;juanjo@mail.com;664888233;5.2\n98376547F;Carmen Sánchez;carmen@mail.com;667677855;15.7"

    string_for_customer = string_whit_all_customers.split("\n")

    print(string_for_customer)
    '''

    # SOLUCIÓN CON INFORMACIÓN IONGRESADA POR TECLADO
    #string_whit_all_customers = "nif;nombre;email;teléfono;descuento/01234567L;Luis González;luisgonzalez@mail.com;656343576;12.5/71476342J;Macarena Ramírez;macarena@mail.com;692839321;8/63823376M;Juan José Martínez;juanjo@mail.com;664888233;5.2/98376547F;Carmen Sánchez;carmen@mail.com;667677855;15.7/01234567L;Luis González;luisgonzalez@mail.com;656343576;12.5/71476342J;Macarena Ramírez;macarena@mail.com;692839321;8"

    # Transformamos el string en una lista para hacerlo mas manipulable y segmentando cada que aparezca un '/'
    string_whit_all_customers = input("Data Customer: ")
    string_for_customer = string_whit_all_customers.split("/")

    # Tansformamos en lista nuestro primer grupo ya que en este se encuentran los datos o las keys que llevara cada subdiccionario de cada cliente
    keys = string_for_customer[0].split(';')
    keys.pop(0)
    string_for_customer.pop(0)    # Elimino los elementos que conforman 'keys' de la lista 'string_for_customer' ya que ahi no me son utiles.
    #print('Llaves:', keys)

    # Creamso las sublistas de 'string_for_customer' 
    individual_customers = [element.split(';')for element in string_for_customer]
    # Las sigientes lineas de codigo las utilice para ver como podia acceder a un elemento de cada una de las listas.
    #count = 0
    #for element in individual_customers:
    #    print(individual_customers[count][0])
    #    count += 1
    
    # Creamos una lista con los NIF de cada cliente y los eliminamos de la lista individual_customers 
    # nif = [element[0] for element in individual_customers] # Con esta linea agregamos los NIF pero no los eliminamos de la lista individual_customers
    nif = []
    count = 0
    # El siguiente bucle nos permitira agregar los nif de cada cliente a nuestra lista nif y a su vez eliminara los nif de la lista individual_customers
    for sublist in individual_customers[:]:
        individual_nif = sublist[0]
        nif.append(individual_nif)
        del individual_customers[count][0]
        count += 1

    # Convertimos ahora los elementos de individual customer esn diccionario utilizando los valores de keys
    for element in individual_customers:
        customer_values = element
        now_dictionary = dict(zip(keys, customer_values))
        customers_whit_kv.append(now_dictionary)

    # Ahora vamos a crear el diccionario con la respectiva clave y el respectivo valor 
    basedata_customers = dict(zip(nif, customers_whit_kv))
    print(basedata_customers)

if __name__ == '__main__':
    run()