
# Crea una lista e inicializala con 5 cadenas de caracteres leídas por teclado. Copia los elementos de la lista en otra lista pero en orden inverso, y muestra sus elementos por la pantalla.

def run():

    def invers_strings():
        number_string = 1
        cont = 5
        list_string = []
        invers_list_string = []

        while cont > 0:
            string = input('Ingresa el string {}: '.format(number_string))
            list_string.append(string)
            cont -= 1
            number_string += 1
        
        for i in reversed(list_string):
            invers_list_string.append(i)

        print(list_string)
        print('La lista de invertida es {}'.format(invers_list_string)) 
    
    invers_strings()

if __name__ == '__main__':
    run()