
# Hacer un programa que inicialice una lista de números con valores aleatorios (10 valores), y posterior ordene los elementos de menor a mayor

import random 

def run():
    
    list_random = []

    while len(list_random) < 10:
        num_ramdom = random.randint(1, 100)
        list_random.append(num_ramdom)  
    print('Los numeros generados aleatoriamente son: {}'.format(list_random))
    
    
    # El codigo comentado es la manera en la que podemos saber cual es el numero mayor dentro de una lista.
    '''num_mayor = 0
    for i in list_random:
        if i > num_mayor:
            num_mayor = i
        else:
            continue
    print('El numero mayor es {}'.format(num_mayor))''' 
    
    list_random.sort()
    print('El numero mayor es {}'.format(list_random[-1]))
    print('Los numeros organizados son: {}'.format(list_random))

if __name__ == '__main__':
    run()