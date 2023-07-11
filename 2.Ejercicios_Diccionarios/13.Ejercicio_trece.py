# Dado un diccionario 'personas' que contiene nombres y edades, crea un nuevo diccionario llamado 'mayores_edad' que contenga únicamente las personas que tienen 18 años o más.

def run():

    persons = {'Edward':17, 'Santiago':20, 'Marta':18, 'Lucia':10, 'Sara':17, 'Camilo':19, }
    #adults = { name for name in persons if persons[name] >= 18}
    '''
    Con la siguiente line ade codigo puedo añadir las llaver y los valores.
    '''
    adults = {name: age for name, age in persons.items() if age >= 18}

    print(adults)

if __name__ == '__main__':
    run()