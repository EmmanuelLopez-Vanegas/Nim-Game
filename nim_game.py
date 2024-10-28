# Here we are importing the Timem, OS, and Random Libraries
import random
import time
import os

# The winning and losing is dedicated to giving it output that says who wins and who loses
def winningANDlosing(loser, winner, names, piles):
    # The os.system('cls') is meant to clear all lines that were present previously
    os.system('cls')
    # Here we will be printing the amount of counters left in the specified values
    print('Pile 1 has',piles[0],'Counters: ','* '*piles[0])
    print('Pile 2 has',piles[1],'Counters: ','* '*piles[1])
    print('Pile 3 has',piles[2],'Counters: ','* '*piles[2])
    # loser == to one value within the names list it will print the correct value
    if loser == names[0]:
        print(f'{loser} has taken the last counter')
        print(f'{names[1]} wins')
    elif loser == names[1]:
        print(f'{loser} has taken the last counter')
        print(f'{names[0]} wins')
    # winner == to one value within the names list it will print the correct value
    if winner == names[0]:
        print(f'{names[1]} has been forced to take the last counter')
        print(f'{winner} wins')
    elif winner == names[1]:
        print(f'{names[0]} has been forced to take the last counter')
        print(f'{winner} wins')

# The fucntion game_rendering is mostly for a bit of visual aesthetic as it shows a countdown until the game starts
def game_rendering(names):
    print('LOCAL GAME BEING RENDERED')
    time.sleep(0.5)
    # This for loop allows for there to be a countdown starting at 5 going down all the way until 0
    for i in range(5, 0, -1):
        os.system('cls')
        print(f'Game Loading... for {names[0]} and {names[1]}  ', i)
        print(f'Piles are being calculated...')
        time.sleep(0.5)
    time.sleep(0.5)

# The nameFOR2 function is meant to update the list - names in order for it to be easily accesible throughout the file
def nameFOR2():
    # Here we are creating a list with empty strings
    names =['', '']
    # while names[0] is blank this code will not execute
    while names[0] == '':
        # This will ask the player to update said value
        names[0] = (input('What is the name of player 1? '))
        time.sleep(0.5)
        # if the player leaves the value blank it will ask for another input
        if names[0] == '':
            print('You must enter a name')
    # while names[0] is blank this code will not execute
    while names[1] == '':
        # This will ask the player to update said value
        names[1] = (input('What is the name of player 2? '))
        time.sleep(0.5)
        # if the player leaves the value blank it will ask for another input
        if names[1] == '':
            print('You must enter a name')
    # return names will enable for the new update list to be used in other functions throughout the file
    return names

# The prunt_piles fucntion is meant to show how many counters are in each pile
def print_piles(piles, name, round):
    os.system('cls')
    # This enables for us to have a visual of what round it is
    print(f"Round {round}")
    # print('\n') is meant to create a break/blank line
    print('\n')
    # Here we are printing each pile with a visual aid of how many counters there are
    print('Pile 1 has',piles[0],'Counters: ','* '*piles[0])
    print('Pile 2 has',piles[1],'Counters: ','* '*piles[1])
    print('Pile 3 has',piles[2],'Counters: ','* '*piles[2])
    print('\n')
    # This line will indicate whos turn it is
    print('It is',name,"'s Turn")

# The function pile_random_gen will calculate the values of the totalCounters and counters in each pike
def pile_random_gen():
    os.system('cls')
    print("Let's Begin")
    # firstly we are creating a list from 0-2 with each value being = to 1 singular pile
    piles = [0,0,0]
    # counters is meant to run a randint that fetches a number from 3-100 
    counters = random.randint(3,100)
    # the next 3 lines calculate how much counters go into each pile, by using the math below we are able to make sure that it all adds up to counters
    piles[0] = random.randint(1,counters - 2)
    piles[1] = random.randint(1,counters - piles[0] - 1)
    piles[2] = counters - piles[0] - piles[1]
    # here we are returning the updated value of piles which contains piles[0], piles[1], and piles[2]
    return piles

# The selectpileandcounters function is meant to ask the player what pile they want to reomve counters from and how much counters from that pile
def selectpileandcounters(piles):
    # this control value will manage all the while loops in this function
    control = False
    # once the player has answered something that is valid to the input below control will be toggled to True
    while control == False:
        # askPiles is meant to ask the player from what pile they would like to remove counters from
        askPiles = input('What pile would you like to remove counters from (1/2/3)? ')
        # if the players answer 1, 2, or 3 it will proceed
        if askPiles == '1' or askPiles == '2' or askPiles == '3':
            # if the amount of counters in the pile chosen is = 0 then it will tell the player to try another pile
            if piles[int(askPiles)-1] == 0:
                print('This Pile is empty, please select another Pile')
            # if the pile has counters than control will be toggled to True leading for it exit the while loop
            else:
                control = True
        # if the player inputs a value other than 1,2, or 3 it will ask the player to retry
        else:
            print('Please enter a valid Input from 1-3')
    # for the next while loop we must again toggle control to false
    control = False
    # this while loop asks the player how many counters they would like to reomve from the pile chosen above
    while control == False:
        # askCounter is an input that will ask the player how many counters to remove from askPiles
        askCounter = input(f'How many counters would you like to remove from Pile {askPiles}? ')
        # if the players answer is a number it will proceed
        if askCounter.isdigit():
            askCounters = int(askCounter)
            # if the value of askCounters > the amount of counters left in askPiles it will say to input another value
            if int(askCounters) > piles[int(askPiles)-1]:
                print(f'Number exceeds amount of counters in Pile {askPiles}, current amount of counters is {piles[int(askPiles)-1]}')
            #  if the value of askCounters = 0 the code will ask the player to choose at least one counter from the chosen pile
            elif askCounters <= 0:
                print(f'Must Select at least one counter from Pile {askPiles}')
            # if the value had passed all the evaluations it will toggle control as true enabling for the player to exit the while loop
            else:
                piles[int(askPiles)-1] = piles[int(askPiles)-1] - askCounters
                control = True
        # if player did not give an integer as the value then it will ask the player to give an existing value
        else:
            print(f'Please enter a valid number beetween 1 and {piles[int(askPiles)-1]}')
    return piles

# The function xor is what takes care of all the logistics regarding the bot
def xor(piles):
    # here we are updating a few variables and transferring the values from piles to the new variables
    temp0 = piles[0]
    temp1 = piles[1]
    temp2 = piles[2]
    # we are setting xor to 0 so that we can allow for the while loop below to run properly
    xor = 0
    # this line will allow for temp to become a list update with the new variables temp0, temp1, and temp2
    temp = [temp0, temp1, temp2]
    # pos will be equal to the hightest index value inside the temp list
    pos = temp.index(max(temp))
    #Avoid condition where there is no counters in the unselected piles
    condition = sum(temp)
    # if the xor isnt 1 the while loop will keep running
    while xor != 1:
        # condition > 1 we will keep decreasing pos by 1 until the xor = 1
        if condition > 1:
            temp[pos] = temp[pos] -1
            condition = condition -1
            xor = temp[0] ^ temp[1] ^ temp[2]
        # if condition is not satisfied step will be skipped
        else:
            xor = 1
            temp[pos] = 1
    return temp

# The playing function is what manages all the turns within the game
def playing(piles, names):
    # here we are setting keepPlaying as True which manages the for loop
    keepPlaying = True
    # before we start actually running the game we need to set a few variables, round = 0 and then winner and loser should be set as empty strings
    round = 0
    winner = ''
    loser = ''
    # while keepPlaying = True the while loop will keep running
    while keepPlaying == True:
        # everytime one round passes it will update the new round value which is round = round + 1
        round = round + 1
        # because our names value is a list we can run this for loop for each value there is, in this case there will always be 2
        for name in names: 
            # this will call the print_piles function enabling for us to extract the amount of piles ther are
            print_piles(piles, name, round)
            time.sleep(1)
            # if the name value within the names list is != to CPU it will cause for the player to have their turn
            if name != 'CPU':
                # this is calling the selectpileandcounters which allows the PLAYERS to complete their action
                piles = selectpileandcounters(piles)
            # if the value of name was = to CPU then it will cause for us to call the function managing the bot
            else:
                # this calls the xor function which manages the bot
                piles = xor(piles)
            # now we are updating our totalCounters bt adding all our values of piles
            totalCounters = piles[0] + piles[1] + piles[2]
            # if totaCounters = 1 then winner will automatically be updated
            if totalCounters == 1:
                winner = name
                keepPlaying = False
                break
            # if totaCounters = 1 then loser will automatically be updated
            elif totalCounters == 0:
                loser = name
                keepPlaying = False
                break             
    return loser, winner, piles

# the function select_game_type will be the main point of the whole game as everything is being called back to this point
def select_game_type():
    # here we are making correct_selection = to false
    correct_selection = False
    while not correct_selection:
        # The how_many input line is meant to ask the users how many players there will be
        how_many = input('Will there be "1" or "2" Players? ')
        # if the how_many input is = to 1 then single player mode will be enabled meaning you will be playing against a bot
        if how_many == '1':
            print('** You are playing Single Player against computer')
            names = ['','']
            names[0] = input('What is your name? ')
            names[1] = 'CPU'
            game_rendering (names)
            piles = pile_random_gen()
            loser, winner, piles = playing(piles, names)
            winningANDlosing(loser, winner, names, piles)

            correct_selection = True
        # if the how_many input is = to 1 then two player mode will be enabled meaning you will be playing against another player LOCALLY
        elif how_many == '2':
            print('** You are playing the 2-player game')
            names = nameFOR2()
            game_rendering(names)            
            piles = pile_random_gen()            
            loser, winner = playing(piles, names)
            winningANDlosing(loser, winner, names, piles)

            correct_selection = True
        elif how_many == 'E':
            print('Exiting Game')            
            SystemExit
        else:
            print("Invalid Input, make a new selection. 'E' to exit")

print('Welcome to the NIM game')
# Let user select game type
select_game_type()
