# Crea una lista que contenga los elementos comunes entre dos listas dadas.

def run():

    enter_numbers = [num for num in range (1, 11)]
    par_numbers = [num for num in range(1, 11) if num % 2 == 0]

    fusion = [element for element in enter_numbers if element in par_numbers]
    print(fusion)


if __name__ == '__main__':
    run()