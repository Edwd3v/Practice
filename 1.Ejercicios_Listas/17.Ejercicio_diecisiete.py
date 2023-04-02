# Queremos guardar la temperatura mínima y máxima de 5 días. Realiza un programa que de la siguiente información:

# 1. La temperatura media de la semana
# 2. Los días con menos temperatura (menores a 10)
# 3. Dias con la misma temeratura. Si no existe ningún día se muestra un mensaje de información.

def run():

    days = {
    'Monday':'', 
    'Tuesday':'', 
    'Wednesday':'', 
    'Thursday':'', 
    'Friday':'', 
    'Saturday':'', 
    'Sunday':''
    }

    # Convertimos nuestro diccionario en una lista para poder manipularlo mas facilmente
    list_days = list(days.keys())
    
    # Tomamos las temperaturas registradas en cada uno de los dias.
    mind_temeperature = 0
    for day in list_days:
        Temperature_of_days = float(input('What was the temperature on {}?: '.format(day)))
        # Esta linea nos agreca el value en cada key de nuestro diccionario
        days[day] = Temperature_of_days

    # 1. La temperatura media de la semana
        mind_temeperature += Temperature_of_days
    print('Average: {}'.format(round(mind_temeperature/len(days)))) 
    # Guardamos en una lista los valores ingresados por es usuario.
    list_values = list(days.values())   
    
    # 2. Los días con menos temperatura (menores a 10)
    lower_tempetature = {}
    for temperature in days:
        valor = days[temperature]
        if valor <= 10:
            lower_tempetature[temperature] = valor
        else:
            continue
    print('lower temperature (below 10º): ',lower_tempetature)

    # 3. Dias con la misma temeratura. Si no existe ningún día se muestra un mensaje de información.
    temperature_repit = {}
    for temperature in days:
        valor = days [temperature]
        if list_values.count(valor) > 1:          
            temperature_repit[temperature] = valor
        else:
            continue  

    if len(temperature_repit) == 0:
            print('There are no days with repeated temperature')
    elif len(temperature_repit) > 0:      
        print('repit temperature: ', temperature_repit)


if __name__ == '__main__':
    run()
