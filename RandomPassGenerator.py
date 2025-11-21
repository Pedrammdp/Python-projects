import random
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!', '#', '$', '%', '@', '&', '(', ')', '*','#']

print("Welcome to the password Generator!")
nr_letters = int(input("How many letters would you like\n"))
nr_symbols = int(input("How many symbols?\n"))
nr_numbers = int(input("How many numbers?\n"))


password_list = []
for letter in range(1, nr_letters+1):
    password_list += random.choice(letters)

for num in range(1, nr_numbers+1):
    password_list += random.choice(numbers)

for symb in range(1, nr_symbols+1):
    password_list += random.choice(symbols)

random.shuffle(password_list)
password = ""
for char in password_list:
    password += char

print(password)