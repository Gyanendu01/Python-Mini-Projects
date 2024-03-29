import random
print('Welcome to the Guess My Number App')

usrName = input('\nEnter your name: ')
print(f'Well {usrName}, I am thinking of a number between 1 and 20.')

# Store a random number guessed by machine
randomNum = random.randint(1,20)

# To display after how many guesses user was able to guess the number
count = 1

# Allow the user to guess the number in 5 trys
for _ in range(4):
    usrGuess = int(input('\nTake a guess: '))
    if usrGuess == randomNum:
        print(f'Good job, {usrName}! You guessed my number in {count} guesses!')
        break
    elif usrGuess < randomNum:
        print('Your guess is too low.')
        count += 1
    elif usrGuess > randomNum:
        print('Your guess is too high.')
        count += 1

