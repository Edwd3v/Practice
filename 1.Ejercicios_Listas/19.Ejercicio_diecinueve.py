# Crea una lista con los cuadrados de los números del 1 al 10.

def run():
    numbers = []

    '''for num in range (1, 21):
        numbers.append(num**2)
    print(numbers)
    '''

    numbers = [num**2 for num in range(1, 11)]
    print(numbers)

if __name__ == '__main__':
    run()