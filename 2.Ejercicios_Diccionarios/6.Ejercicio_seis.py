
# Escribir un programa que cree un diccionario vacío y lo vaya llenado con información sobre una persona (por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.) que se le pida al usuario. Cada vez que se añada un nuevo dato debe imprimirse el contenido del diccionario.

def run():

    information = {
    }
    dates = ['Name', 'Age', 'Gender', 'Tel', 'E-mail', 'Address', 'Profetion', 'Favorite color']

    def add_dates():
        for i in dates:
            value = input(f'{i}: ')
            information[i] = value   
    add_dates()

    print(information)

if __name__ == '__main__':
    run()