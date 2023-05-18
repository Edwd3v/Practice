
# Escribir un programa que cree un diccionario de traducción español-inglés. El usuario introducirá las palabras en español e inglés separadas por dos puntos, y cada par <palabra>:<traducción> separados por comas. El programa debe crear un diccionario con las palabras y sus traducciones. Después pedirá una frase en español y utilizará el diccionario para traducirla palabra a palabra. Si una palabra no está en el diccionario debe dejarla sin traducir.

import re
def run():

    diccionary ={}
    list_1 = []
    list_2 = []

    words = input('''

CREA TU DICCIONARIO
        
 IMPORTANTE!!
    1. ingresa las palabras asi: "<palabra>:<traducción>".
    2. Separa cada una de estas por una coma.

    Ingrese las palabras:
    ''')
    list_1 = re.split(':|,', words) # Esto lo aprendi hoy, que util puede llegar a ser si lo sabemso utilizar
    
    for i in list_1:
        if list_1.index(i) % 2 == 0:
            list_2.append(i)
            list_1.remove(i)
        else:
            continue

    for i in list_2:
        for x in list_1:
            diccionary [list_2(x)] = list_2(i)

    print(words)
    print(list_1)
    print(list_2)
    print(diccionary)
    

if __name__ == '__main__':
    run()