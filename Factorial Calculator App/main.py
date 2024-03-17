import math
print("Welcome to the Factorial Calculator App")

# Allowing the users to enter only integer values -gt 0
while True:
    usr_input = input("What number would you like to compute the factorial of? ")
    if usr_input.isdigit():
        usr_input = int(usr_input)
        if usr_input>0:
            break
        else:
            print("Enter a number greater than zero")
    else:
        print("Please enter an integer value")

# Algorithm to compute the factorial of the given number
result = 1
print(f"{usr_input}! = ",end="")
for i in range(1,usr_input):
    print(f"{i}*",end="")
    result=result*i
result = result*usr_input
print(f"{usr_input}")

# Display the factorial using math library
print("\nHere is the result from the math library:")
print(f"The factorial of {usr_input} is {math.factorial(usr_input)}!")

# Display the factorial using my algorthm
print("\nHere is the result from the my:")
print(f"The factorial of {usr_input} is {result}!")

print("It is shown twice that {}! = {} (with excitement)".format(usr_input,result))

