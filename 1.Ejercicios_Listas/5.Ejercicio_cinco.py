
# Escriba un programa que permita crear dos listas de palabras y que, a continuación, elimine de la primera lista los nombres de la segunda lista.

def run():

    #LISTA UNO

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

    # LISTA DOS

    num_list = int(input('Dígame cuántas palabras tiene la lista de palabras a eliminar: '))
    deleted_list = []
        
    if num_list <= 0:
        print('¡Imposible!')
        return False

    for i in range (num_list):
        if num_list > 0:
            element = input('Dígame la palabra {}: '.format(i+1))
            deleted_list.append(element)

    print('La lista creada es: {}'.format(deleted_list))

    for i in reversed(strings_list):
        for x in reversed(deleted_list):
            if x == i:
                strings_list.remove(i)
            else:
                continue

    print('La lista es ahora: {}'.format(strings_list))
    
    



if __name__ == '__main__':
    run()