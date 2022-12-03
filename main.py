import random

dices = {1 :(
" ___________ ",
"|           |",
"|           |",
"|     *     |",
"|           |",
"|___________|"

),

2 :(
" ___________ ",
"|           |",
"|  *        |",
"|           |",
"|        *  |",
"|___________|"

),
3 :(
" ___________ ",
"|           |",
"|  *        |",
"|     *     |",
"|        *  |",
"|___________|"

),
4 :(
" ___________ ",
"|           |",
"|  *     *  |",
"|           |",
"|  *     *  |",
"|___________|"

),

5 :(
" ___________ ",
"|           |",
"| *       * |",
"|     *     |",
"| *       * |",
"|___________|"

),

6 :(
" ___________ ",
"|           |",
"| *   *   * |",
"|           |",
"| *   *   * |",
"|___________|",
)}

def dice_roll(dices):

    random_number = random.randint(1,6)
    for art in dices.get(random_number):
        print(art)
    print("")
    
roll_again = ""
while roll_again!= "n":
    dice_roll(dices)
    roll_again = input("Roll again? Y/N: ").lower()
print("Thank you for playing\n")