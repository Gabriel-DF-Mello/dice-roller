import random, sys

memory = {}
dicebag = 'dicebag.txt'

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
        modifier = 0
    else:
        modifier = int(diceStr[modIndex + 1 :])
        if diceStr[modIndex] == '-':
            modifier = -modifier

    # Roll dice
    rolls = []
    for i in range(numberOfDice):
        roll = random.randint(1, numberOfSides)
        rolls.append(roll)

    return rolls, modifier

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
    global memory
    with open(path, "w") as f:
        for key, val in memory.items():
            f.write(f"{key}:{val}\n")
    return

def load_file(path):
    global memory
    with open(path, 'r') as file:
        for line in file:
            s = line.strip().split(':')
            memory[s[0]] = s[1]
    return

def __main__():
    global memory
    global dicebag
    
    load_file(dicebag)
    print('Type the commands (info) or (help) for instructions')
    while True:
        try:
            dice_input = input('> ')  # The prompt to enter the dice string.
            if (dice_input.upper() == 'QUIT')or(dice_input.upper() == 'EXIT')or(dice_input.upper() == 'Q'):
                print('Thanks for playing!')
                save_file(dicebag)
                sys.exit()

            if (dice_input.strip() == ''):
                continue

            if (dice_input.upper()[:4] == 'READ') or (dice_input.upper()[:8] == 'REMEMBER'):
                print(memory)
                continue

            if (dice_input.upper()[:4] == 'INFO') or (dice_input.upper()[:4] == 'HELP'):
                print('Here is a list of commands:')
                print('\troll (xdy): rolls x many dice, each with y sides, for example: roll 4d6+3')
                print('\twrite (name of formula) (xdy): saves a certain formula under the given name, to be easily rolled later, for example: write fireball 8d6')
                print('\tuse (name of formula): rolls a previously saved formula, for example: use fireball')
                print('\tforget (name of formula): deletes a formula from memory, for example: forget fireball')
                print('\tread: view your formulas currently in memory')
                print('\tsave: saves your current memory to a file for later use')
                print('\tquit: exits the game and saves your memory')
                continue

            if (dice_input.upper()[:4] == 'SAVE'):
                save_file(dicebag)
                print('Memory saved!')
                continue

            if (dice_input.upper()[:5] == 'WRITE'):
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
                rolls, modifier = roll_saved(name)

            if (dice_input.upper()[:4] == 'ROLL'):
                sinput = dice_input.split(' ')
                dice = ' '.join(sinput[1:])
                rolls, modifier = roll_dice(dice)
            
            # Total
            print('Total:', sum(rolls) + modifier, '( ', end='')

            for i, roll in enumerate(rolls):
                rolls[i] = str(roll)
            print(', '.join(rolls), end='')

            if modifier != 0:
                modSign = '+' if modifier > 0 else '-'
                print(' ) {} {}'.format(modSign, abs(modifier)))
            else :
                print(' )')

        except Exception as exc:
            # Catch any exceptions and display the message to the user:
            print('Invalid input. Enter a valid command such as (roll), (save), (use), or (info)')
            print('Input was invalid because: ' + str(exc))
            continue  # Go back to the dice string prompt.

__main__()