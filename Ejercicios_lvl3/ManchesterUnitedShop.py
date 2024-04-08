"""4. United Direct: The Manchester United's Shop
United Direct, the official store of Manchester United FC, has hired you as a developer for their online store. The manager wishes to launch a new line of products with different discounts.

Develop the shopping cart of this application considering the following features:

The jerseys are classified by: Men, Women, and Children.
Sizes range from XS to 3XL.
All men's and women's jerseys are priced at £100 if they are short-sleeved.
Long-sleeved jerseys cost £120.
Short-sleeved children's jerseys are priced at £70.
Long-sleeved children's jerseys are priced at £90.
If you are a club member, you get a 20% discount on the total purchase.
The user can buy as many jerseys as they want.
If the buyer wishes to personalize their jersey with a player's number, there is an additional charge of £25.
The stock is as follows:

FOR MEN:

First kit short-sleeved jersey: 100 units
First kit long-sleeved jersey: 90 units
Second kit short-sleeved jersey: 80 units
Second kit long-sleeved jersey: 80 units
Third kit short-sleeved jersey: 85 units
Third kit long-sleeved jersey: 50 units
FOR WOMEN:

First kit short-sleeved jersey: 105 units
First kit long-sleeved jersey: 92 units
Second kit short-sleeved jersey: 81 units
Second kit long-sleeved jersey: 81 units
Third kit short-sleeved jersey: 85 units
Third kit long-sleeved jersey: 51 units
FOR CHILDREN:

First kit short-sleeved jersey: 200 units
First kit long-sleeved jersey: 100 units
Second kit short-sleeved jersey: 85 units
Second kit long-sleeved jersey: 85 units
Third kit short-sleeved jersey: 90 units
Third kit long-sleeved jersey: 62 units

IMPORTANT: You decide how many sizes are available for each available shirt size."""
from os import system

texts = ['men', 'women', 'children']
sizes = ['XS', 'S', 'M', 'L', 'XL', 'XXL', 'XXXL']
sleeve_type = ['short sleeved', 'long sleeved']
men = {'short sleeved': ([23, 24, 24, 24, 24, 23, 23], 100), 'long sleeved': ([31, 31, 32, 32, 32, 31, 31], 120)}
women = {'short sleeved': ([38, 39, 39, 39, 39, 39, 38], 100), 'long sleeved': ([32, 32, 32, 32, 32, 32, 32], 120)}
children = {'short sleeved': ([53, 53, 54, 54, 54, 54, 53], 70), 'long sleeved': ([35, 35, 35, 36, 36, 35, 35], 90)}
jerseys = [men, women, children]
shopping_cart = []


def check_membership():
    while True:
        try:
            membership = input('Are you a Manchester United club member? [Y/N]: ').upper()
            ['Y', 'N'].index(membership)
        except ValueError:
            system('cls')
            print('\x1B[4mEnter a valid option\x1B[0m')
        else:
            system('cls')
            if membership == 'Y':
                print('You will receive a 20% final discount when purchasing')
                input('Press any key to continue ')
                return True
            else:
                input('Press any key to continue ')
                return False


def remove_stock(product):
    type_shirt = product[0]
    type_shirt_index = texts.index(type_shirt)
    type_sleeve = product[1]
    type_size = product[2]
    type_size_index = sizes.index(type_size)
    amount = product[3]
    jerseys[type_shirt_index][type_sleeve][0][type_size_index] -= amount


def custom(articles):
    amounts = [x[3] for x in articles]
    personalize = input('Do you wish to personalize your jersey with a player number? (You will be charged an additional £25 for jersey [Y/N]: ').lower()
    if personalize == 'y':
        additional_price = sum([25 * x for x in amounts])
        input('Write the number of the player you want: ')
        return True, additional_price
    elif personalize == 'n':
        additional_price = 0
        return True, additional_price
    else:
        system('cls')
        return False, None


def calculate_price(product):
    type_shirt = product[0]
    type_shirt_index = texts.index(type_shirt)
    type_sleeve = product[1]
    amount = product[3]
    found_product_price = jerseys[type_shirt_index][type_sleeve][1]
    return found_product_price * amount


def catalogue(jersey):
    while True:
        for text in texts:
            print(text.capitalize())
        print('Enter "back" if you want to go back to menu')
        action = input('Choose a type of jersey: ').lower()
        if action == 'back':
            return False
        elif action in texts:
            jersey_type = texts.index(action)
            for sleeve in sleeve_type:
                print(sleeve.capitalize())
            action2 = input('Choose a sleeve type for your jersey: ').lower()
            if action2 in sleeve_type:
                stock = [x for x in jersey[jersey_type][action2][0]]
                size_stock = list(zip(sizes, stock))
                for size, amount in size_stock:
                    print(f'{size}: Stock => {amount}')
                action3 = input('Choose a size for your jersey: ').upper()
                if action3 in sizes:
                    index_size = sizes.index(action3)
                    try:
                        jersey_amount = input('Enter the amount of jersey you want to buy within stock: ')
                        int(jersey_amount)
                    except ValueError:
                        system('cls')
                        print('\x1B[4mEnter a valid amount to buy\x1B[0m\n')
                    else:
                        if size_stock[index_size][1] >= int(jersey_amount) > 0:
                            shopping_cart.append((action, action2, action3, int(jersey_amount)))
                            system('cls')
                            print('Your purchase has been added succesfully to the shopping cart')
                            input('Press any key to go back to menu')
                            return False
                        else:
                            system('cls')
                            print('\x1B[4mEnter a valid amount to buy\x1B[0m\n')

                else:
                    system('cls')
                    print('\x1B[4mEnter a valid size for your jersey\x1B[0m\n')
            else:
                system('cls')
                print('\x1B[4mEnter a valid type of sleeve\x1B[0m\n')
        else:
            system('cls')
            print('\x1B[4mEnter a valid type of jersey\x1B[0m\n')


def buy(articles, membership_status):
    while True:
        prices = [calculate_price(x) for x in articles]
        if membership_status:
            total_price = sum(prices) * 0.8
        else:
            total_price = sum(prices)
        article_number = []
        list_number = 1
        print('List of articles: ')
        for article, price in zip(articles, prices):
            print(f'{list_number}. {article[0].capitalize()} Jersey: {article[1].capitalize()}, Size: {article[2]}, Amount: {article[3]}, Price: £{price}')
            article_number.append(str(list_number))
            list_number += 1
        print('\nIf you are a club member you will get a 20% discount')
        print(f'The total price is £{total_price}')
        print('If you wish to remove an article, write the number of the article')
        print('If you want to go back to menu write "back"')
        confirm = input('To confirm your purchase, write "buy": ').lower()
        if confirm == 'back':
            return False
        elif confirm == 'buy' and len(articles) > 0:
            validation, additional_price = custom(articles)
            if validation:
                system('cls')
                for article in articles:
                    remove_stock(article)
                shopping_cart.clear()
                print(f'Your purchase has been made succesfully for an amount of £{total_price + additional_price}')
                input('Press any key to go back to menu')
                return False
            else:
                print('\x1B[4mEnter a valid option\x1B[0m')

        elif confirm in article_number:
            removed_article_index = article_number.index(confirm)
            shopping_cart.pop(removed_article_index)
            system('cls')
        else:
            system('cls')
            print('\x1B[4mEnter a valid option\x1B[0m')


def main():
    member_club = check_membership()
    system('cls')
    while True:
        print('\x1B[4mWelcome to the official Manchester United FC official shop!!!\x1B[0m')
        print('1. Review jersey catalogue')
        print('2. Check shopping cart')
        print('3. End program')
        action = input('Select an option: ')
        if action == '1':
            system('cls')
            catalogue(jerseys)
            system('cls')
        elif action == '2':
            system('cls')
            buy(shopping_cart, member_club)
            system('cls')
        elif action == '3':
            system('cls')
            print('Thanks for buying in our shop, have a nice day')
            return False
        else:
            system('cls')
            print('\x1B[4mEnter a valid option\x1B[0m\n')


if __name__ == '__main__':
    main()
