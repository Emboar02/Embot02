import random
import json
from type_matchups import type_mu
from type_defending_matchups import type_defend_mu
from dual_type import dual_type_chart

with open("data\moves.json", "r") as moves:
    moves_list = json.load(moves)

with open("data\mons.json", "r") as mons:
    pokemon_list = json.load(mons)

# battling through user-created functions
class Battle:
    # starts a battle
    def __init__(self, team = None, going_on = True):
        self._team = team
        self._going_on = going_on

    # formats and sets team so that is easy to understand and accessible
    def organize_team(self, information):
        team = {}
        information = json.loads(information)
        for i in range(0, 6):
            team[information["side"]["pokemon"][i]["details"].split(",")[0].replace("-", "").replace(" ", "").replace(".", "").lower()] = information["side"]["pokemon"][i]["moves"]
        self._team = team
    
    def getTeam(self):
        return self._team

    # keeps track of the current Pokemon on the field 
    def currentPokemon(self, information):
        current = information["side"]["pokemon"][0]["details"].split(",")[0]
        current = current.replace("-", "").replace(" ", "").replace(".", "").lower()
        if current[-2:] == r'\n': current = current[:-2]
        return current

    # removes pokemon from team if it faints
    def faint(self, pokemon):
        self._team.pop(pokemon) 

    # get info of moves of active pokemon
    def moves_info(self, information):
        active_moves = information["side"]["pokemon"][0]["moves"]
        return active_moves

    # handles switching of Pokemon 
    def switch(self, opponent_pokemon, information):
        if opponent_pokemon == None: return mons[random.randrange(0, len(mons))]
        mons = list(self.getTeam().keys())
        switch_position = {
            "name": None,
            "priority": 0
        }
        for i in mons:
            temp_effect = 0
            opp_pokemon_type = pokemon_list[opponent_pokemon["name"]]["types"]
            my_mon_type = pokemon_list[self.currentPokemon(information)]["types"]
            if len(opp_pokemon_type) > 1: # if opp has two types, makes new type chart
                type_chart = dual_type_chart(type_defend_mu[opp_pokemon_type[0].lower()], type_defend_mu[opp_pokemon_type[1].lower()])
                for j in my_mon_type:
                    j = j.lower()
                    if type_chart[j] == 1:
                        temp_effect += 1
                    elif type_chart[j] == 2:
                        temp_effect -= 1
                    elif type_chart[j] == 3:
                        temp_effect -= 3
                    elif type_chart[j] == 4:
                        temp_effect += 2
                    elif type_chart[j] == 5:
                        temp_effect -= 2
                if temp_effect > switch_position["priority"]:
                    switch_position["name"] == i
                    switch_position["priority"] == temp_effect
                temp_effect = 0
            else:
                for k in my_mon_type:
                    k = k.lower()
                    opp_pokemon_type = opp_pokemon_type[0].lower()
                    if type_defend_mu[opp_pokemon_type][k] == 1:
                        temp_effect += 1
                    elif type_defend_mu[opp_pokemon_type][k] == 2:
                        temp_effect -= 1
                    elif type_defend_mu[opp_pokemon_type][k] == 3:
                        temp_effect -= 3
                    elif type_defend_mu[opp_pokemon_type][k] == 4:
                        temp_effect += 2
                    elif type_defend_mu[opp_pokemon_type][k] == 5:
                        temp_effect -= 2
                if temp_effect > switch_position["priority"]:
                    switch_position["name"] == i
                    switch_position["priority"] == temp_effect
                temp_effect = 0
        if switch_position["name"] == None: switch_position["name"] = mons[random.randrange(0, len(mons))]
        return switch_position["name"]
        

    # puts moves in a priority list
    def move_selection_priority(self, information, opponent_pokemon):
        if "trapped" in information["active"][0]:
            return "/choose move " + information["active"][0]["moves"][0]["move"]
        statused = False
        my_mon = self.currentPokemon(information)
        my_mon_types = pokemon_list[my_mon]["types"]
        my_mon_hp = information["side"]["pokemon"][0]["condition"]
        if len(my_mon_hp) < 8:
            my_mon_hp = int(my_mon_hp.split("/")[0]) / int(my_mon_hp.split("/")[1])
        else:
            temp_hp = my_mon_hp.split(" ")[0]
            my_mon_hp = int(temp_hp.split("/")[0]) / int(temp_hp.split("/")[1])

        opponent_pokemon["name"] = opponent_pokemon["name"].replace("-", "").replace(" ", "").replace(".", "").lower()
        if opponent_pokemon["name"][-2:] == r'\n': opponent_pokemon["name"] = opponent_pokemon["name"][:-2]
        if len(opponent_pokemon["hp"]) < 8: # no status on opponent pokemon
            opp_mon_health_percentage = int(opponent_pokemon["hp"].split("/")[0]) / int(opponent_pokemon["hp"].split("/")[1])
        else: # status on opponent pokemon
            statused = True
            temp_hp = opponent_pokemon["hp"].split(" ")[0] # gotta remove status condition
            opp_mon_health_percentage = int(temp_hp.split("/")[0]) / int(temp_hp.split("/")[1])
        moves = self.moves_info(information) 
        opp_pokemon_type = pokemon_list[opponent_pokemon["name"]]["types"]
        effectiveness = self.effectiveness(opp_pokemon_type, moves) # gets effectiveness of moves against opposing pokemon
        move_to_use = {
            "name": None,
            "bp": 0,
        }
        priority = 0
        move_priorities = []
        for i in range(0, len(effectiveness)):
            counter = 0
            if information["active"][0]["moves"][i]["disabled"] == True:
                counter = -100
            else:
                if moves_list[moves[i]]["category"] == "Status":
                    if "boosts" in moves_list[moves[i]] and opp_mon_health_percentage == 1 and my_mon_hp > 0.8:
                        counter += 5
                    elif "status" in moves_list[moves[i]] and opp_mon_health_percentage > 0.8 and statused == False:
                        if moves_list[moves[i]]["status"] == "tox" and ("Poison" not in opp_pokemon_type or "Steel" not in opp_pokemon_type):
                            counter += 10
                        elif moves_list[moves[i]]["status"] == "psn" and ("Poison" not in opp_pokemon_type or "Steel" not in opp_pokemon_type):
                            counter += 6
                        elif moves_list[moves[i]]["status"] == "brn" and ("Fire" not in opp_pokemon_type):
                            counter += 8
                        elif moves_list[moves[i]]["status"] == "par" and ("Electric" not in opp_pokemon_type or "Ground" not in opp_pokemon_type):
                            counter += 7
                else:
                    if (effectiveness[i] == 1 or effectiveness[i] == 4):
                        counter += 4
                    elif effectiveness[i] == 0:
                        counter += 1
                    elif effectiveness[i] == 3:
                        counter -= 10
                    elif effectiveness[i] == 5 or effectiveness[i] == 2:
                        counter -= 4
                    if moves_list[moves[i]]["type"] in my_mon_types and (moves_list[moves[i]]["basePower"] > move_to_use["bp"]*1.1):
                        counter += 2
                    elif moves_list[moves[i]]["type"] in my_mon_types:
                        counter += 1
                    elif moves_list[moves[i]]["type"] not in my_mon_types and (moves_list[moves[i]]["basePower"] > move_to_use["bp"]*1.3):
                        counter += 1
            if counter > priority:
                priority = counter
                move_to_use["name"] = moves[i]
                move_to_use["bp"] = moves_list[moves[i]]["basePower"]
            move_priorities.append([moves[i], counter])
        if move_to_use["name"] == None:
            counter = 0
            return "/choose switch " + self.switch(opponent_pokemon, information)
        return "/choose move " + move_to_use["name"]

    # check if move is usable
    def move_check(self, move, information):
        move = 4

    # gets effectiveness of moves against opposing pokemon in list format
    def effectiveness(self, type, move):
        move_effectiveness = []
        if len(type) > 1: # if opp has two types, makes new type chart
            type_chart = dual_type_chart(type_defend_mu[type[0].lower()], type_defend_mu[type[1].lower()])
            counter = 0
            for i in move:
                move_effectiveness.append(type_chart[moves_list[i]["type"].lower()])
                counter += 1
            counter = 0
        else:
            counter = 0
            for i in move:
                move_effectiveness.append(type_defend_mu[type[0].lower()][moves_list[i]["type"].lower()])
                counter += 1
            counter = 0
        return move_effectiveness

    # decision on whether to switch or make a move
    def switch_or_move(self, choice):
        choice = 5 # placeholder

    # game ends, nothing is going on...
    def game_ends(self):
        self._going_on = False