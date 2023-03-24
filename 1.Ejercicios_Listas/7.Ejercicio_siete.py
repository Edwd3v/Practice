
# Escriba un programa que permita crear una lista de palabras y que, a continuación, elimine los elementos repetidos (dejando únicamente el primero de los elementos repetidos).

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

    for i in reversed(strings_list):
        # print(strings_list.index(i))
        if strings_list.count(i) > 1:
            strings_list.remove(i)
            #print(i)'''

    print('La lista sin repeticiones es: {}'.format(strings_list))
    

if __name__ == '__main__':
    run()