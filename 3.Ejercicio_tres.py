
# Escriba un programa que permita crear una lista de palabras y que, a continuación, pida dos palabras y sustituya la primera por la segunda en la lista.

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

    susti_word = input('Sustituir la palabra: ')
    remplace_word = input('por la palabra: ')

    '''position = strings_list.index(susti_word)
    strings_list[position] = remplace_word
    
    print(strings_list)'''

    # CODIGO PARA SUSTITUIR LAS PALABRAS IGUALES

    for i in strings_list:
        if i == susti_word:
            position = strings_list.index(i)
            strings_list[position] = remplace_word
            # print(strings_list)
        else:
            continue
    print(strings_list)

if __name__ == '__main__':
    run()