# Filtra los números pares de una lista dada. 

def run():

    '''
    numbers = []
    for num in range(1, 21):
        if num % 2 == 0:
            numbers.append(num)
    print(numbers)
    '''

    numbers = [num for num in range(1, 21) if num % 2 == 0]
    print(numbers)

if __name__ == '__main__':
    run()