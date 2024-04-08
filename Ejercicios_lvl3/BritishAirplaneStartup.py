"""5. British Airplanes Startup

A British start-up specializing in the manufacturing of high-security, high-speed aircraft seeks to calculate the prices of its planes based on the following characteristics: Aircraft size, VIP seats, economy class seats, material quality, security system, and speed level.
Currently, it offers 3 types of aircraft ready for sale.

Wayne Rooney Plane:
Quality AAA
200 economy class seats
70 VIP seats
90 square meters
Security system AAA
Speed level AAA

Eric Cantona Plane:
Quality AAA
150 economy class seats
80 VIP seats
110 square meters
Security system AAA
Speed level AA

Bobby Charlton Plane:
Quality AA
100 economy class seats
40 VIP seats
120 square meters
Security system AA
Speed level A

The AAA material costs £60,000.
The AA material costs £54,000.
The A material costs £48,000.

The AAA security system costs £75,000.
The AA security system costs £68,000.
The A security system costs £59,000.

The AAA speed level costs £89,000.
The AA speed level costs £78,000.
The A speed level costs £70,000.

In the Wayne Rooney and Eric Cantona planes, each economy class seat costs £400, and each VIP seat costs £1200.

In the Bobby Charlton plane, each economy class seat costs £300, and each VIP seat costs £1000"""
from os import system

airplane_type = ['wayne rooney plane', 'eric cantona plane', 'bobby charlton plane']
size = {'wayne rooney plane': 90, 'eric cantona plane': 110, 'bobby charlton plane': 120}
vip_seats = {'wayne rooney plane': (70, 1200), 'eric cantona plane': (80, 1200), 'bobby charlton plane': (40, 1000)}
economy_class_seats = {'wayne rooney plane': (200, 400), 'eric cantona plane': (150, 400), 'bobby charlton plane': (100, 300)}
material_quality = {'wayne rooney plane': ('AAA', 60000), 'eric cantona plane': ('AAA', 60000), 'bobby charlton plane': ('AA', 54000)}
security_system = {'wayne rooney plane': ('AAA', 75000), 'eric cantona plane': ('AAA', 75000), 'bobby charlton plane': ('AA', 68000)}
speed_level = {'wayne rooney plane': ('AAA', 89000), 'eric cantona plane': ('AA', 78000), 'bobby charlton plane': ('A', 70000)}
plane_characteristics = [size, vip_seats, economy_class_seats, material_quality, security_system, speed_level]


def calculate_price(characteristics, type_airplane):
    vip_price = characteristics[1][type_airplane][1] * characteristics[1][type_airplane][0]
    economy_class_price = characteristics[2][type_airplane][1] * characteristics[2][type_airplane][0]
    material_quality_price = characteristics[3][type_airplane][1]
    security_system_price = characteristics[4][type_airplane][1]
    speed_level_price = characteristics[5][type_airplane][1]
    price = vip_price + economy_class_price + material_quality_price + security_system_price + speed_level_price
    return price


def buy_airplane(characteristics):
    while True:
        print('These are the available planes ready for sale')
        for text in airplane_type:
            print(text.title())
        print('If you want to go back to menu, write "back"')
        selection = input('Write the name of the airplane to check characteristics and price: ').lower()
        if selection == 'back':
            return False
        elif selection in airplane_type:
            system('cls')
            price = calculate_price(characteristics, selection)
            print('\x1B[4m' + selection.capitalize() + '\x1B[0m')
            print(f'Size: {characteristics[0][selection]}')
            print(f'VIP seats: {characteristics[1][selection][0]}')
            print(f'Economy class seats: {characteristics[2][selection][0]}')
            print(f'Material quality: {characteristics[3][selection][0]}')
            print(f'Security system: {characteristics[4][selection][0]}')
            print(f'Speed Level: {characteristics[5][selection][0]}')
            print(f'Total price: £{price}')
            confirm = input('Write "confirm" if you want to buy this airplane model, if you don\'t press any other key: ')
            if confirm == 'confirm':
                system('cls')
                print(f'The airplane has been purchased succesfully for a price of £{price}')
                input('Press any key to continue')
                return False
            else:
                system('cls')
                continue
        else:
            system('cls')
            print('\x1B[4mEnter a valid option\x1B[0m')


def main():
    while True:
        print('Welcome to the airplane shop program')
        print('1. See available airplanes')
        print('2. End program')
        action = input('Select an option: ')
        if action == '1':
            system('cls')
            buy_airplane(plane_characteristics)
            system('cls')
        elif action == '2':
            system('cls')
            print('Thanks for buying with our system')
            return False
        else:
            system('cls')
            print('\x1B[4mEnter a valid option\x1B[0m')


if __name__ == '__main__':
    main()
