print("Welcome to the Average Calculator App")

usrName = input("\nEnter your name: ")
# Asking the user for number of records
while True:
    numOfGrade = input("How many grades would you like to enter: ")
    if numOfGrade.isdigit():
        numOfGrade = int(numOfGrade)
        if numOfGrade>0:
            break
        else:
            print("Number of grades must be greater than zero.")
    else:
        print("Grade can be a number only...")

studentGrade = []
for _ in range(numOfGrade):
    studentGrade.append(int(input("Enter Grade: ")))


# Display the grades from higest to lowest
print(f"\n{usrName}'s grades from highest to lowest are: ")
studentGrade.sort(reverse=True)
for i in studentGrade:
    print(i)

# Grade Summary
print(f"\n{usrName}'s grade summary: ")
print("\tTotal number of grades: {}".format(len(studentGrade)))
print("\tHighest grade: {}".format(studentGrade[0]))
print("\tLowest grade: {}".format(studentGrade[-1]))
orgAverage = sum(studentGrade)/len(studentGrade)
print("\tAverage grade: {}".format(orgAverage))

# marks needed to obtain the desired average grade
desiredAverage = float(input("\nWhat is your desired average: "))
print(f"\nGood luck {usrName}.")
gradeReq = desiredAverage*(len(studentGrade)+1) - sum(studentGrade)
gradeReq = round(gradeReq,2)
print(f"You will need to get a {gradeReq} on your next assignment to earn a {desiredAverage} average")

# Change an existing mark to see average grade
print("\nLets see what your average could have been if you did better/worse on an assignment.")

while True:
    gradeChng = int(input("What grade would you like to change: "))
    if gradeChng in studentGrade:
        break
    else:
        print("That grade is not present in database, please enter a valid grade.")
orgStudentGrade = studentGrade.copy()
studentGrade.remove(gradeChng)
newGrade = int(input(f"What grade would you like to change {gradeChng} to: "))
studentGrade.append(newGrade)
studentGrade.sort(reverse=True)

# Display the grades from higest to lowest
print(f"\n{usrName}'s grades from highest to lowest are: ")
studentGrade.sort(reverse=True)
for i in studentGrade:
    print(i)

# Grade Summary
print(f"\n{usrName}'s grade summary: ")
print("\tTotal number of grades: {}".format(len(studentGrade)))
print("\tHighest grade: {}".format(studentGrade[0]))
print("\tLowest grade: {}".format(studentGrade[-1]))
print("\tAverage grade: {}".format(sum(studentGrade)/len(studentGrade)))

print(f"\nYour new average grade would be {sum(studentGrade)/len(studentGrade)} compared to the original average of {orgAverage}!")
print(f"That is a change of {(sum(studentGrade)/len(studentGrade))-orgAverage} points!")

print("\nToo bad your original grades are still the same!")
print(orgStudentGrade)
print("You should go ask for extra credit!")