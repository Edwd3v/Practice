
# Escribir un programa que cree un diccionario simulando una cesta de la compra. El programa debe preguntar el artículo y su precio y añadir el par al diccionario, hasta que el usuario decida terminar. Después se debe mostrar por pantalla la lista de la compra y el coste total, con el siguiente formato.

import random

def run():

    shopping_list = {

    }
    
    def enter_dates ():
        while True:
            item = input('''
What item did you purchase? 
    If this the last item enter "*"
    : ''')
            if item != '*':
                #value = random.randint(1, 100)
                value = random.uniform(1, 100)
                value = round(value,2)
                shopping_list [item] = value

            else:
                payment = 0
                for price in shopping_list.values():
                    payment += price
                shopping_list ['TOTAL'] = payment
                print("{:<12} {:<12}".format("ITEM", "VALUE"))
                for key, val in shopping_list.items():
                    print("{:<12} {}{:<12}".format(key,'$ ',val))
                break

    enter_dates()

if __name__ == '__main__':
    run()