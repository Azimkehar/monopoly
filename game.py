#this is monopoly game
import json # json file

owned_property = {}
total_properties = {}
properties_for_rent = []
properties_for_sell = []
players = {"Peter":{"balance":16,"color_owned":[]},"Billy":{"balance":16,"color_owned":[]},"Charlotte":{"balance":16,"color_owned":[]},"Sweedal":{"balance":16,"color_owned":[]}}

def board():
    board_rules = open('board.json')  # Opening JSON file
    board = json.load(board_rules)  # returns JSON object as a dictionary
    for properties in board:  # Iterate through the json list
        total_properties[properties['name']]=properties
    for property in total_properties:
        if property == "GO":
            continue
        properties_for_sell.append(property)

board()

def rolls_1():
    rolls_1 = open('rolls_1.json') # Opening JSON file
    dice_num_1 = json.load(rolls_1) # returns JSON object as a dictionary
    for dice1 in dice_num_1: # Iterating through the json list
        print(dice1,end="-")
#rolls_1()

def rolls_2():
    rolls_2 = open('rolls_2.json')  # Opening JSON file
    dice_num_2 = json.load(rolls_2)  # returns JSON object as a dictionary
    for dice2 in dice_num_2:  # Iterating through the json list
        print(dice2, end="-")
#rolls_2()

def buy_property(player_name, property_name):
    if property_name in properties_for_sell:
        players[player_name]["color_owned"].append(total_properties[property_name]["colour"])
        players[player_name]["balance"] = players[player_name]["balance"] - total_properties[property_name]["price"]
        properties_for_rent.append(property_name)
        properties_for_sell.remove(property_name)
        owned_property.update({property_name:player_name})
buy_property("Peter","Fast Kebabs")

def rent_property(player_name, property_name):
    if property_name in properties_for_rent:
        amount = total_properties[property_name]["price"]
        if players[owned_property[property_name]]["color_owned"].count(total_properties[property_name]["colour"]) >= 2:
            amount *= 2
        if players[player_name]["balance"] < amount:
            end_game()
        players[player_name]["balance"] = players[player_name]["balance"] - amount
        players[owned_property[property_name]]["balance"] = players[owned_property[property_name]]["balance"] + amount

rent_property("Billy","Fast Kebabs")
buy_property("Peter","The Burvale")
rent_property("Charlotte","The Burvale")

#print(players)
#print(properties_for_sell)
#print(properties_for_rent)
#print(owned_property)

#def total_money_acquired():

#total_money_acquired()

def end_game():
    print("The game has ended, thanks for playing")