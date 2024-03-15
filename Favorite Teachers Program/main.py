print("Welcome to the Favorite Teachers Program")
list_of_teachers = []
# Adding Teachers to our list
for i in range(1,5):
    usr_data = input("Who is your favorite teacher {}: ".format(i))
    list_of_teachers.append(usr_data)
list_of_teachersCopy = list_of_teachers.copy()

# printing the list of favourite teachers in alphabetical order as well as reverse order
print("\nYour favorite teachers ranked are: {}".format(list_of_teachers))
list_of_teachers.sort()
print("Your favorite teachers alphabetically are {}".format(list_of_teachers))
list_of_teachers.reverse()
print("Your favorite teachers in reverse alphabetical order are: {}".format(list_of_teachers))

print("\nYour top two teachers are: {}".format(list_of_teachersCopy[0:2]))
print("Your next two favorite teachers are: {}".format(list_of_teachersCopy[2:4]))
print("Your last favorite teacher is: {}".format(list_of_teachersCopy[-1]))
print(f"You have a total of {len(list_of_teachersCopy)} favorite teachers")

# Adding a new Favourite teacher
new_favourite = input(f"Oops, {list_of_teachersCopy[0]} is no longer your first favorite teacher. Who is your new FAVORITE teacher ")
list_of_teachersCopy.insert(0,new_favourite)
list_of_teachers = list_of_teachersCopy.copy()

print("\nYour favorite teachers ranked are: {}".format(list_of_teachersCopy))
list_of_teachersCopy.sort()
print("Your favorite teachers alphabetically are {}".format(list_of_teachersCopy))
list_of_teachersCopy.reverse()
print("Your favorite teachers in reverse alphabetical order are: {}".format(list_of_teachersCopy))

print("\nYour top two teachers are: {}".format(list_of_teachers[0:2]))
print("Your next two favorite teachers are: {}".format(list_of_teachers[2:4]))
print("Your last favorite teacher is: {}".format(list_of_teachers[-1]))
print(f"You have a total of {len(list_of_teachers)} favorite teachers")

# Remove a teacher that you don't like
replacement_teacher = input("You've decided you no longer like a teacher. Which teacher would you like to remove from you list: ") 
list_of_teachers.remove(replacement_teacher)

list_of_teachersCopy = list_of_teachers.copy()
print("\nYour favorite teachers ranked are: {}".format(list_of_teachers))
list_of_teachers.sort()
print("Your favorite teachers alphabetically are {}".format(list_of_teachers))
list_of_teachers.reverse()
print("Your favorite teachers in reverse alphabetical order are: {}".format(list_of_teachersCopy))

print("\nYour top two teachers are: {}".format(list_of_teachersCopy[0:2]))
print("Your next two favorite teachers are: {}".format(list_of_teachersCopy[2:4]))
print("Your last favorite teacher is: {}".format(list_of_teachersCopy[-1]))
print(f"You have a total of {len(list_of_teachersCopy)} favorite teachers")