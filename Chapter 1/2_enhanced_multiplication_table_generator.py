"""
Enhanced Multiplication Table Generator
"""


def multi_table(a, b):
    for i in range(1, b + 1):
        print('{0} x {1} = {2}'.format(a, i, a * i))


if __name__ == '__main__':

    # 5: Give Exit Power to the User
    while True:

        '''
        The classical Python mentality, though, is that it's easier to ask forgiveness than permission.
        In other words, don't check whether x is an integer; assume that it is and catch the exception
        results if it isn't.
        '''
        try:
            a = int(input('Please enter the number to be multiplied: '))
            b = int(input('Please enter the number of multiples of the first number: '))

            multi_table(a, b)
        except ValueError:
            exit('An invalid integer was inputted.')

        answer = input('Do you want to exit? (y) for yes ')
        if answer == 'y':
            break
