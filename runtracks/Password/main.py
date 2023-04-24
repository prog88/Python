# PASSWORD
import string
import hashlib
import json

## CONSTANTS
ALPHABET_UPPER = string.ascii_uppercase
ALPHABET_LOWER = string.ascii_lowercase
NUMBER = "0123456789"
SYMBOL = "(!@#$%^&*)."
FILENAME = "secured_data.json"

## DEFINITION
def get_user_password_input():
    print("Please enter your password:")
    return input()

def get_menu_input():
    print("Please choose between [O, 1, 2] to:\n0: exit\n1: add password\n2: display passwords")
    return input()

def is_valid_length(inputString):
    return len(inputString) >= 8

def contains_at_least_an_uppercase(character):
    return character in ALPHABET_UPPER

def contains_at_least_a_lowercase(character):
    return character in ALPHABET_LOWER

def contains_at_least_a_number(character):
    return character in NUMBER

def contain_at_least_a_symbol(character):
    return character in SYMBOL

def check_if_password_is_valid(userInput):
    has_valid_length = False
    hasUpper, hasLower, hasDigit, hasSymbol = False, False, False, False
    for char in userInput:
        if contains_at_least_an_uppercase(char):
            hasUpper = True
        elif contains_at_least_a_lowercase(char):
            hasLower = True
        elif contains_at_least_a_number(char):
            hasDigit = True
        elif contain_at_least_a_symbol(char):
            hasSymbol = True
        else:
            return False
    return is_valid_length(userInput) and hasUpper and hasLower and hasDigit and hasSymbol

## PROCESS HASH256
def get_hashed(userInput):
    hashed = hashlib.sha256(userInput.encode('utf-8'))
    return hashed.hexdigest()

## PROCESS ADD PASSWORD 
def add_password_to_file(newPassword):
    hashedPassword = get_hashed(newPassword)
    datas = load_data_from(FILENAME)
    if hashedPassword not in datas:
        datas.append(hashedPassword)
        save_data_into(datas, FILENAME)

### FILE WRITE
def save_data_into(datas, filename):
    with open(filename, "w") as file_write:
        json.dump(datas, file_write)

### FILE READ
def load_data_from(filename):
    try:
        with open(filename) as file_object:
            datas = json.load(file_object)
        return datas
    except FileNotFoundError:
        return []

## PROCESS PASSWORD CONTROL
def password_control():
    userInput = get_user_password_input()
    isValid = check_if_password_is_valid(userInput)
    if isValid == True:
        add_password_to_file(userInput)
    return isValid

## PROCESS LOGIN
def login():
    attempt = 2
    while password_control() is False and attempt > 0:
        attempt -= 1

## POMPT MENU
def menu():
    running = True
    while running:
        menuItem = get_menu_input()
        match menuItem:
            case "0":
                running = False
            case "1":
                print("Create new password")
                login()
            case "2":
                print("Password list are:")
                print(load_data_from(FILENAME))       

## MAIN FUNCTION
def main():
    menu()

## EXECUTE
main()