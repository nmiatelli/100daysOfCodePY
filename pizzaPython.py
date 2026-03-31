print("Welcome to Pizza Python Deliveries!")
size = input("Choose the pizza size you want: S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("DO you want extra cheese? Y or N: ")

print('''
    And how about a slice?
                        ___
                        |  ~~--.
                        |%=@%%/
                        |o%%%/
                     __ |%%o/
               _,--~~ | |(_/ ._
            ,/'  m%%%%| |o/ /  `\.
           /' m%%o(_)%| |/ /o%%m `\
         /' %%@=%o%%%o|   /(_)o%%% `\
        /  %o%%%%%=@%%|  /%%o%%@=%%  \
       |  (_)%(_)%%o%%| /%%%=@(_)%%%  |
       | %%o%%%%o%%%(_|/%o%%o%%%%o%%% |
       | %%o%(_)%%%%%o%(_)%%%o%%o%o%% |
       |  (_)%%=@%(_)%o%o%%(_)%o(_)%  |
        \ ~%%o%%%%%o%o%=@%%o%%@%%o%~ /
         \. ~o%%(_)%%%o%(_)%%(_)o~ ,/
           \_ ~o%=@%(_)%o%%(_)%~ _/
             `\_~~o%%%o%%%%%~~_/'
                `--..____,,--'
''')

# to do: work out how much they need to pay based on their size choice
if size == "S":
    pizza_price = 15
elif size == "M":
    pizza_price = 20
else:
    pizza_price = 25

print("Size:",  pizza_price)
# todo: work out how much to add to their bill based on their pepperoni choice.
if pepperoni == "Y" and size == "S":
    pizza_price += 2
elif pepperoni == "N":
    pizza_price = pizza_price
else:
    pizza_price += 3
print("Adding pepperoni: $",  pizza_price)
#todo : work out their  final amount based whether if they want extra cheese.
if extra_cheese == "Y":
    pizza_price += 1
print("Adding cheees: $",  pizza_price)
print(f"Final bill is: ${pizza_price}" )
