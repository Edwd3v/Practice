# Comprobar si un número es par:
# Crea una función lambda que tome un número como entrada y devuelva True si es par y False si es impar.

def run():

    number = int(input('Write a number: '))

    # Manera larga
    def pair_or_odd(number):
        if number % 2 == 0:
            return True
        else:
            return False

    result = pair_or_odd(number)
    print(result)

    # Manera corta con Lambda
    is_pair = lambda a: True if a % 2 == 0 else False
    result_2 = is_pair(number)
    print(result_2)


if __name__ == '__main__':
    run()