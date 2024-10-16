#attendance status from the user
cw_score = float(input("Enter your CW score (out of 50): "))
attendance = input("Did you attend the class? (yes/no): ")

# Check if the user passes CW and attendance
if cw_score >= 17.5 and attendance == "yes":
    # Get the exam score from the user
    exam_score = float(input("Enter your exam score (out of 50): "))

    # Check if the user passes the exam
    if exam_score >= 17.5:
        print("Congratulations! You can move to Year 1 Semester 2.")
    else:
        print("Sorry, you didn't pass the exam.")
else:
    print("Sorry, you didn't meet the criteria for the exam")