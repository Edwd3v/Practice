# Calcular el cuadrado de un número:
# Escribe una función lambda que tome un número como argumento y devuelva su cuadrado.

def run():

    # Manera larga 
    def squere(a):
        return a**2

    squere_number = lambda a: a**2

    # Manera corta con lambda
    result_1 = squere(2)
    resutl_2 = squere_number(4)

    print(result_1)
    print(resutl_2)

if __name__ == '__main__':
    run()