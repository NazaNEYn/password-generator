import random
from list import alphabets, numbers, symbols

password = []

user_number = int(input("How many numbers?\n"))

for _ in range(user_number):
    password.append(random.choice(numbers))


user_symbol = int(input("How many symbols?\n"))

for _ in range(user_symbol):
    password.append(random.choice(symbols))


user_alphabets = int(input("How many alphabets?\n"))

for _ in range(user_alphabets):
    password.append(random.choice(alphabets))


random.shuffle(password)
password = "".join(password)

print(f"Your generated password is: {password}")
