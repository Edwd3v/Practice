
# Se quiere realizar un programa que lea por teclado las 5 notas obtenidas por un alumno (comprendidas entre 0 y 10). A continuación debe mostrar todas las notas, la nota media, la nota más alta que ha sacado y la menor.

def run():

    topics = ['Matematicas', 'Sociales', 'Ciencias Naturales', 'Artes', 'Ingles']
    

    def topics_notes():

        calificaciones = []
        for i in topics:
            note = float(input('¿Cual fue tu nota en {} ?: '.format(i)))
            calificaciones.append(note)
            #print(calificaciones)
            
        calificaciones.sort()
        print(calificaciones)
        
        promedio = 0
        for i in calificaciones:
            promedio += i
        promedio = promedio/len(calificaciones)
        

        print('Tu mayor nota es {}'.format(calificaciones[-1]))
        print('Tu menor nota es {}'.format(calificaciones[0]))
        print('Tu nota promedio es {}'.format(promedio))

    topics_notes()

if __name__ == '__main__':
    run()