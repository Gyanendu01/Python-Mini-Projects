import random
print('Welcome to a game of Rock, Paper, Scissors')

usrScore = 0
compScore = 0

numOfRounds = int(input('\nHow many rounds would you like to play: '))
for i in range(1,numOfRounds+1):
    
    # Random guess by the computer
    choices = ['rock', 'paper', 'scissors']
    compGuess=random.choice(choices)
    print(f'\nRound{i}')
    print(f'Player: {usrScore}\t\tComputer: {compScore}')
    usrGuess = input('Time to pick...rock, paper, scissors: ')
    usrGuess.lower()

    # if user guess is not valid the computer gets a point
    if usrGuess in ['rock', 'paper', 'scissors']:
        # Logic for the [rock, paper,scissors] Game
        if usrGuess == 'rock' and compGuess == 'paper':
            print('Computer: paper')
            print('Player: rock')
            compScore += 1
            print('Paper covers rock!')
        elif usrGuess == 'paper' and compGuess == 'rock':
            print('Computer: rock')
            print('Player: paper')
            usrScore += 1
            print('Paper covers rock!')
        elif usrGuess == 'paper' and compGuess == 'scissors':
            print('Computer: scissors')
            print('Player: paper')
            compScore += 1
            print('Scissors cut paper')
        elif usrGuess == 'scissors' and compGuess == 'paper':
            print('Computer: paper')
            print('Player: scissors')
            usrScore += 1
            print('Scissors cut paper')
        elif usrGuess == 'rock' and compGuess == 'scissors':
            print('Computer: scissors')
            print('Player: rock')
            usrScore += 1
            print('Rock is harder than scissors!')
        elif usrGuess == 'scissors' and compGuess == 'rock':
            print('Computer: rock')
            print('Player: scissors')
            compScore += 1
            print('Rock is harder than scissors!')
        elif usrGuess == 'paper' and compGuess == 'paper':
            print('Computer: paper')
            print('Player: paper')
            print('It is a tie, how boring!\nThis round was a tie')
        elif usrGuess == 'rock' and compGuess == 'rock':
            print('Computer: rock')
            print('Player: rock')
            print('It is a tie, how boring!\nThis round was a tie')
        elif usrGuess == 'scissors' and compGuess == 'scissors':
            print('Computer: scissors')
            print('Player: scissors')
            print('It is a tie, how boring!\nThis round was a tie')
    else:
        print('That is not a valid game option!\nComputer gets the point!')
        compScore += 1 

# Displaying the final results
print('\nFinal Game Results')
winner = 'PLAYER' if (usrScore>compScore) else 'Computer :-('
print(f'Rounds Played: {numOfRounds}\nPlayer Score: {usrScore}\nComputer Score: {compScore}\nWinner: {winner}!!!')