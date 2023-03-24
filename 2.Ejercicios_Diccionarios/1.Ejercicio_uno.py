
# Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥', 'Renminbi':'元', 'Won':'₩'}, pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso si la divisa no está en el diccionario

def run():

    divisa = {
        'Euro':'€', 
        'Dollar':'$', 
        'Yen':'¥', 
        'Renminbi':'元', 
        'Won':'₩'
    }

    your_divisa = input(
    '''
    ¡BIENVENIDO!
    ¿De cual divisa deseas saber el simbolo?
    
    - Euro
    - Dollar
    - Yen
    - Renminbi
    - Won

    : ''')
    your_divisa = your_divisa.capitalize()
    #print(your_divisa)

    print(
        '''
    El simbolo de tu divisa es: {}
        '''.format(divisa[your_divisa]))

    #print('El simbolo de tu divisa es: {}'.format(divisa.get[your_divisa]))
    #print('El simbolo de tu divisa es: {}'.format(divisa.get[your_divisa]))


if __name__ == '__main__':
    run()