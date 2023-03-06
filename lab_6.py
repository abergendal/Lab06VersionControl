encoded_string = ''


# Alexander Bergendal
def encode(string):
    global encoded_string
    for i in string:
        encoded_string += str(int(i) + 3)


def decode(string):
    pass


def menu():
    print('Menu')
    print('-------------')
    print('1. Encode')
    print('2. Decode')
    print('3. Quit')


while True:
    menu()
    user_option = int(input('\nPlease enter an option: '))
    if user_option == 1:
        user_password = input('Please enter your password to encode: ')
        encode(user_password)
        print('Your password has been encoded and stored!\n')
    elif user_option == 2:
        print(f'The encoded password is {encoded_string}, and the original password is {decode(encoded_string)}\n')
    else:
        break








