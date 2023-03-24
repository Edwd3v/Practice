
# Escriba un programa que permita crear una lista de palabras y que, a continuación, cree una segunda lista igual a la primera, pero al revés (no se trata de escribir la lista al revés, sino de crear una lista distinta).

def run():

    num_list = int(input('Dígame cuántas palabras tiene la lista: '))
    strings_list = []
    invers_string_list = []
        
    if num_list <= 0:
        print('¡Imposible!')
        return False

    for i in range (num_list):
        if num_list > 0:
            element = input('Dígame la palabra {}: '.format(i+1))
            strings_list.append(element)
    
    print('La lista creada es: {}'.format(strings_list))

    for i in reversed(strings_list):
        invers_string_list.append(i)
    
    print('La lista inversa es: {}'.format(invers_string_list))

if __name__ == '__main__':
    run()