# fire-fighting Weaknesses: Flying, Ground, Psychic, Water
# Resistances: Bug, Dark, Fire, Grass, Ice, Steel
# fire: weak = ground, water, rock | resist = bug, fire, grass, steel, ice, fairy
# fighting: weak = psychic, flying, fairy | resist = dark, rock, bug

def dual_type_chart(type1, type2):
    type3 = {
        "normal": 0,
        "fire": 0,
        "water": 0,
        "electric": 0,
        "grass": 0,
        "ice": 0,
        "fighting": 0,
        "poison": 0,
        "ground": 0,
        "flying": 0,
        "psychic": 0,
        "bug": 0,
        "rock": 0,
        "ghost": 0,
        "dragon": 0,
        "dark": 0,
        "steel": 0,
        "fairy": 0
    }
    for i in list(type3.keys()):
        if type1[i] == 1 and type2[i] == 1:
            type3[i] = 4
        elif type1[i] == 2 and type2[i] == 2:
            type3[i] = 5
        elif type1[i] == 3 or type2[i] == 3:
            type3[i] = 3
        elif (type1[i] == 1 and type2[i] == 2) or (type1[i] == 2 and type2[i] == 1):
            type3[i] = 0
        elif type1[i] == 1 or type2[i] == 1:
            type3[i] = 1
        elif type1[i] == 2 or type2[i] == 2:
            type3[i] = 2
    return type3