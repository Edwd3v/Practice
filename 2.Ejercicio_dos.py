
# Escriba un programa que permita crear una lista de palabras y que, a continuación, pida una palabra y diga cuántas veces aparece esa palabra en la lista. 

def run():

    num_list = int(input('Dígame cuántas palabras tiene la lista: '))
    strings_list = []
    sets = 0
    
    if num_list <= 0:
        print('¡Imposible!')
        return False

    for i in range (num_list):
        if num_list > 0:
            element = input('Dígame la palabra {}: '.format(i+1))
            strings_list.append(element)
    
    print('La lista creada es: {}'.format(strings_list))

    word_share = input('Dígame la palabra a buscar: ')

    for i in strings_list:
        if i == word_share:
            sets += 1 

    if sets == 1:
        print('La palabra {} aparece una vez en la lista.'.format(word_share))
    elif sets > 1:
        print('La palabra {} aparece {} veces en la lista'.format(word_share, sets))
    else:
        print('La palabra {} no aparece en la lista.'.format(word_share))

if __name__ == '__main__':
    run()