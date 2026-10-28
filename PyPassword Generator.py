import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
password = ""
# new_passwords = ''
print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Easy ways
# #first choice the random letter
# for i in range(nr_letters):
#     random_letter = random.choice(letters)
#     password += random_letter
#
# #Then random symbols
# for i in range(nr_symbols):
#     random_symbol = random.choice(symbols)
#     password += random_symbol
# #then random numbers
# for i in range(nr_numbers):
#     random_number = random.choice(numbers)
#     password += random_number
# #in last select random of the random
# # for i in range(len(password)):
# #     new_passwords += random.choice(password)
#
# print(f'Your Password : {password}')

#Hard level ---------------

password_list=[]
#first choice the random letter
for i in range(nr_letters):
   password_list.append(random.choice(letters))

#Then random symbols
for i in range(nr_symbols):
   password_list.append(random.choice(symbols))
#then random numbers
for i in range(nr_numbers):
    password_list.append(random.choice(numbers))

print(password_list)
random.shuffle(password_list)
print(password_list)
password = ""

for char in password_list:
    password += char
print(password)
