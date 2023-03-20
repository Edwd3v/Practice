
# Programa que declare una lista y la vaya llenando de números hasta que introduzcamos un número negativo. Entonces se debe imprimir el vector (sólo los elementos introducidos).

def run():

    list_numbers = []

    while True:
        number = int(input('Ingrese un numero: '))
        if number >= 0:
            list_numbers.append(number)
        else:    
            print('La lista generada es: {}'.format(list_numbers))
            break
    
if __name__ == '__main__':
    run()