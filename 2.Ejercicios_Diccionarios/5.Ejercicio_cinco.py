
# Escribir un programa que almacene el diccionario con los créditos de las asignaturas de un curso {'Matemáticas': 6, 'Física': 4, 'Química': 5} y después muestre por pantalla los créditos de cada asignatura en el formato <asignatura> tiene <créditos> créditos, donde <asignatura> es cada una de las asignaturas del curso, y <créditos> son sus créditos. Al final debe mostrar también el número total de créditos del curso.

def run():

    topics = {
        'Matematicas': 16,
        'Fisica': 4,
        'Quimica': 3,
        'Sociales': 2,
        'Biologia': 3,
        'Ingles':4
    }

    credits = 0
    for topic in topics:
        print(f'La asignatura {topic} tiene {topics[topic]} creditos.')
        credits += topics[topic]
    print(f'El total de creditos es de {credits}')

if __name__ == '__main__':
    run()