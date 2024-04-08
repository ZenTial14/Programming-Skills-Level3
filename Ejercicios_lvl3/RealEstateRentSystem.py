"""3. Real State Rent System


A real estate agency has 5 homes for rent. The homes are characterized by their size, number of bedrooms, number of bathrooms, and location. The rental price of a home is calculated based on these factors.
Features:

First home: 200 square meters, 3 bedrooms, 2 bathrooms
Second home: 150 square meters, 2 bedrooms, 2 bathrooms
Third home: 100 square meters, 2 bedrooms, 1 bathroom
Fourth home: 100 square meters, 1 bedroom, 2 bathrooms
Fifth home: 80 square meters, 1 bedroom, 1 bathroom
The program must quote the price of the home according to: square meters, number of bedrooms, and number of bathrooms. Each bedroom adds $40, and each bathroom adds $30.
Each square meter has a cost of $90."""
from os import system


class Casa:
    def __init__(self, numero_casa, metros_cuadrados, habitaciones, banos):
        self.numero_casa = numero_casa
        self.metros_cuadrados = metros_cuadrados
        self.habitaciones = habitaciones
        self.banos = banos


casa_a = Casa('Casa A', 200, 3, 2)
casa_b = Casa('Casa B', 150, 2, 2)
casa_c = Casa('Casa C', 100, 2, 1)
casa_d = Casa('Casa D', 100, 1, 2)
casa_e = Casa('Casa E', 50, 1, 1)
lista_casas = [casa_a, casa_b, casa_c, casa_d, casa_e]
casa_rentada = []


def calcular_precio(casa):
    metros = casa.metros_cuadrados
    habitaciones = casa.habitaciones
    banos = casa.banos
    precio_final = (90 * metros) + (40 * habitaciones) + (30 * banos)
    return precio_final


def rentar_casas(casas):
    while True:
        tipos_casas = []
        print('¿Cual de la siguientes casas desea rentar?')
        for casa in casas:
            tipos_casas.append(casa.numero_casa)
            precio = calcular_precio(casa)
            print(f'{casa.numero_casa}: {casa.metros_cuadrados}mts², {casa.habitaciones} habitaciones, {casa.banos} baños  -- Precio Total: {precio}$')
        try:
            casa_elegida = input('')
            indice = tipos_casas.index(casa_elegida)
        except ValueError:
            system('cls')
            print('\x1B[4mElige una opción correcta\x1B[0m')
        else:
            if len(casa_rentada) == 0:
                casa_rentada.append(casas[indice])
                system('cls')
                print(f'La casa ha sido rentada exitosamente al precio de {calcular_precio(casas[indice])}$')
                input('Presione cualquier tecla para continuar')
                return False
            else:
                system('cls')
                print('Actualmente ya hay una casa rentandose')
                input('Presione cualquier tecla para continuar')
                return False


def mostrar_renta(renta_actual):
    if len(casa_rentada) == 1:
        textos = []
        for casa in lista_casas:
            textos.append(casa.numero_casa)
        casa = renta_actual[0]
        print(f'La casa rentada actualmente es la {casa.numero_casa}, sus características son:')
        print(f'Metros cuadrados: {casa.metros_cuadrados}mts²')
        print(f'Habitaciones: {casa.habitaciones}')
        print(f'Baños: {casa.banos}')
        print(f'Precio: {calcular_precio(casa)}$')
        print('Si desea cancelar la renta escriba "cancelar"')
        accion = input('Si no es asi, presione cualquier tecla para continuar: ')
        if accion == 'cancelar':
            casa_rentada.pop()
            system('cls')
            print('La renta ha sido cancelada exitosamente')
            input('Presione cualquier tecla para continuar')
        else:
            system('cls')
    else:
        system('cls')
        print('Actualmente no hay ninguna casa rentada')
        input('Presione cualquier tecla para continuar')


def main():
    while True:
        print('\x1B[4m' + 'Bienvenido al programa de renta de nuestra agencia' + '\x1B[0m')
        print('1. Ver casas disponibles para rentar')
        print('2. Ver casa rentada actualmente')
        print('3. Finalizar programa')
        accion = input('Elige una opción: ')
        if accion == '1':
            system('cls')
            rentar_casas(lista_casas)
            system('cls')
        elif accion == '2':
            system('cls')
            mostrar_renta(casa_rentada)
            system('cls')
        elif accion == '3':
            system('cls')
            print('Gracias por usar nuestro programa')
            print('El programa ha sido finalizado exitosamente')
            return False
        else:
            system('cls')
            print('\x1B[4mElige una opción correcta\x1B[0m\n')


if __name__ == '__main__':
    main()
