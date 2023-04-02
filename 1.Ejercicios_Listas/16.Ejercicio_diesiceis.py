# Queremos guardar los nombres y la edades de los alumnos de un curso. Realiza un programa que introduzca el nombre y la edad de cada alumno. El proceso de lectura de datos terminará cuando se introduzca como nombre un asterisco (*) Al finalizar se mostrará los siguientes datos:

    # Todos lo alumnos mayores de edad.
    # Los alumnos mayores (los que tienen más edad > 30 años) 

def run ():

    old = []
    adult = []
    kids = []

    while True:
        name = input('Ingrese el nombre del estudiante: ')
        if name != '*':
            age = int(input('Ingrese la edad del estudiante {}: '.format(name)))
            if age < 18:
                kids.append(name)
            elif age >= 18 and age < 30:
                adult.append(name)
            elif age > 30:
                old.append(name)
            else:
                print('FINALIZADO')
        
        else:
            print('Los niños son {}'.format(kids))
            print('Los adultos mayores de 18 años son {}'.format(adult))
            print('Los adultos mayores de 30 años son {}'.format(old))
            break

if __name__ == '__main__':
    run()