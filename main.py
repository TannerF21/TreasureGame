print(r'''
                    ____...------------...____
               _.-"` /o/__ ____ __ __  __ \o\_`"-._
             .'     / /                    \ \     '.
             |=====/o/======================\o\=====|
             |____/_/________..____..________\_\____|
             /   _/ \_     <_o#\__/#o_>     _/ \_   \
             \_________\####/_________/
              |===\!/========================\!/===|
              |   |=|          .---.         |=|   |
              |===|o|=========/     \========|o|===|
              |   | |         \() ()/        | |   |
              |===|o|======{'-.) A (.-'}=====|o|===|
              | __/ \__     '-.\uuu/.-'    __/ \__ |
              |==== .'.'^'.'.====|
              |  _\o/   __  {.' __  '.} _   _\o/  _|
              `""""-""""""""""""""""""""""""""-""""`
''')

print("Welcome to Laugh Tale island. Your mission is to find the One Piece!")

choice1 = input("You're at a crossroads, which direction will you go? 'Left' or 'Right': ").lower()

if choice1 == "left":
    choice2 = input("You've come to a lake, will you 'swim' or 'wait'?: ").lower()

    if choice2 == "wait":
        choice3 = input("You've come to 3 doors. Which will you go in? 'Red', 'Yellow', or 'Blue'?: ").lower()

        if choice3 == "red":
            print("Your Haki burned up. GAME OVER!!!!")
        elif choice3 == "blue":
            print("You were slashed by Zoro. GAME OVER!!!!")
        elif choice3 == "yellow":
            print("You found the One Piece and win the game! You're the King of the Pirates!")
        else:
            print("You picked a non-existent door. GAME OVER!!!!")
    else:
        print("You were eaten by a sea beast. GAME OVER!!!!")
else:
    print("You were attacked by Jack the Drought. GAME OVER!!!!")