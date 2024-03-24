print('Welcome to the Voter Registration App')

usrName = input('\nEnter your name: ')
usrAge = int(input('Enter your age: '))

if usrAge>=18:
    print('\nCongratulations {}! You are old enough to register to vote.'.format(usrName))
    print('\nHere is a list of political parties to join.')
    print('\t-Republican\n\t-Democratic\n\t-Independent\n\t-Libertarian\n\t-Green')
    while True:
        usrParty = input('\nWhich party would you like to join: ')
        if usrParty.lower() in ['independent', 'green','democratic','republican','Libertarian']:
            break
        else:
            print('Choose a valid party to join')
        
    if usrParty.lower() == 'republican':
        print('Congratulations {}! You have joined the Republican party!\nThat is a major party'.format(usrName))
    elif usrParty.lower() == 'independent':
        print('Congratulations {}! You have joined the Independent party!\nYou are an independent person!'.format(usrName))
    elif usrParty.lower() == 'democratic':
        print('Congratulations {}! You have joined the Democratic party!\nYou vouch for democratic values!'.format(usrName))
    elif usrParty == 'libertarian':
        print('Congratulations {}! You have joined the Green party!\nYou vouch for Individual liberty!'.format(usrName))
    elif usrParty == 'green':
        print('Congratulations {}! You have joined the Green party!\nYou vouch for environmentalism!'.format(usrName))
else:
    print('\nYou are not old enough to register to vote')