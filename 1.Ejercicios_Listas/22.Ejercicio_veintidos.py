# Dada una lista de números, crea una lista que contenga solo los elementos mayores a 5. 

def run():
    
    numbers = []

    for num in range(1, 16):
        if num > 5:
            numbers.append(num)
    print(numbers)

    numbers_2 = [num for num in range(1, 16) if num > 5]
    print(numbers_2)

if __name__ == '__main__':
    run()