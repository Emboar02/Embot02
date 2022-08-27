import websocket
import json
import requests
from config import username, password, rooms, header, admin, avatar
from battle import Battle

current_battle = None
current_information = None
opp_pokemon = {
    "name": None,
    "hp": None
}

def parser(wsapp, message):
    #websocket.enableTrace(True) # for debugging purposes
    message = message.split("|")
    if message[1] == "challstr": # creates necessary string to log in
        if len(message[3]) != 0:
            challstr = message[2] + "|" + message[3]
            log_in(challstr)
    if message[1] == "pm":
        pm_parser(message[2], message[4])
    if message[-2] == "gametype":
        global current_battle
        current_battle = Battle()
    elif message[1] == "request":
        if current_battle.getTeam() == None:
            current_battle.organize_team(message[2])
        global current_information
        current_information = json.loads(message[2])
        if "forceSwitch" in current_information:
            global opp_pokemon
            battle(message[0], current_information, current_battle, opp_pokemon)
    elif message[-2] == "turn":
        for i in range(0, len(message)):
            if message[i][0:4] == "p1a:":
                if message[i][-2:] == r'\n':
                    opp_pokemon["name"] = message[i][5:-2]
                else: 
                    opp_pokemon["name"] = message[i][5:]
                if message[i-1] == "switch":
                    opp_pokemon["hp"] = message[i+2][:-1]
                elif message[i-1] == "-damage":
                    opp_pokemon["hp"] = message[i+1]
        battle(message[0], current_information, current_battle, opp_pokemon)

def log_in(challstr):
    body = {
        "act": "login",
        "name": username,
        "pass": password, 
        "challstr": challstr
    }
    # sends a post request to the server
    r = requests.post("https://play.pokemonshowdown.com/~~showdown/action.php", headers = header, data = body)
    assertion = r.text.partition('"assertion":"')[2]
    assertion = assertion[:-2]
    # finishes log-in process to the server
    wsapp.send("|/trn " + username + "," + avatar + "," + assertion)
    # joins rooms that are wanted
    if len(rooms) > 0:
        for i in rooms:
            wsapp.send("|/join " + i)
    wsapp.send("|/avatar " + avatar)

def pm_parser(sender, message):
    if message[0:10] == "/challenge":
        if message[11:] == "gen8randombattle":
            wsapp.send("|/utm null")
            wsapp.send("|/accept " + sender)
        else:
            wsapp.send("|/reject " + sender)
            wsapp.send("|/pm " + sender + ", I do not support battling in this format. Send .help for more info.")
    elif message == ".kill" and sender[1:] == admin:
        wsapp.close()
    elif message == ".help":
            wsapp.send("|/pm " + sender + ", Hi! I am a bot programmed by " + admin + ". If you want to battle me, I can battle in [Gen 8] Random Battle, though I am still in development and could stop working during a battle.")

def battle(battle_link, information, current_battle, opponent = None):
    currentMon = current_battle.currentPokemon(information)
    if "active" in information:
        wsapp.send("|/msgroom " + battle_link[1:-1] + ", " + current_battle.move_selection_priority(information, opponent))
    elif "forceSwitch" in information:
        current_battle.faint(currentMon)
        wsapp.send("|/msgroom " + battle_link[1:-1] + ", " + "/choose switch " + current_battle.switch(opponent, information))
    
# connects to websocket
wsapp = websocket.WebSocketApp("wss://sim3.psim.us/showdown/websocket", on_message=parser)
# makes it an endless connection
wsapp.run_forever()