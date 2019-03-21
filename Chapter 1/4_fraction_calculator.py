"""
Fraction Calculator
"""


from fractions import Fraction


def print_menu():
    print('1. Add')
    print('2. Subtract')
    print('3. Divide')
    print('4. Multiply')


def ask_questions():
    try:
        a = Fraction(input('Enter first fraction: '))
        b = Fraction(input('Enter second fraction: '))
    except ValueError:
        exit('Invalid input entered.')

    print_menu()
    map_choice_to_function(input('Operation to perform: '), a, b)


def map_choice_to_function(choice, a, b):

    mapped_functions = {
        '1': add,
        '2': subtract,
        '3': divide,
        '4': multiply
    }

    if choice in ('1', '2', '3', '4'):
        return mapped_functions.get(choice)(a, b)
    else:
        exit('Invalid selection.')


def add(a, b):
    print('Result of Addition: {0}'.format(a + b))


def subtract(a, b):
    print('Result of Addition: {0}'.format(a - b))


def divide(a, b):
    print('Result of Addition: {0}'.format(a * (b.denominator / a.numerator)))


def multiply(a, b):
    print('Result of Addition: {0}'.format(a * b))


if __name__ == '__main__':
    ask_questions()
