"""
Enhanced Unit Converter
"""


def print_menu():
    print('1. Kilograms to pounds')
    print('2. Pounds to kilograms')
    print('3. Celsius to Fahrenheit')
    print('4. Fahrenheit to Celsius')


def map_choice_to_function(choice):

    # Dictionary mapping for functions
    mapped_functions = {
        '1': kgs_lbs,
        '2': lbs_kgs,
        '3': c_f,
        '4': f_c
    }

    try:
        return mapped_functions.get(choice, lambda: 'Invalid selection.')()
    except ValueError:
        exit('Invalid input entered.')


def kgs_lbs():
    kgs = float(input('Enter weight in kilograms: '))
    lbs = kgs * 2.205
    return 'Weight in pounds: {0:.2f} lbs'.format(lbs)


def lbs_kgs():
    lbs = float(input('Enter weight in pounds: '))
    kgs = lbs / 2.205
    return 'Weight in kilograms: {0:.2f} kg'.format(kgs)


def c_f():
    celsius = float(input('Enter temperature in Celsius: '))
    fahrenheit = celsius * (9 / 5) + 32
    return 'Temperature in Fahrenheit: {0:.2f}\xb0F'.format(fahrenheit)


def f_c():
    fahrenheit = float(input('Enter temperature in Fahrenheit: '))
    celsius = (fahrenheit - 32) * (5 / 9)
    return 'Temperature in Celsius: {0:.2f}\xb0C'.format(celsius)


if __name__ == '__main__':
    print_menu()
    print(map_choice_to_function(input('Which conversion would you like to do?: ')))
