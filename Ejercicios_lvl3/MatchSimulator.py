"""Manchester United Line Up

You are the Manager of Manchester United FC, and your objective is to defeat Tottenham Hotspur. To achieve this, you must consider the power level of your players and choose the appropriate line-up against your opponent. Select 11 players from your team.

Tottenham Hotspur:
Goalkeepers

Hugo Lloris 85 pts
Guglielmo Vicario 79 pts
Fraser Forster 79 pts
Brandon Austin 79 pts

Defenders
Eric Dier 80 pts
Cristian Romero 80 pts
Davinson Sánchez 74 pts
Japhet Tanganga 70 pts
Matt Doherty 70 pts
Djed Spence 70 pts
Sergio Reguilón 74 pts
Ben Davies 76 pts
Joe Rodon 70 pts
Mislav Orsic 71 pts

Midfielders
Oliver Skipp 70 pts
Pierre-Emile Højbjerg 70 pts
Yves Bissouma 72 pts
James Maddison 74 pts
Giovani Lo Celso 78 pts
Ryan Sessegnon 80 pts
Dejan Kulusevski 60 pts
Pape Sarr 65 pts
Rodrigo Bentancur 65 pts
Oliver Skipp 65 pts

Forwards
Son Heung-Min 78 pts
Richarlison 82 pts
Bryan Gil 80 pts
Timo Werner 82 pts
Brennan Johnson 70 pts
Manor Solomon 70 pts
Alejo Véliz 75 pts
Dane Scarlett 75 pts

Manchester United:
Goalkeepers

André Onana 80 pts
Tom Heaton 75 pts
Altay Bayindir 69 pts

Defenders
Victor Lindelöf 80 pts
Harry Maguire 82 pts
Lisandro Martínez 82 pts
Tyrell Malacia 67 pts
Raphaël Varane 80 pts
Diogo Dalot 89 pts
Luke Shaw 89 pts
Aaron Wan-Bissaka 70 pts

Midfielders
Sofyan Amrabat 76 pts
Scott McTominay 80 pts
Bruno Fernandes 88 pts
Christian Eriksen 67 pts
Mason Mount 77 pts
Kobbie Mainoo 65 pts
Daniel Gore 60 pts

Forwards
Anthony Martial 50 pts
Marcus Rashford 76 pts
Antony 75 pts
Rasmus Højlund 80 pts
Alejandro Garnacho 85 pts
Facundo Pellistri: 75 pts
How it works: The system will randomly generate 11 Tottenham Hotspur players, comprising 1 goalkeeper, 4 defenders, 3 midfielders, and 3 strikers.

As the Manager of Manchester United, you must select 11 players following the same system: 4-3-3."""
import random
from os import system
import numpy as np

tottenham = [{'Hugo Lloris': 85, 'Guglielmo Vicario': 79, 'Fraser Forster': 79, 'Brandon Austin': 79},
             {'Eric Dier': 80, 'Cristian Romero': 80, 'Davinson Sanchez': 74, 'Japhet Tanganga': 70, 'Matt Doherty': 70,
              'Djed Spence': 70, 'Sergio Reguilon': 74, 'Ben Davies': 76, 'Joe Radon': 70, 'Mislav Orsic': 71},
             {'Oliver Skipp': 70, 'Pierre-Emile Højbjerg': 70, 'Yves Bissouma': 72, 'James Maddison': 74, 'Giovani Lo Celso': 78, 'Ryan Sessegnon': 80, 'Dejan Kulusevski': 60,
              'Pape Sarr': 65, 'Rodrigo Bentancur': 65},
             {'Son Heung-Min': 78, 'Richarlison': 82, 'Bryan Gil': 80, 'Timo Werner': 82, 'Brennan Johnson': 70, 'Manor Solomon': 70, 'Alejo Veliz': 75, 'Dane Scarlett': 75}]

manchester_united = [{'Andre Onana': (80, 0), 'Tom Heaton': (75, 0), 'Altay Bayindir': (69, 0)},
                     {'Victor Lindelof': (80, 1), 'Harry Maguire': (82, 1), 'Lisandro Martinez': (82, 1),
                      'Tyrell Malacia': (67, 1), 'Raphael Varane': (80, 1), 'Diogo Dalot': (89, 1), 'Luke Shaw': (89, 1), 'Aaron Wan-Bissaka': (70, 1)},
                     {'Sofyan Amrabat': (76, 2), 'Scott McTominay': (80, 2), 'Bruno Fernandes': (88, 2), 'Christian Eriksen': (67, 2), 'Mason Mount': (77, 2), 'Kobbie Mainoo': (65, 2),
                      'Daniel Gore': (60, 2)},
                     {'Anthony Martial': (50, 3), 'Marcus Rashford': (76, 3), 'Antony': (75, 3), 'Rasmun Hojlund': (80, 3), 'Alejandro Garnacho': (85, 3), 'Facundo Pellistri': (75, 3)}]
nombres_mujugadores = ['Andre Onana', 'Tom Heaton', 'Altay Bayindir', 'Victor Lindelof', 'Harry Maguire', 'Lisandro Martinez', 'Tyrell Malacia', 'Raphael Varane', 'Diogo Dalot', 'Luke Shaw',
                       'Aaron Wan-Bissaka', 'Sofyan Amraba', 'Scott McTominay', 'Bruno Fernandes', 'Christian Eriksen', 'Mason Mount', 'Kobbie Mainoo', 'Daniel Gore',
                       'Anthony Martial', 'Marcus Rashford', 'Antony', 'Rasmun Hojlund', 'Alejandro Garnacho', 'Facundo Pellistri', 'back']
jugadores_random = np.array([[dict(random.sample(list(tottenham[0].items()), 1))],
                             [dict(random.sample(list(tottenham[1].items()), 4))],
                             [dict(random.sample(list(tottenham[2].items()), 3))],
                             [dict(random.sample(list(tottenham[3].items()), 3))]])
plantilla_tottenham = jugadores_random.reshape(-1)
plantilla_mu = [{}, {}, {}, {}]


def puntaje_total(jugadores):
    puntajes = []
    for posicion in jugadores:
        for value in posicion.values():
            puntajes.append(value)
    return sum(puntajes)


puntaje_total_tottenham = puntaje_total(plantilla_tottenham)
textos = ['Portero', 'Defensas', 'Mediocampistas', 'Delantero']


def verificador(plantilla_jugadores, posicion):
    match posicion:
        case 0:
            if len(plantilla_jugadores[0]) == 1:
                return False
            else:
                return True
        case 1:
            if len(plantilla_jugadores[1]) == 4:
                return False
            else:
                return True
        case 2:
            if len(plantilla_jugadores[2]) == 3:
                return False
            else:
                return True
        case 3:
            if len(plantilla_jugadores[3]) == 3:
                return False
            else:
                return True


def agregar_jugador(jugadores):
    while True:
        indice = 0
        for posicion in jugadores:
            print("\x1B[4m" + textos[indice] + "\x1B[0m")
            for key, value in posicion.items():
                print(f'{key}: {value[0]}pts')
            indice += 1
        print('\nSi desea volver al menu escriba "back"')
        jugador_elegido = input('Escriba el nombre del jugador que desea incluir en la plantilla titular: ')
        try:
            nombres_mujugadores.index(jugador_elegido)
        except ValueError:
            system('cls')
            print('\x1B[4mEste jugador no existe\x1B[0m\n')
        else:
            if jugador_elegido == 'back':
                return False
            else:
                for posicion in jugadores:
                    if jugador_elegido in posicion.keys():
                        indice_dic = posicion[jugador_elegido][1]
                        if verificador(plantilla_mu, indice_dic):
                            posicion_actual = plantilla_mu[indice_dic]
                            posicion_actual[jugador_elegido] = posicion[jugador_elegido][0]
                            del posicion[jugador_elegido]
                            system('cls')
                            print('El jugador ha sido agregado a la plantilla exitosamente')
                            input('Presione cualquier tecla para volver al menu')
                            return False
                        else:
                            system('cls')
                            print('\x1B[4mEsta posición de jugador tiene todos sus integrantes\x1B[0m')
                    else:
                        continue


def contar_jugadores(jugadores):
    cantidad_jugadores = 0
    for posicion in jugadores:
        for _ in posicion.keys():
            cantidad_jugadores += 1
    return cantidad_jugadores


def eliminar_jugador(jugadores):
    while True:
        indice = 0
        for posicion in jugadores:
            print("\x1B[4m" + textos[indice] + "\x1B[0m")
            for key, value in posicion.items():
                print(f'{key}: {value}pts')
            indice += 1
        print('\nSi desea volver al menu escriba "back"')
        jugador_elegido = input('Escriba el nombre del jugador que desea eliminar de la plantilla titular: ')
        try:
            nombres_mujugadores.index(jugador_elegido)
        except ValueError:
            system('cls')
            print('\x1B[4mEste jugador no existe\x1B[0m\n')
        else:
            if jugador_elegido == 'back':
                return False
            else:
                indice_posicion = 0
                for posicion in jugadores:
                    if jugador_elegido in posicion.keys():
                        puntos = posicion[jugador_elegido]
                        dic_posicion = manchester_united[indice_posicion]
                        dic_posicion[jugador_elegido] = (puntos, indice_posicion)
                        del posicion[jugador_elegido]
                        system('cls')
                        print('El jugador ha sido removido de la plantilla titular exitosamente')
                        input('Presione cualquier tecla para continuar')
                        return False
                    else:
                        indice_posicion += 1
                        continue


def plantilla():
    print('\x1B[4mPlantilla del Tottenham Hotspur\x1B[0m\n')
    indice = 0
    for posicion in plantilla_tottenham:
        print("\x1B[4m" + textos[indice] + "\x1B[0m")
        for key, value in posicion.items():
            print(f'{key}: {value}pts')
        indice += 1


def manchesteru_plantilla():
    print('\x1B[4mPlantilla del Manchester United\x1B[0m\n')
    indice = 0
    for posicion in plantilla_mu:
        print("\x1B[4m" + textos[indice] + "\x1B[0m")
        for key, value in posicion.items():
            print(f'{key}: {value}pts')
        indice += 1


def jugar(puntaje1, puntaje2, cantidad_jug):
    if cantidad_jug == 11:
        if puntaje1 > puntaje2:
            goles2 = random.randint(0, 3)
            goles1 = goles2 + random.randint(1, 3)
            print('Estos son los resultados finales del partido jugado:')
            print(f'Manchester United - {goles1} VS {goles2} -   Tottenham Hotspur')
        elif puntaje1 < puntaje2:
            goles1 = random.randint(0, 3)
            goles2 = goles1 + random.randint(1, 3)
            print('Estos son los resultados finales del partido jugado:')
            print(f'Manchester United - {goles1} VS {goles2} - Tottenham Hotspur')
        else:
            goles2 = random.randint(0, 5)
            goles1 = random.randint(0, 5)
            print('Estos son los resultados finales del partido jugado:')
            print(f'Manchester United - {goles1} VS {goles2} - Tottenham Hotspur')
    else:
        system('cls')
        print('Tu plantilla no posee la cantidad de jugadores necesarios para jugar')
        return


def main():
    system('cls')
    while True:
        puntaje_mu = puntaje_total(plantilla_mu)
        cantidad_jug = contar_jugadores(plantilla_mu)
        print('\x1B[4mCrea tu plantilla del Manchester United para derrotar al Tottenham!!!\x1B[0m')
        print(f'Actualmente la suma de los puntajes totales es tal que:\nTot {puntaje_total_tottenham}pts vs {puntaje_mu}pts MU')
        print('Vas a necesitar una formación de 1-4-3-3')
        print('1. Revisar plantilla del Tottenham Hotspur')
        print('2. Agregar jugadores a plantilla del Manchester United')
        print('3. Revisar plantilla actual del Manchester United')
        print('4. Remover jugador de plantilla titular')
        print('5. Jugar partido')
        print('6. Salir del programa')
        eleccion = input('Elige una opción: ')
        if eleccion == '1':
            system('cls')
            plantilla()
            input('\nPresione cualquier tecla para volver al menu')
            system('cls')
        elif eleccion == '2':
            system('cls')
            agregar_jugador(manchester_united)
            system('cls')
        elif eleccion == '3':
            system('cls')
            manchesteru_plantilla()
            input('\nPresione cualquier tecla para volver al menu')
            system('cls')
        elif eleccion == '4':
            system('cls')
            eliminar_jugador(plantilla_mu)
            system('cls')
        elif eleccion == '5':
            system('cls')
            jugar(puntaje_mu, puntaje_total_tottenham, cantidad_jug)
            input('Presione cualquier tecla para volver al menu ')
            system('cls')
        elif eleccion == '6':
            system('cls')
            print('El prograna ha sido finalizado, gracias por usar el simulador')
            return False
        else:
            system('cls')
            print('\x1B[4mOpción invalida\x1B[0m\n')


if __name__ == '__main__':
    main()
