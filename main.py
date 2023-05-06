from Lista import lista
from ClassPlanAhorro import PlanAhorro


def menu():
    print('a. Actualizar el valor del vehículo de cada plan.')
    print('b. Mostrar código del plan, modelo y versión del vehículo cuyo valor de la cuota sea inferior al valor ingresado.')
    print('c. Mostrar el monto que se debe haber pagado para licitar el vehículo.')
    print('d. Dado el código de un plan, modificar la cantidad cuotas que debe tener pagas para licitar.')
    print('e. Salir')


def funciones():
    m = lista()
    m.testlista()
    menu()
    opc = input('Ingrese una opcion: ')
    while opc != 'e':

        if opc == 'a':
            m.actualizar()
            m.mostrar()
        elif opc == 'b':
            valor = float(input('Ingrese el valor: '))
            m.mostrar_plan_cuota_inf(valor)
        elif opc == 'c':
            cuota = float(input('Ingrese el importe de la cuota: '))
            monto = PlanAhorro.monto_licitacion(cuota)
            print(f'Monto para licitar: {monto}')
        elif opc == 'd':
            cod_plan = input('Ingrese el código del plan: ')
            nuevas_cuotas = int(input('Ingrese la nueva cantidad de cuotas para licitar: '))
            m.modificar_cuotas_licitar(cod_plan, nuevas_cuotas)

        opc = input('Ingrese una opcion: ')


if __name__ == '__main__':
    funciones()
