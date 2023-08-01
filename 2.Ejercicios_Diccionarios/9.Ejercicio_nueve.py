#
# Escribir un programa que gestione las facturas pendientes de cobro de una empresa. Las facturas se almacenarán en un diccionario donde la clave de cada factura será el número de factura y el valor el coste de la factura. El programa debe preguntar al usuario si quiere añadir una nueva factura, pagar una existente o terminar. Si desea añadir una nueva factura se preguntará por el número de factura y su coste y se añadirá al diccionario. Si se desea pagar una factura se preguntará por el número de factura y se eliminará del diccionario. Después de cada operación el programa debe mostrar por pantalla la cantidad cobrada hasta el momento y la cantidad pendiente de cobro.

def run ():
    
    invoices = {

    }

    sum_values_invoices = 0

    def data_manipulation ():

        while True:
            action = input('''
    What do you want to do?

        1 - Add: add invoice
        2 - Delete: Delete invoice
        3 - Pay: Pay invoice
        4 - Finish

: ''')
            action = action.upper()

            # Añadir facturas
            if action == '1' or action == 'ADD':
                # Se añaden los respectivos ceros a la izquierda del numero de nuestra factura
                invoice_number =input('Invoice Number to Add: ').zfill(6)
                # Añadimos el valor de nuestra factura como value en nuestro diccionario
                invoice_value = int(input('Invoice Value: ')) 
                invoices [invoice_number] = invoice_value
                # print(invoices)
                sum_values_invoices = sum(invoices.values()) 
                print('TOTAL TO PAY: $', sum_values_invoices)

            # Eliminar Facturas
            elif action == '2' or action == 'DELETE':
                number_invoices_to_deleted = input('Invoice Number to Deleted: ').zfill(6)

                if number_invoices_to_deleted in invoices:
                    del invoices [number_invoices_to_deleted]
                    #print(invoices)
                    sum_values_invoices = sum(invoices.values())
                    print('TOTAL TO PAY: $', sum_values_invoices)
                else:
                    print('The rerequested invoice does not exist or was not found.')
                    #print(invoices)
                    sum_values_invoices = sum(invoices.values())
                    print('TOTAL TO PAY: $', sum_values_invoices)
            
            # Pago de facturas
            elif action == '3' or action == 'PAY':
                number_invoices_to_pay = input('Invoice Number to Pay: ').zfill(6)
                
                if number_invoices_to_pay in invoices:
                    del invoices [number_invoices_to_pay]
                    #print(invoices)
                    sum_values_invoices = sum(invoices.values())
                    print('TOTAL TO PAY: $', sum_values_invoices)
                else:
                    print('The rerequested invoice does not exist or was not found.')
                    #print(invoices)
                    sum_values_invoices = sum(invoices.values())
                    print('TOTAL TO PAY: $', sum_values_invoices)

           elif action == '4' or action == 'FINISH':
                sum_values_invoices = sum(invoices.values())
                print(invoices)
                print('TOTAL TO PAY: $', sum_values_invoices)
                break

            else:
                continue

    data_manipulation()
    
if __name__ == '__main__':
    run()
