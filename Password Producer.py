from string import ascii_letters, digits
from random import choice
from os import path, getlogin, mkdir

# Available modes
availavle = 's', 'm', 'w'

while True:
    if not path.exists(f'C:\\Users\\{getlogin()}\\Documents\\Generation'):
        mkdir(f'C:\\Users\\{getlogin()}\\Documents\\Generation')

    # Preparing
    password = ''

    # Log
    log_type = input("Type 'Over' to overwrite your saved password in a file; Type 'Append' to append your saved passwords into the file ").lower()
    while log_type[0] != 'a' and log_type[0] != 'o' and log_type != 'w':
        log_type = input("You can only use 'Over' or 'Append' ").lower()
    if log_type[0] == 'o' or log_type == 'w':
        log_mode = 'w'
    else:
        log_mode = 'a+'


    # Inputs
    strength = input("What is your password strength? Choose 'Strong', 'Medium' or 'Weak' ").lower()
    while strength[0] not in availavle:
        strength = input("You can only use 'Strong', 'Medium' or 'Weak' ").lower()
    length_error = True
    while length_error:
        try:
            length = int(input("How many characters do you want your password to contain? "))
            length_error = False
        except:
            pass
                

    # Generating
    if strength[0] == 's':
        for _ in range(length):
            password += choice(digits + ascii_letters)
        with open(f'C:\\Users\\{getlogin()}\\Documents\\Generation\\strong.txt', log_mode) as slist_file:
            slist_file.write(f'{password}\n')
    elif strength[0] == 'm':
        for _ in range(length):
            password += choice(ascii_letters)
        with open(f'C:\\Users\\{getlogin()}\\Documents\\Generation\\medium.txt', log_mode) as mlist_file:
            mlist_file.write(f'{password}\n')
    else:
        for _ in range(length):
            password += choice(digits)
        with open(f'C:\\Users\\{getlogin()}\\Documents\\Generation\\weak.txt', log_mode) as wlist_file:
            wlist_file.write(f'{password}\n')