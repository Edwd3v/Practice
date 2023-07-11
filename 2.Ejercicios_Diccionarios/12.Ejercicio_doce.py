# La composición de un Dictionary Comprehension es:
# {key:value for var in interable}

# Dado un diccionario 'numeros' que contiene pares clave-valor, crea un nuevo diccionario llamado 'cuadrados' que contenga las claves del diccionario original y los valores correspondientes elevados al cuadrado.


def run():

    numbers = { 1 : 1, 2 : 2, 3 : 3,  4 : 4,  5 : 5}
    cuadrados = {num:num**2 for num in numbers}

    print(cuadrados)

if __name__ == '__main__':
    run()
