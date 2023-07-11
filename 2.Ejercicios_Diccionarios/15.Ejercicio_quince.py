# Dado un diccionario 'precios' que contiene nombres de productos y sus respectivos precios, crea un nuevo diccionario llamado 'descuentos' que aplique un descuento del 10% a cada precio.

def run():

    prices = {
    'Manzanas': 1000,
    'Plátanos': 3200,
    'Naranjas': 2500,
    'Peras': 5300,
    'Uvas': 3500,
    'Fresas': 4400,
    'Sandías': 6500,
    'Melones': 5000,
    'Piñas': 3800,
    'Mangos': 2700
}

    discount = {product: price - (price * 0.1) for product, price in prices.items()}
    print(discount)

if __name__ == '__main__':
    run()