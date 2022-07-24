#this is monopoly game
import json ,sys # json file

# creating variables for logic implementation
owned_property = {}
total_properties = {}
properties_for_rent = []
properties_for_sell = []
coloured_property = {}
board=[]
players = {"Peter":{"balance":16,"color_owned":[],"moves":[],"last_step":0},"Billy":{"balance":16,"color_owned":[],"moves":[],"last_step":0},"Charlotte":{"balance":16,"color_owned":[],"moves":[],"last_step":0},"Sweedal":{"balance":16,"color_owned":[],"moves":[],"last_step":0}}

def board():
    board_rules = open('board.json')  # Opening JSON file
    board = json.load(board_rules)  # returns JSON object as a dictionary
    for properties in board:  # Iterate through the json list
        total_properties[properties['name']]=properties # creating a dictionary and importing board.json

board()

for property in total_properties:
    if property == "GO": # first condition every players starts at GO
        continue
    if total_properties[property]['colour'] in coloured_property: # creating a dictionary of all the possible coloured properties
        coloured_property[total_properties[property]['colour']] += 1
    else:
        coloured_property[total_properties[property]['colour']] = 1

    properties_for_sell.append(property) # creating a property for sell list to check if the property is available for sell purposes

def rolls_1():
    rolls_1 = open('rolls_1.json') # Opening JSON file
    dice_num_1 = json.load(rolls_1) # returns JSON object as a dictionary
    num = 0
    for player in players:
        i = num
        num += 1 # logic for total number of player who are going to play in the game
        while(i < len(dice_num_1)): # condition for each player who will move a certain pattern of tiles in the game
            players[player]['moves'].append(dice_num_1[i]) # appending all possible moves in players dictionary for each player
            i += len(players) # loop will run until total number of/or length of all players

rolls_1()

# def rolls_2():
#     rolls_2 = open('rolls_2.json')  # Opening JSON file
#     dice_num_2 = json.load(rolls_2)  # returns JSON object as a dictionary
#     for dice2 in dice_num_2:  # Iterating through the json list
#         print(dice2, end="-")
# #rolls_2()

def buy_property(player_name, property_name):
    if property_name in properties_for_sell: # condition to check if the property exists in the property for sell list
        players[player_name]["color_owned"].append(total_properties[property_name]["colour"]) # appending property against player who now owns the coloured propoerty
        players[player_name]["balance"] = players[player_name]["balance"] - total_properties[property_name]["price"] # substracting the player balance from property price
        properties_for_rent.append(property_name) # adding property to the list for potential rent
        properties_for_sell.remove(property_name) # deleting property from list as it is now owned by a player
        owned_property.update({property_name:player_name}) # creating dictionary to see if the owned property exists against owner

def rent_property(player_name, property_name):
    doubled = 2 # doubled rent if player owns all coloured property
    if property_name in properties_for_rent:# checking property if exists in the property for rent array
        amount = total_properties[property_name]["price"]
        if players[owned_property[property_name]]["color_owned"].count(total_properties[property_name]["colour"]) == coloured_property[total_properties[property_name]["colour"]] :
        # logic for coloured property with regards to total number of properties in the json file if more were added code will dynamically check the condition
            amount *= doubled
        players[player_name]["balance"] = players[player_name]["balance"] - amount
        # otherwise keep substracting from balance as rent
        players[owned_property[property_name]]["balance"] = players[owned_property[property_name]]["balance"] + amount
        # The owner of the property gets the loyalty for owning the property
        if players[player_name]["balance"] < amount: # condition for bankruptcy if player has no more money left end_game
            end_game()

def end_game():
    i = 0
    for player in players:
        player_name = list(players.keys())
        print(f"Players_name {player_name[i]} and thier remaining balance {players[player]['balance']}")
        # finally printing the results
        i += 1
    sys.exit(players)

max_moves = 0
for player in players:
    if len(players[player]['moves']) > max_moves :
        max_moves = len(players[player]['moves'])
keys_name_properties = list(total_properties.keys())
# logic for getting the count of possible moves per person

def start_game():
    i=0
    while( i < max_moves ): # itterate through each move per person
        for player in players:
            if i > 0:
                players[player]['balance'] += 1 # adding one each step of moves
            if i >= len(players[player]['moves']): # if the player hits the end of all moves break the loop
                break
            players[player]["last_step"] += players[player]['moves'][i] # adding all the possible moves played in players array
            players[player]["last_step"] = players[player]["last_step"] % len(total_properties) # logic for avoiding list out of bounds
            if players[player]["last_step"] == 0:
                players[player]["last_step"]+=1
            if total_properties[keys_name_properties[players[player]["last_step"]]]["name"] in properties_for_sell:
                # logic for putting all the information into above mentioned function of (buy_property)
                buy_property(player,total_properties[keys_name_properties[players[player]["last_step"]]]["name"])
            else:
                rent_property(player,total_properties[keys_name_properties[players[player]["last_step"]]]["name"])
                # logic for putting all the information into above mentioned function of (rent_property)
        i+=1
start_game()