# Genera una lista que contenga el doble de cada número en una lista dada.

def run():

    dobel_numbers = [num*2 for num in range (1, 21)]
    print(dobel_numbers)

if __name__ == '__main__':
    run()