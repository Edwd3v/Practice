
# Crea un programa que pida un número al usuario (un número de mes, por ejemplo, el 4) y diga cuántos días tiene (por ejemplo, 30) y el nombre del mes. Debes usar listas. Para simplificarlo vamos a suponer que febrero tiene 28 días.

# Todos los meses tienen 30 dias con esepcion de febrero



def run():

    months = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']

    requesrtes_month = int(input('Ingrese el numero del mes: '))
    requesrtes_month -= 1
    position = months[requesrtes_month]
    #print(position)

    for i in months:
        if requesrtes_month != 1:
            print('El mes de {} tiene 30 dias.'.format(position))
            break            
        else:
            print('El mes de Febrero tiene 28 dias.')
            break   

if __name__ == '__main__':
    run()