
# Crea una lista que contenga el producto de los elementos correspondientes de dos listas dadas.

def run():

    list_1 = [5, 3, 2, 8, 7]
    list_2 = [1, 7, 9, 4, 2]
    product_list = []
    
    n = 0
    for num in list_1:
        x = num*list_2[n]
        product_list.append(x)
        n += 1
    print(product_list)

    #product_list_2 = [num*list_2[n] for num in list_1]
    #print(product_list_2)

    '''
    for element_1 in list_1:
        for element_2 in list_2:
            x = element_1*element_2
            product_list.append(x)
            list_1.remove(element_1)
            list_2.remove(element_2)
    print(product_list)
    '''

    

if __name__ == '__main__':
    run()