
# Escriba un programa que permita crear una lista de palabras. Para ello, el programa tiene que pedir un número y luego solicitar ese número de palabras para crear la lista. Por último, el programa tiene que escribir la lista.

# Dígame cuántas palabras tiene la lista: 3
# Dígame la palabra 1: Alberto
# Dígame la palabra 2: Benito
# Dígame la palabra 3: Carmen
# La lista creada es: ['Alberto', 'Benito', 'Carmen']

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

if __name__ == '__main__':
    run()
