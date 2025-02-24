from operator import mod
import random, sys

def roll_dice(diceStr):
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
        mod = 0
    else:
        mod = int(diceStr[modIndex + 1 :])
        if diceStr[modIndex] == '-':
            mod = -mod

    # Roll dice
    rolls = []
    for i in range(numberOfDice):
        roll = random.randint(1, numberOfSides)
        rolls.append(roll)

    return rolls, mod

def __main__():
    while True:
        try:
            diceStr = input('> ')  # The prompt to enter the dice string.
            if (diceStr.upper() == 'QUIT')or(diceStr.upper() == 'EXIT'):
                print('Thanks for playing!')
                sys.exit()

            rolls, mod = roll_dice(diceStr)

            # Total
            print('Total:', sum(rolls) + mod, '( ', end='')

            for i, roll in enumerate(rolls):
                rolls[i] = str(roll)
            print(', '.join(rolls), end='')

            if mod != 0:
                modSign = '+' if mod > 0 else '-'
                print(' ) {} {}'.format(modSign, abs(mod)))
            else :
                print(' )')

        except Exception as exc:
            # Catch any exceptions and display the message to the user:
            print('Invalid input. Enter something like "3d6" or "1d10+2".')
            print('Input was invalid because: ' + str(exc))
            continue  # Go back to the dice string prompt.

__main__()