
# Programa que declare tres listas ‘lista1’, ‘lista2’ y ‘lista3’ de cinco enteros cada uno, pida valores para ‘lista1’ y ‘lista2’ y calcule lista3=lista1+lista2.

import random

def run ():
   
    # Esta funcon nos ayuda a llenar dos lista con maximo cinco numeros al azar del 1 - 100
    def load_strings_in_list(list):
        while len(list) < 5:
            random_number = random.randint(1, 10)
            list.append(random_number)
    
    list_1 = []
    list_2 = []

    # Llamamos a la funcion para llenar dos listas    
    load_strings_in_list(list_1)
    print(list_1)    
    load_strings_in_list(list_2)
    print(list_2)

    list_3 = list_1 + list_2
    #Organizamos la lista
    list_3.sort()
    print(list_3)

    for i in reversed(list_3):
        if list_3.count(i) > 1:
            list_3.remove(i)
    print('Elementos sin retetir: ', list_3) 
    # Esto lo podemos hacer convirtiendo la lista en un conjunto (set) pero es interesante saber como lo podemos hacer en caso de que no lo recordemos, es decir es una alternativa.
    
if __name__ == '__main__':
    run()