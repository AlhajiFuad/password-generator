import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ]

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '@', '#', '$', '&', '*', '_', ',', '+', '%']

print("Welcome to the PyPassword Generator!")

l = int(input("How many letters would you like in your password?\n"))
s = int(input("How many symbols would you like?\n"))
n = int(input("How many numbers would you like?\n"))

password = ""
password_list = []

for char in range(1, l + 1):
    password_list.append(random.choice(letters))

for char in range(1, s + 1):
    password_list.append(random.choice(symbols))

for char in range(1, n + 1):
    password_list.append(random.choice(numbers))

random.shuffle(password_list)

for char in password_list:
    password += char

print(password)
