"""2. Amazon Software Engineer

Amazon has hired you as a software engineer. Your first task is to create a system that allows calculating the price of shipping based on distance. Fulfill the following requirements:
Amazon has one branch in each state of the USA.
Research the approximate distance between each pair of states.
The price is $50 USD per kilometer.
The minimum number of packages to transport is 100, and the maximum is 500.
If the number of packages exceeds 200, a larger vehicle should be recommended, with a price of $60 USD per kilometer.
Based on the distance, the system should calculate an estimated delivery time."""
from os import system
import haversine as hs

states_coordinates = {'wisconsin': (44.5, -89.5), 'west virginia': (39, -80.5), 'vermont': (44, -72.699997), 'texas': (31, -100), 'south dakota': (44.5, -100), 'rhode island': (41.742325, -71.742332),
                      'oregon': (44, -120), 'new york': (43, -75), 'new hampshire': (44, -71.5), 'nebraska': (41.5, 100), 'kansas': (38.5, -98), 'mississippi': (33, -90), 'illinois': (40, -89),
                      'delaware': (39, -75.5), 'connecticut': (41.599998, -72.699997), 'arkansas': (34.799999, -92.199997), 'indiana': (40.273502, -86.126976), 'missouri': (38.573936, -92.603760),
                      'florida': (27.994402, -81.760254), 'nevada': (39.876019, -117.224121), 'maine': (39.876019, -117.224121), 'michigan': (44.182205, -84.506836),
                      'georgia': (33.247875, -85.441162),
                      'hawaii': (19.741755, -155.844437), 'alaska': (66.160507, -153.369141), 'tennessee': (35.860119, -86.660156), 'virginia': (37.926868, -78.024902),
                      'new jersey': (39.833851, -74.871826),
                      'kentucky': (37.839333, -74.871826), 'north dakota': (47.650589, -100.437012), 'minnesota': (46.392410, -94.636230), 'oklahoma': (36.084621, -96.921387),
                      'montana': (46.965260, -109.533691),
                      'washington': (47.751076, -120.740135), 'utah': (39.419220, -111.950684), 'colorado': (39.113014, -105.358887), 'ohio': (40.367474, -82.996216),
                      'alabama': (32.318230, -86.902298),
                      'iowa': (42.032974, -93.581543), 'new mexico': (34.307144, -106.018066), 'south carolina': (33.836082, -81.163727), 'pennsylvania': (41.203323, -77.194527),
                      'arizona': (34.048927, -111.09373),
                      'maryland': (39.045753, -76.641273), 'massachusetts': (42.407211, -71.382439), 'california': (36.778259, -119.417931), 'idaho': (44.068203, -114.742043),
                      'wyoming': (43.075970, -107.290283),
                      'north carolina': (35.782169, -80.793457), 'louisiana': (30.391830, -92.329102)}


def coordinates_to_km(state1, state2, states):
    loc1 = states[state1]
    loc2 = states[state2]
    km = hs.haversine(loc1, loc2)
    return round(km, 1)


def calculate_price(state1, state2, states, packages_amount):
    km = coordinates_to_km(state1, state2, states)
    if packages_amount > 200:
        print('For recommendation, a larger vehicle will be used, therefore you will be charged $60 USD/km instead $50/km')
        return km * 60
    else:
        return km * 50


def estimated_time(km):
    estimated_seconds = 180
    total_seconds = km * estimated_seconds
    hours = total_seconds / 3600
    return round(hours)


def choose_state(states):
    while True:
        print('-' * 50)
        print('List of all Amazon branches:')
        print('-' * 50)
        for state in states.keys():
            print(state.title())
        print('Write "back" if you want to go back to menu')
        origin_state = input('Choose the state from where you want to send the shipment: ').lower()
        destiny_state = input('Choose the state for the destination: ').lower()
        if origin_state == 'back' or destiny_state == 'back':
            return False
        elif origin_state in states_coordinates and destiny_state in states_coordinates:
            try:
                amount = int(input('¿How many packages you want to send? [Min 100/ Max 500]: '))
            except ValueError:
                system('cls')
                print('\x1B[4mEnter a valid amount of packages\x1B[0m')
            else:
                if 100 <= amount <= 500:
                    system('cls')
                    price = calculate_price(origin_state, destiny_state, states, amount)
                    time = estimated_time(coordinates_to_km(origin_state, destiny_state, states))
                    print(f"Your shipment has been ordered for a price of ${price} and will reach it's destination in aproximately {time} hours")
                    input('Press any key to go back to menu')
                    return False
        else:
            system('cls')
            print('\x1B[4mEnter a valid option\x1B[0m')


def main():
    while True:
        print('Welcome to the Amazon shipping software')
        print('1. Order a shipment')
        print('2. End program')
        action = input('Select an option: ')
        if action == '1':
            system('cls')
            choose_state(states_coordinates)
            system('cls')
        elif action == '2':
            system('cls')
            print('Thanks for using the Amazon services. See you next time')
            return False
        else:
            system('cls')
            print('\x1B[4mEnter a valid option\x1B[0m')


if __name__ == '__main__':
    main()
