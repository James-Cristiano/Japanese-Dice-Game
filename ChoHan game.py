#imports
import random
import sys

#intro to game
print(""" Cho-Han: 

This is a traditional Japanese dice game, where 2 dice are folled in a bamboo cup
by the dealer sitting on the floor. The aim of this game is for the player to then guess
if the total of the dice is even (Cho) or odd (Han).""")

#global variables
JapaneseNumbers = {1:'ICHI', 2:'NI', 3:'SAN', 4:'SHI', 5:'GO', 6:'Roku'}
Purse = 5000
dice1 = random.randint(1, 6)
dice2 = random.randint(1, 6)

#Main Game Loop
while True: 
    print('You have ', Purse, 'mon. How much do you bet? (or QUIT)')            #tells us how much money we have, and how much we wanna bet 
    while True: 
        Pot = input('> ')                                                       #allows player to add their bet value
        if Pot.upper() == 'QUIT':                                               #if user inpuits 'QUIT', will close system off
            print('Thanks for playing!')
            sys.exit()
        elif not Pot.isdecimal():                                               #checks to make sure it is a full number added
            print('Please enter a number.')
        elif int(Pot) > Purse:                                                  #makes sure user has enough money to make bet 
            print('Not enough money!')
        else:
            Pot = int(Pot)
            break

    #setup to player choice
    print('The dealer swirls the cup around and you hear the dice rattling.')
    print('The cup is slammed onto the table, the dealer still covering it, ')
    print('asks for your bet:')
    print()
    print('CHO (Even) or HAN (Odd)?')

    #letting the player make their choice
    while True: 
        Bet = input('> ').upper()                                                   #converts any response to all capitals
        if Bet != 'CHO' and Bet != 'HAN':
            print('Please enter either "CHO" or "HAN"!')                            #makes sure user only inputs correct answers
            continue
        else:
            break

    #reveal dice rolls
    print('The dealer reveals the following:')
    print(' ', JapaneseNumbers[dice1], '-', JapaneseNumbers[dice2])
    print(' ', dice1, '-', dice2)

    #math for if the player won
    RollIsEven = (dice1 + dice2) %2 == 0
    if RollIsEven:
        CorrectBet = 'CHO'
    else:
        CorrectBet = 'HAN'
    
    PlayerWon = Bet == CorrectBet                                                     #checks if user guessed correctly

    #displaying the results 
    if PlayerWon:
        print('You won! You take:', Pot, 'mon.')
        Purse = Purse + Pot
        print('The house collects a', Pot//10, 'mon fee.')                            #'//' will divide the numbers and round down to nearest whole number 
        Purse = Purse - (Pot//10)
    else: 
        Purse = Purse - Pot
        print('You loose!')

    #player has no more money
    if Purse == 0:
        print('You have run out of money!')
        print('Thanks for playing!')
        sys.exit()