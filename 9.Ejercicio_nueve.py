
# Realizar un programa que inicialice una lista con 10 valores aleatorios (del 1 al 10) y posteriormente muestre en pantalla cada elemento de la lista junto con su cuadrado y su cubo.

import random

def run():

    count = 10
    list_numbers = []

    # BUCLE PARA GENERAR LISTA CON NUMEROS ALEATORIOS.
    while len(list_numbers) < 10:
        num_agree = random.randint(1, 99)
        list_numbers.append(num_agree)
        count -= 1

    # UN RETO MINTERESANTE SERIA EVITAR QUE LOS NUMEROS ALEATORIOS SE REPITAN(oviamente debemos tener en cuenta que el rango a seleccionar debe ser mayor a la cantidad de numeros que podamos alamcenar en la lista)

    print(list_numbers)

    # FUNCION PARA HACER LA OPERACIÒN

    def cuadrado_and_cubo():

        for i in list_numbers:
            cuadrado = i**2
            cubo = i**3

            print('El numero {} tiene como cuadrado al {} y como cubo el {}'.format(i, cuadrado, cubo))

    cuadrado_and_cubo()


if __name__ == '__main__':
    run()