"""

Program for converting int to and from different base systems


uses int() function with base parameter
uses string.format() method and format specifications

"""

name = input('Please type your name and press enter.')
print('Hi,', name, 'This program will convert integer numbers between 3 bases')

while True:
    print('\nYour input options are Quit, Binary, Decimal, Hexadecimal.')
    command = input('Type the first letter of your choice and press enter')
    if len(command) < 1:  # Check prevents a crash when indexing to first character
        continue
    command == command[0]

    if command in ['q', 'Q']:
        break  # exit the loop, which will quit the program
    elif command in ['b', 'B']:
        mode = 'binary'
        base = 2
    elif command in ['d', 'D']:
        mode = 'decimal'
        base = 10
    elif command in ['h', 'H']:
        mode = 'hexadecimal'
        base = 16
    else:
        print("unrecognized option!")
        continue

    number_text = input('Type the ' + mode + ' integer number to convert:')
# use exception handling since the conversion would crash on many inputs

    try:
        # convert string to an integer of specified base
        n = int(number_text, base)


    except ValueError:
        print('Invalid integer input. Try again.')
        continue

    print('in binary {0:b}'.format(n))
    print('in decimal {0:d}'.format(n))
    print('in hexadecimal {0:x}'.format(n))

print('all done now, bye!')