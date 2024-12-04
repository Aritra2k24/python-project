import string
import random
upper_case = string.ascii_uppercase
lower_case = string.ascii_lowercase
my_letters = list(upper_case+lower_case)
my_digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
my_symbol = ["#", "$", "^", "&", "*", "!", "?", "@"]
number_of_letters = int(input("enter the number of letters"))
number_of_digits =  int(input("enter the number of digits"))
number_of_symbols = int(input("enter the number of symbols"))
password_list = []
for char in range(0, number_of_letters):
    password_list += random.choice(my_letters)
for digit in range(0, number_of_digits):
    password_list += random.choice(my_digits)
for symbol in range(0, number_of_symbols):
    password_list += random.choice(my_symbol)
random.shuffle(password_list)
password = ""
for char in password_list:
    password += char
print(f"your password :{password}")