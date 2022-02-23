"""Password generator with database"""
import random
from utils import database

database.create_db()

UPPERCASE = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
LOWERCASE = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',  'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SPECIAL = ['@', '#', '$', '.', '*', ',', '!']

def easy_pass(password_len):
    """Function which generate password with low strenght"""
    characters =random.sample(UPPERCASE, 1) + random.sample(UPPERCASE + LOWERCASE, password_len - 1)
    random.shuffle(characters)
    password = "".join(characters)
    database.add_password(password)
    return password


def medium_pass(password_len):
    """Function which generate password with medium strenght"""
    characters = random.sample(DIGITS, 1)+ random.sample(UPPERCASE, 1) + random.sample(DIGITS + UPPERCASE + LOWERCASE, password_len - 2)
    random.shuffle(characters)
    password = "".join(characters)
    database.add_password(password)
    return password


def strong_pass(password_len):
    """Function which generate password with strong strenght"""
    characters = random.sample(SPECIAL, 1) + random.sample(DIGITS, 1) + random.sample(UPPERCASE, 1) + random.sample(SPECIAL + DIGITS + UPPERCASE + LOWERCASE, password_len - 3)
    random.shuffle(characters)
    password = "".join(characters)
    database.add_password(password)
    return password



def generate_password_menu():
    """User password generetor menu"""
    user_selection = 0
    while user_selection != '4':
        condition = False
        user_selection = input("""
1.Generate easy password (Only upper and lower cases )                                   
2.Generate medium password (Contains numerical digits, upper and lower cases)                    
3.Generate strong password (Contains pecial signs, numerical digits, upper and lower cases)
4.Back to main menu
What you wanna do: """)
        if user_selection == '1' or user_selection == 'g':
            while condition != True:
                password_lenght = int(input("Enter the length of the password (min - 5, max - 20): "))
                if password_lenght >= 5 and password_lenght <= 20:
                    print(f'Password - {easy_pass(password_lenght)}')
                    condition = True
        elif user_selection == '2' or user_selection == 'search':
            while condition != True:
                password_lenght = int(input("Enter the length of the password (min - 8, max - 20): "))
                if password_lenght >= 8 and password_lenght <= 20:
                    print(f'Password - {medium_pass(password_lenght)}')
                    condition = True
        elif user_selection == '3' or user_selection == 'add':
            while condition != True:
                password_lenght = int(input("Enter the length of the password (min - 8, max - 20): "))
                if password_lenght >= 8 and password_lenght <= 20:
                    print(f'Password - {strong_pass(password_lenght)}')
                    condition = True
        elif user_selection == '4' or user_selection == 'quit':
            continue
        else:
            print("Unknow comand")
            continue


def database_options_menu():
    """Database option menu"""
    user_selection = 0
    while user_selection != '2':
        user_selection = input("""
1.Delete password                                 
2.Back to main menu
What you wanna do: """)
        if user_selection == '1':
             database.delete_password()
        elif user_selection == '2':
            continue
        else:
            print("Unknow comand")
            continue

def main_menu():
    """Function with main menu"""
    user_selection = 0
    while user_selection != '5':
        user_selection = input("""
Choose one of the options below:
1.Generate password               : Enter '1' or 'g'
2.Show last generated password    : Enter '2' or 'last'
3.Show all generated password     : Enter '3' or 'all'
4.Database options                : Enter '4' or 'opt
5.Quit the program                : Enter '5' or 'quit'
What you wanna do: """)
        if user_selection == '1' or user_selection == 'g':
            generate_password_menu()
        elif user_selection == '2' or user_selection == 'last':
            database.show_last()
            continue
        elif user_selection == '3' or user_selection == 'all':
            database.show_all()
            continue
        elif user_selection == '4' or user_selection == 'opt':
            database_options_menu()
        elif user_selection == '5' or user_selection == 'quit':
            print('Goodbye :)')
            break
        else:
            print("Unknow comand")
            continue


if __name__ == "__main__":
    main_menu()




