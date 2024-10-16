phone_number_db = "0755032436"
email_db = "matthewmukasa0@gmail.com"
password_db = "1234"

while 'count' > 3:
    user_entry = input("email or phone number: ")
    password = input("Enter Your Password")

    if phone_number_db == user_entry or email_db == user_entry:
        print("proceed")
    else:
        print("wrong entry ,TRY AGAIN")




