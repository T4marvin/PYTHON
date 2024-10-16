#NUMBER 1

total_votes = int(input("Fill in the total number of votes recieved:"))
no_of_votes = int(input("Fill in the number of votes each candidate recieved"))
percentage = (total_votes/no_of_votes)*100
results = print(f"The percentage of votes each candidated recieved are {percentage:.1f}%:")

#NUMBER 2
Candidate_1_votes = int(input("Enter the Number of votes Recieved:"))
Candidate_2_votes = int(input("Enter the number of votes Recieved:"))
if Candidate_1_votes > Candidate_2_votes:
    print("hurrey Canditate 1 is the Winner")
elif Candidate_2_votes > Candidate_1_votes:
    print("Amazing canditate 2 is the winner")
else:
    print("WOAH ITS A TIE")

#NUMBER 3
num_members = int(input("Enter the number of parliament members: "))
total_age = sum(int(input("Enter the age of members")))
average_age = num_members/total_age
print(f"The average of parliamentary is {average_age:.1f}")

#NUMBER 4
age = int(input("What is Your AGE my friend"))
if age >=18:
    print("You're Eligible To Vote")
else:
    print("You Are Not ELIGIBLE TO VOTE")

#NUMBER5
total_seats = int(input("Enter the total number of seats: "))
num_parties = int(input("Enter the number of political parties: "))
party_votes = []
party_name = input(f"Enter the name of party")
party_percentage = float(input(f"Enter the percentage of votes for {party_name}: "))
seats_for_party = (party_percentage / 100) * total_seats
print(f"Each Political party Shall Recieve {seats_for_party}:Accondingly")
#NUMBER6
party_seats = int(input("Enter the number of seats held by the party: "))
total_seats = int(input("Enter the total number of seats: "))
majority_threshold = total_seats // 2

if party_seats > majority_threshold:
    print("The party has a majority!")
else:
   print("The party does not have a majority.")




