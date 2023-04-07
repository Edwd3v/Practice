
# Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, pregunte al usuario por una fruta, un número de kilos y muestre por pantalla el precio de ese número de kilos de fruta. Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello.

# FRUTA     PRECIO
# Platano   1.35
# Manzana   0.80
# Pera      0.85
# Naranja   0.70

def run():

    fruts = {
        'Platano': 1.35,
        'Manzana': 0.80,
        'Pera': 0.85,
        'Naranja': 0.70
        }

    your_frut = input('''

    WELCOME!!!

    FRUTA     PRECIO
    Platano   1.35
    Manzana   0.80
    Pera      0.85
    Naranja   0.70               
                      
                      
    What you want fruit?: '''             
    )

    your_frut = your_frut.capitalize()
   
    while your_frut not in fruts:
        print('The selected fruit is not available')
        your_frut = input('What you want fruit?: ')
        your_frut = your_frut.capitalize()

    if your_frut in fruts:
        weigth = float(input('''
    How many KG you want?: '''))
        print(f'''
    You have to pay $ {round(weigth*fruts[your_frut])}
        ''')

if __name__ == '__main__':
    run()