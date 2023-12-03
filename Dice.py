import random

def dice_throw (dice):
    num_dice, dice_size = map(int, dice.split('d'))
    if dice_size < 4 or dice_size > 20:
        raise ValueError(f"Invalid Dice Size: {dice_size}")
        return 0
    
    print("Rolling ",num_dice,"d",dice_size," :")
    for x in range(0,num_dice):
       roll = random.randint(1, dice_size)
       print(f"Die {x}: {roll}")