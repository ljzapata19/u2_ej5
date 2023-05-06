from ClassPlanAhorro import PlanAhorro
import csv


class lista:

    def __init__(self):
        self.__lista = []

    def testlista(self):
        archivo = open('planes.csv')
        reader = csv.reader(archivo, delimiter=';')
        for fila in reader:
            f = fila
            plan = PlanAhorro(f[0], f[1], f[2], f[3])
            self.__lista.append(plan)
        archivo.close()

    def __str__(self):
        s = ""
        for plan in self.__lista:
            s += str(plan) + '\n'
        return s

    def actualizar(self):
        for plan in self.__lista:
            print(plan)
            nuevo_valor = input('Ingrese nuevo valor para modificarlo en el plan: ')
            plan.actualizar_valor(nuevo_valor)

    def mostrar_plan_cuota_inf(self, valor):
        for plan in self.__lista:
            if plan.valor_cuota() < valor:
                print(plan)

    def modificar_cuotas_licitar(self, cod_plan, nuevas_cuotas):

        i = 0
        while i < len(self.__lista):
            if self.__lista[i].get_cod() == cod_plan:
                self.__lista[i].set_cant_cuotas_licitar(nuevas_cuotas)

            i += 1

    def mostrar(self):
        for plan in self.__lista:
            print(plan)