number = float(input("Input a number: "))

if number > 0:
    print(f"{number} is a positive number.")
elif number < 0:
    print(f"{number} is a negative number.")
else:
    print(f"{number} is zero.")





for i in range(10):
    # Print the string representation of 'i' multiplied by 'i'
    print(str(i) * i)






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
    if not any(char in "._" for char in password):
        return "Invalid Password: Must contain at least one of the characters $, %, or &."
    return "Valid Password!"

user_password = input("Enter a password: ")
print(validate_password(user_password))
