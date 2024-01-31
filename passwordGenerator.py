import random
import string
import os
from click import clear
from rich import print

PASSWORD_LENGTH = 5
OUTPUT_DIR = 'output'  # Output directory


ASCII_ART = '''
        .-""-.
           / .--. \\
          / /    \\ \\
          | |    | |
          | |.-""-.|
         ///`.::::.`\\
        ||| ::/  \\:: ;
        ||; ::\\__/:: ;
         \\\\\\ '::::' /
     jgs  `=':-..-'`
'''

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_menu():
    clear_console()

    print("[bold red]..................................................[/bold red]")
    print("[red]\t\t\t\t{}[/red]".format(ASCII_ART))
    print("[bold red]\t\tPassword Generator     [/bold red]")
    print("[bold red]\t\tV1.0                   [/bold red]")
    print("[bold red]\t\tAuthor: Sayed elhadad                   [/bold red]")
    print("[bold red]..................................................\n[/bold red]")
    print("1) Create a new custom password.")
    print("2) Let me suggest you a strong password.")
    print("3) Quit")

def random_string(length, charset):
    return ''.join(random.choice(charset) for _ in range(length))

def random_special_character():
    return random.choice("!@#$%^&*(){}?<>~")

def password(upper, lower, nums):
    upper_letters = random_string(upper, string.ascii_uppercase)
    lower_letters = random_string(lower, string.ascii_lowercase)
    numbers = random_string(nums, string.digits)
    special_char = random_special_character()
    
    return upper_letters + lower_letters + numbers + special_char

def ask_to_continue():
    print("Do you want to continue? [green]y) yes[/green]  [red]n) no[/red]")
    choose = input("Choose: ")
    return choose.lower() == "y"

def ask_to_save():
    print("Do you want to save the password in an external file? [green]y) yes[/green]  [red]n) no[/red]")
    choose = input("Choose: ")
    return choose.lower() == "y"

def get_user_input(prompt):
    while True:
        user_input = input(prompt)
        if user_input.isdigit() and int(user_input) >= 0:
            return int(user_input)
        else:
            print("[red]Invalid input! Please enter an integer.[/red]")

def save_to_file(password, file_name):
    output_path = os.path.join(os.getcwd(), OUTPUT_DIR, f"{file_name}.txt")
    with open(output_path, 'w', encoding='UTF-8') as file:
        file.write("............::Password Generator::............ \n\n")
        file.write(f"Password: {password}\n\n")
        file.write("............................................... \n\n")

def program():
    while True:
        print_menu()
        choose = get_user_input("Enter your choice (1, 2, or 3): ")

        if choose == 1:
            clear_console()
            upper = get_user_input("Enter the length of upper letters: ")
            lower = get_user_input("Enter the length of lower letters: ")
            nums = get_user_input("Enter the length of numbers: ")
            clear_console()
            generated_password = password(upper, lower, nums)
            print("\n\t\tPassword: [bold red]{}[/bold red]\n\n".format(generated_password))
            if ask_to_save():
                file_name = input("Enter the file name: ")
                save_to_file(generated_password, file_name)
                clear_console()
                print(f"[bold green]Password saved successfully in \n {file_name}.txt[/bold green]\n\n")

                if not ask_to_continue():
                    break
        elif choose == 2:
            clear_console()
            generated_password = password(PASSWORD_LENGTH, PASSWORD_LENGTH, PASSWORD_LENGTH)
            print("\n\t\tPassword: [bold red]{}[/bold red]\n\n".format(generated_password))

            if ask_to_save():
                file_name = input("Enter the file name: ")
                save_to_file(generated_password, file_name)
                clear_console()
                print(f"[bold green]Password saved successfully in \n {file_name}.txt[/bold green]\n\n")
                
                if not ask_to_continue():
                    break
        elif choose == 3:
            break
        else:
            print("[red]Invalid choice. Please enter 1, 2, or 3.[/red]")

if __name__ == "__main__":
    program()
