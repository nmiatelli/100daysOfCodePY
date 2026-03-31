print("Welcome to Treasure Island. Your mission is to find the Treasure.")
choice1 = input("You're at a cross road. Where do you want to go?\n Type 'left' or 'right'.\n").lower()

print('''
                                _.--.
                        _.-'_:-'||
                    _.-'_.-::::'||
               _.-:'_.-::::::'  ||
             .'`-.-:::::::'     ||
            /.'`;|:::::::'      ||_
           ||   ||::::::'     _.;._'-._
           ||   ||:::::'  _.-!oo @.!-._'-.
           \'.  ||:::::.-!()oo @!()@.-'_.|
            '.'-;|:.-'.&$@.& ()$%-'o.'\U||
              `>'-.!@%()@'@_%-'_.-o _.|'||
               ||-._'-.@.-'_.-' _.-o  |'||
               ||=[ '-._.-\U/.-'    o |'||
               || '-.]=|| |'|      o  |'||
               ||      || |'|        _| ';
               ||      || |'|    _.-'_.-'
               |'-._   || |'|_.-'_.-'
            jgs '-._'-.|| |' `_.-'
                    '-.||_/.-'
''')

if choice1 == "left":
    choice2 = input("You've come to a lake. There is an insland in the middle of the lake.\n Type 'wait' for a boat or 'swim' to swim across.\n").lower()

    if choice2 == "wait":
        choice3 = input("You arrive at the island unharmed. There is a house with 3 doors.\n On red, one yellow and one blue. Which color do you choose?\n").lower()
        if choice3 == "red":
            print("You've been burnt by a fire. Game over!!!! ")
        elif choice3 == "yellow":
            print("CONGRATULATIONS! YOU JUST WON THE GAME!")
        elif choice3 == "blue":
            print("You've been eaten by beasts. Game over!!!!!")
        else:
            print("You chose a door that doesn't exist. Game over!!!!!!")
    else:
        print("You've been atacked by a trout! Game over!!!")
else:
    print("You fell into a hole. Game over!")
