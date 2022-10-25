from operator import mod
import random, sys

def __main__():
    while True:
        try:
            diceStr = input('> ')  # The prompt to enter the dice string.
            if diceStr.upper() == 'QUIT':
                print('Thanks for playing!')
                sys.exit()

            diceStr = diceStr.lower().replace(' ', '')
            # Find the "d" in the dice string input:
            dIndex = diceStr.find('d')
            if dIndex == -1:
                raise Exception('Missing the "d" character.')

            # Find number of dice
            numberOfDice = diceStr[:dIndex]
            if not numberOfDice.isdecimal():
                raise Exception('Missing the number of dice.')
            numberOfDice = int(numberOfDice)

            # Find Modifier
            modIndex = diceStr.find('+')
            if modIndex == -1:
                modIndex = diceStr.find('-')
            
            # Find number of sides
            if modIndex == -1:
                numberOfSides = diceStr[dIndex + 1 :]
            else:
                numberOfSides = diceStr[dIndex + 1 : modIndex]
            if not numberOfSides.isdecimal():
                raise Exception('Missing number of sides.')
            numberOfSides = int(numberOfSides)

            # Modifier
            if modIndex == -1:
                modAmount = 0
            else:
                modAmount = int(diceStr[modIndex + 1 :])
                if diceStr[modIndex] == '-':
                    modAmount = -modAmount

            # Roll dice
            rolls = []
            for i in range(numberOfDice):
                roll = random.randint(1, numberOfSides)
                rolls.append(roll)

            # Total
            print('Total:', sum(rolls) + modAmount, '( ', end='')

            for i, roll in enumerate(rolls):
                rolls[i] = str(roll)
            print(', '.join(rolls), end='')

            if modAmount != 0:
                modSign = diceStr[modIndex]
                print(' ) {} {}'.format(modSign, abs(modAmount)))
            else :
                print(' )')

        except Exception as exc:
            # Catch any exceptions and display the message to the user:
            print('Invalid input. Enter something like "3d6" or "1d10+2".')
            print('Input was invalid because: ' + str(exc))
            continue  # Go back to the dice string prompt.

__main__()