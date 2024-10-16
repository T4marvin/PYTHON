#number 1
price_in_ugx = 1500
days_in_week = 7
trips = 3
#
total_trips = days_in_week*trips
total_amout = total_trips*price_in_ugx
#
print(f"The Total amount For the week is:",total_amout)

#number2
print(len((input("enter a sentence:"))))
#number 3(upper case)
print((input("enter a sentence:")).upper())
#number 4(lower case)
print((input("enter a sentence:")).lower())
#number 5(finding position)
original_string = "The nile is the longest river in the world"
search_word = "nile"

position = original_string.find(search_word)
if position != -1:
    print(f"The word '{search_word}' is found at position {position}.")
#number 6(replace)
statement = "The Nile river is the longest river in the world"
replace = statement.replace("Nile","Victoria")
print(f"",replace)
#number 7
print(len(("Ugandan Matooke")))
#NUMBER 8
num_of_students=45
divide = 6
ans = num_of_students%divide
print("",ans)
#NUMBER 9
price=2500
buying=10
total = price*buying
#
if total>20000:
    print("Its High")
#NUMBER 10
#fruits
apples = 1000
bananas = 200
mangoes = 1500
#display
print("The total amout of buying 5 Apples is:",apples*5,"UGX")
print("The total amount of buying 10 bananas is:",bananas*10,"UGX")
print("The total amount of buying 3 mangoes is:",mangoes*3,"UGX")
