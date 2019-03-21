"""
Even Odd Vending Machine
"""


def is_even(num):
    return True if num % 2 == 0 else False


def repeat_number(num):
    num = int(num)
    even_text = (' is odd: ', ' is even: ')[is_even(num)]

    nums = str(num) + even_text
    nums += str(num) + " "

    for i in range(1, 10):
        nums += str(num + (i * 2)) + " "

    return nums.rstrip()


if __name__ == '__main__':
    try:
        user_input = float(input('Please enter an integer: '))

        if user_input.is_integer():
            t1 = repeat_number(user_input)
            print(t1)
        else:
            print('Invalid integer.')

    except ValueError:
        exit('Invalid integer.')
