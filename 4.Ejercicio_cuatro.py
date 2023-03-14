
# Escriba un programa que permita crear una lista de palabras y que, a continuación, pida una palabra y elimine esa palabra de la lista.

def run():

    num_list = int(input('Dígame cuántas palabras tiene la lista: '))
    strings_list = []
        
    if num_list <= 0:
        print('¡Imposible!')
        return False

    for i in range (num_list):
        if num_list > 0:
            element = input('Dígame la palabra {}: '.format(i+1))
            strings_list.append(element)
    
    print('La lista creada es: {}'.format(strings_list))

    delete_word = input('Palabra a eliminar: ')

    '''strings_list.remove(delete_word)
    print('La lista de ahora: {}'.format(strings_list))'''

    # MANERA DE ELIMINAR TODAS LAS PALABRAS 

    # NOTA CHAT GPT = Sin embargo, hay algunas situaciones en las que puede parecer que el ciclo for se está saltando elementos de una lista. Por ejemplo, si estás modificando la lista dentro del ciclo for (por ejemplo, agregando o eliminando elementos), esto puede afectar la estructura del ciclo y puede hacer que se salte algunos elementos.

    for i in reversed(strings_list):
        if i == delete_word:
            # position = strings_list.index(i)
            strings_list.remove(i)
            # print(strings_list)
        else:
            continue
    print(strings_list)


if __name__ == '__main__':
    run()