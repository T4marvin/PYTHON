#FOR LOOP TO FIND THE LARGEST NUMBER IN THE LIST
NUMBERS = [15,42,73,29,91,50]
#using max function
largest = max(NUMBERS)
print(f"the largest number is{largest}")


#using for loop function
NUMBERS = [15,42,73,29,91,50]
largest = NUMBERS[0]

#displaying the largest value
for num in NUMBERS:
    if num >largest:
        largest = num
        print(largest)
print(NUMBERS[1:])