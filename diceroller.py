from operator import mod
import random, sys

memory = {}

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

def save_roll(name, diceStr):
    global memory
    memory[name] = diceStr

def roll_saved(name):
    global memory
    return roll_dice(memory[name])

def remove_saved(name):
    global memory
    memory.pop(name)

def save_file(path):
    return

def load_file(path):
    return

def __main__():
    while True:
        try:
            dice_input = input('> ')  # The prompt to enter the dice string.
            if (dice_input.upper() == 'QUIT')or(dice_input.upper() == 'EXIT')or(dice_input.upper() == 'Q'):
                print('Thanks for playing!')
                sys.exit()

            if (dice_input.upper()[:4] == 'INFO'):
                continue

            if (dice_input.upper()[:8] == 'KEEP'):
                sinput = dice_input.split(' ')
                name = ' '.join(sinput[1:-1])
                save_roll(name, sinput[-1])
                print(memory)
                continue

            if (dice_input.upper()[:6] == 'FORGET'):
                sinput = dice_input.split(' ')
                name = ' '.join(sinput[1:])
                remove_saved(name)
                print(memory)
                continue

            if (dice_input.upper()[:3] == 'USE'):
                sinput = dice_input.split(' ')
                name = ' '.join(sinput[1:])
                rolls, mod = roll_saved(name)

            if (dice_input.upper()[:4] == 'ROLL'):
                sinput = dice_input.split(' ')
                dice = ' '.join(sinput[1:])
                rolls, mod = roll_dice(dice)
            
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
            print('Invalid input. Enter a valid command such as (roll), (save), (use), or (info)')
            print('Input was invalid because: ' + str(exc))
            continue  # Go back to the dice string prompt.

__main__()