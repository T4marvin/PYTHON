#NUMBER 1
def find_numbers():
    result = []
    for num in range(2000, 3201):
        if num % 8 == 0 and num % 6 == 0:
            result.append(num)
    return result

divisible_numbers = find_numbers()
print(divisible_numbers)

#NUMBER 2
def guess_number():
    target_number = 11
    while True:
        user_guess = int(input("Guess a number between 1 and 20: "))
        if user_guess == target_number:
            print("Well guessed!")
            break
        else:
            print("Try again!")

guess_number()

#NUMBER 3
n = 5 
# Maximum number of asterisks in the middle row
# Upper part of the pattern
for i in range(n):
    for j in range(i + 1):
        print("* ", end="")
    print()

# Lower part of the pattern
for i in range(n - 1, 0, -1):
    for j in range(i):
        print("* ", end="")
    print()

#NUMBER 4
user_input = input("Enter a word: ")
reversed_word = user_input[::-1]
print("Reversed word:", reversed_word)

#NUMBER 5
numbers = (13, 26, 39, 52, 65, 78, 91)
count = 0

for num in numbers:
    if num % 13 == 0:
        count += 1

print(f"Number of numbers divisible by 13: {count}")

#NUMBER 6
for i in range(11):
    if i in (4, 8):
        continue
    print(i, end=" ")

#NUMBER 7
num = int(input("Input a number: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

#NUMBER 8
for i in range(1, 81):
    if i % 3 == 0 and i % 7 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 7 == 0:
        print("Buzz")
    else:
        print(i)

#NUMBER 9
rows = 4
columns = 5
array = [[i * j for j in range(columns)] for i in range(rows)]

for row in array:
    print(row)

#NUMBER 12
def count_upper_lower_ascii(s):
    upper = 0
    lower = 0
    for char in s:
        if 'a' <= char <= 'z':
            lower += 1
        elif 'A' <= char <= 'Z':
            upper += 1
    return upper, lower

input_string = "PyThOn"
upper, lower = count_upper_lower_ascii(input_string)
print(f"Uppercase letters: {upper}")
print(f"Lowercase letters: {lower}")

#NUMBER 13
def validate_password(password):
    if len(password) < 8:
        return "Invalid Password: Too short (minimum length is 8 characters)."
    if len(password) > 16:
        return "Invalid Password: Too long (maximum length is 16 characters)."
    if not any(char.islower() for char in password):
        return "Invalid Password: Must contain at least one lowercase letter."
    if not any(char.isupper() for char in password):
        return "Invalid Password: Must contain at least one uppercase letter."
    if not any(char.isdigit() for char in password):
        return "Invalid Password: Must contain at least one digit (0-9)."
    if not any(char in "$%&" for char in password):
        return "Invalid Password: Must contain at least one of the characters $, %, or &."
    return "Valid Password!"

user_password = input("Enter a password: ")
print(validate_password(user_password))

#number 39
number = float(input("Input a number: "))

if number > 0:
    print(f"{number} is a positive number.")
elif number < 0:
    print(f"{number} is a negative number.")
else:
    print(f"{number} is zero.")

#number 50
for i in range(10):
    # Print the string representation of 'i' multiplied by 'i'
    print(str(i) * i)





