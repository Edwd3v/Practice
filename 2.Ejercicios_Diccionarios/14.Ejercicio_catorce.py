
# Dado un diccionario 'estudiantes' que contiene nombres y calificaciones, crea un nuevo diccionario llamado 'aprobados' que contenga únicamente los estudiantes que tienen una calificación igual o mayor a 70.

def run():

    students = {
    'Juan': 65,
    'María': 12,
    'Carlos': 78,
    'Laura': 68,
    'Pedro': 76,
    'Ana': 95,
    'Luis': 72,
    'Sofía': 30,
    'Diego': 59,
    'Mónica': 67
}
    approved = {name: qualification for name, qualification in students.items() if qualification >= 70 }
    deprecated = {name: qualification for name, qualification in students.items() if qualification < 70 }
    print('Estudiantes aprobados: ', approved)
    print('Estudiantes desaprobados: ', deprecated)

if __name__ == '__main__':
    run()