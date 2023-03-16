
# Escriba un programa que permita crear dos listas de palabras y que, a continuación, escriba las siguientes listas (en las que no debe haber repeticiones):

# Lista de palabras que aparecen en las dos listas.
# Lista de palabras que aparecen en la primera lista, pero no en la segunda.
# Lista de palabras que aparecen en la segunda lista, pero no en la primera.
# Lista de palabras que aparecen en ambas listas.
# Nota: Para evitar las repeticiones, el programa deberá empezar eliminando los elementos repetidos en cada lista.

def run():

    # LISTA UNO

    num_list = int(input('Dígame cuántas palabras tiene la primera lista: '))
    strings_list_1 = []

        
    if num_list <= 0:
        print('¡Imposible!')
        return False

    for i in range (num_list):
        if num_list > 0:
            element = input('Dígame la palabra {}: '.format(i+1))
            strings_list_1.append(element)
    
    print('La primera lista es: {}'.format(strings_list_1))

    # LISTA NUMERO DOS

    num_list = int(input('Dígame cuántas palabras tiene la segunda lista: '))
    strings_list_2 = []
        
    if num_list <= 0:
        print('¡Imposible!')
        return False

    for i in range (num_list):
        if num_list > 0:
            element = input('Dígame la palabra {}: '.format(i+1))
            strings_list_2.append(element)
    
    print('La segunda lista es: {}'.format(strings_list_2))

    # Lista de palabras que aparecen en las dos listas.
    elements_repited = []
    for i in strings_list_1:
        for x in strings_list_2:
            if i == x:
                elements_repited.append(i)
                set_elements_repited = set(elements_repited)
                list_elements_repited = list(set_elements_repited)

    print('Palabras que aparecen en las dos listas: {}'.format(list_elements_repited))

    # Lista de palabras que aparecen en la primera lista, pero no en la segunda.
    elements_alone_list_1 = []
    for i in strings_list_1:
        if not i in strings_list_2:
            elements_alone_list_1.append(i)
            set_elements_alone_list_1 = set(elements_alone_list_1)
            list_elements_alone_list_1 = list(set_elements_alone_list_1)
    print('Palabras que sólo aparecen en la primera lista: {}'.format(list_elements_alone_list_1))
    
    # Lista de palabras que aparecen en la segunda lista, pero no en la primera.
    elements_alone_list_2 = []
    for i in strings_list_2:
        if not i in strings_list_1:
            elements_alone_list_2.append(i)
            set_elements_alone_list_2 = set(elements_alone_list_2)
            list_elements_alone_list_2 = list(set_elements_alone_list_2)
    print('Palabras que sólo aparecen en la segunda lista: {}'.format(list_elements_alone_list_2))

    # Lista de palabras que aparecen en ambas listas.
    list_with_all_elements = strings_list_1 + strings_list_2
    list_with_all_elements = set(list_with_all_elements)
    list_with_all_elements = list(list_with_all_elements)
    print('Todas las palabras de las dos listas: {}'.format(list_with_all_elements))


if __name__ == '__main__':
    run()
