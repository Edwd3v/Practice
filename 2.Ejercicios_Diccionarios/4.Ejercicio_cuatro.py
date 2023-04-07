
# Escribir un programa que pregunte una fecha en formato dd/mm/aaaa y muestre por pantalla la misma fecha en formato dd de <mes> de aaaa donde <mes> es el nombre del mes.

def run():

    all_monts = {
        '01' : 'Enero',
        '1' : 'Enero',
        '02' : 'Febrero',
        '2' : 'Febrero',
        '03' : 'Marzo',
        '3' : 'Marzo',
        '04' : 'Abril',
        '4' : 'Abril',
        '5' : 'Mayo',
        '05' : 'Mayo',
        '6' : 'Junio',
        '06' : 'Junio',
        '7' : 'Julio',
        '07' : 'Julio',
        '8' : 'Agosto',
        '08' : 'Agosto',
        '9' : 'Septiembre',
        '09' : 'Septiembre',
        '10' : 'Octubre',
        '11' : 'Noviembre',
        '12' : 'Diciembre'
    }

    date = input("Enter today's day(dd/mm/aaaa): ")
    segment_date = date.split('/')

    day = segment_date[0]
    mont = segment_date[1]
    year = segment_date[2]
    mont = all_monts[mont]


    print(f'{day} del mes de {mont} del año {year}')

if __name__ == '__main__':
    run()