#checking
print("Welcome To Uganda is Voting system")
print("please follow the procedure")
yes="1"
no="2"
confirm_citizen = input("Are you a citizen?\nif yes enter (1)if not enter(2):")
if confirm_citizen ==yes:
    print("Please proceed to the next step")
    age1=int(input("How Old are you?"))
    age = 18
    if age<=age1:
        print("You are eligible")
    else:
        print("You are not eligible")
elif confirm_citizen==no:
    print("Youre not ugandan")

#asking 