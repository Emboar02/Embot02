# every type and their matchups
# x: {}, where x is defending type, and inside bracket has attacking types
# 0 = normal, 1 = super effective, 2 = not very effective, 3 = immune, 4 = 4x effective, 5 = 4x not very effective

type_defend_mu = {
    "normal": {
        "normal": 0,
        "fire": 0,
        "water": 0,
        "electric": 0,
        "grass": 0,
        "ice": 0,
        "fighting": 1,
        "poison": 0,
        "ground": 0,
        "flying": 0,
        "psychic": 0,
        "bug": 0,
        "rock": 0,
        "ghost": 3,
        "dragon": 0,
        "dark": 0,
        "steel": 0,
        "fairy": 0
    },
    "fire": {
        "normal": 0,
        "fire": 2,
        "water": 1,
        "electric": 0,
        "grass": 2,
        "ice": 2,
        "fighting": 0,
        "poison": 0,
        "ground": 1,
        "flying": 0,
        "psychic": 0,
        "bug": 2,
        "rock": 1,
        "ghost": 0,
        "dragon": 0,
        "dark": 0,
        "steel": 2,
        "fairy": 2
    },
    "water": {
        "normal": 0,
        "fire": 2,
        "water": 2,
        "electric": 1,
        "grass": 1,
        "ice": 2,
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
        "steel": 2,
        "fairy": 0
    },
    "electric": {
        "normal": 0,
        "fire": 0,
        "water": 0,
        "electric": 2,
        "grass": 0,
        "ice": 0,
        "fighting": 0,
        "poison": 0,
        "ground": 1,
        "flying": 2,
        "psychic": 0,
        "bug": 0,
        "rock": 0,
        "ghost": 0,
        "dragon": 0,
        "dark": 0,
        "steel": 2,
        "fairy": 0
    },
    "grass": {
        "normal": 0,
        "fire": 1,
        "water": 2,
        "electric": 2,
        "grass": 2,
        "ice": 1,
        "fighting": 0,
        "poison": 1,
        "ground": 2,
        "flying": 1,
        "psychic": 0,
        "bug": 1,
        "rock": 0,
        "ghost": 0,
        "dragon": 0,
        "dark": 0,
        "steel": 0,
        "fairy": 0
    },
    "ice": {
        "normal": 0,
        "fire": 1,
        "water": 0,
        "electric": 0,
        "grass": 0,
        "ice": 2,
        "fighting": 1,
        "poison": 0,
        "ground": 0,
        "flying": 0,
        "psychic": 0,
        "bug": 0,
        "rock": 1,
        "ghost": 0,
        "dragon": 0,
        "dark": 0,
        "steel": 1,
        "fairy": 0
    }, 
    "fighting": {
        "normal": 0,
        "fire": 0,
        "water": 0,
        "electric": 0,
        "grass": 0,
        "ice": 0,
        "fighting": 0,
        "poison": 0,
        "ground": 0,
        "flying": 1,
        "psychic": 1,
        "bug": 2,
        "rock": 2,
        "ghost": 0,
        "dragon": 0,
        "dark": 2,
        "steel": 0,
        "fairy": 1
    }, 
    "poison": {
        "normal": 0,
        "fire": 0,
        "water": 0,
        "electric": 0,
        "grass": 2,
        "ice": 0,
        "fighting": 2,
        "poison": 2,
        "ground": 1,
        "flying": 0,
        "psychic": 1,
        "bug": 2,
        "rock": 0,
        "ghost": 0,
        "dragon": 0,
        "dark": 0,
        "steel": 0,
        "fairy": 2
    }, 
    "ground": {
        "normal": 0,
        "fire": 0,
        "water": 1,
        "electric": 3,
        "grass": 1,
        "ice": 1,
        "fighting": 0,
        "poison": 2,
        "ground": 0,
        "flying": 0,
        "psychic": 0,
        "bug": 0,
        "rock": 2,
        "ghost": 0,
        "dragon": 0,
        "dark": 0,
        "steel": 0,
        "fairy": 0
    }, 
    "flying": {
        "normal": 0,
        "fire": 0,
        "water": 0,
        "electric": 1,
        "grass": 2,
        "ice": 1,
        "fighting": 2,
        "poison": 0,
        "ground": 3,
        "flying": 0,
        "psychic": 0,
        "bug": 2,
        "rock": 1,
        "ghost": 0,
        "dragon": 0,
        "dark": 0,
        "steel": 0,
        "fairy": 0
    }, 
    "psychic": {
        "normal": 0,
        "fire": 0,
        "water": 0,
        "electric": 0,
        "grass": 0,
        "ice": 0,
        "fighting": 2,
        "poison": 0,
        "ground": 0,
        "flying": 0,
        "psychic": 2,
        "bug": 1,
        "rock": 0,
        "ghost": 1,
        "dragon": 0,
        "dark": 1,
        "steel": 0,
        "fairy": 0
    }, 
    "bug": {
        "normal": 0,
        "fire": 1,
        "water": 0,
        "electric": 0,
        "grass": 2,
        "ice": 0,
        "fighting": 2,
        "poison": 0,
        "ground": 2,
        "flying": 1,
        "psychic": 0,
        "bug": 0,
        "rock": 1,
        "ghost": 0,
        "dragon": 0,
        "dark": 0,
        "steel": 0,
        "fairy": 0
    }, 
    "rock": {
        "normal": 0,
        "fire": 2,
        "water": 1,
        "electric": 0,
        "grass": 1,
        "ice": 0,
        "fighting": 1,
        "poison": 2,
        "ground": 1,
        "flying": 2,
        "psychic": 0,
        "bug": 0,
        "rock": 0,
        "ghost": 0,
        "dragon": 0,
        "dark": 0,
        "steel": 1,
        "fairy": 0
    }, 
    "ghost": {
        "normal": 3,
        "fire": 0,
        "water": 0,
        "electric": 0,
        "grass": 0,
        "ice": 0,
        "fighting": 3,
        "poison": 2,
        "ground": 0,
        "flying": 0,
        "psychic": 0,
        "bug": 2,
        "rock": 0,
        "ghost": 1,
        "dragon": 0,
        "dark": 1,
        "steel": 0,
        "fairy": 0
    }, 
    "dragon": {
        "normal": 0,
        "fire": 2,
        "water": 2,
        "electric": 2,
        "grass": 2,
        "ice": 1,
        "fighting": 0,
        "poison": 0,
        "ground": 0,
        "flying": 0,
        "psychic": 0,
        "bug": 0,
        "rock": 0,
        "ghost": 0,
        "dragon": 1,
        "dark": 0,
        "steel": 0,
        "fairy": 1
    }, 
    "dark": {
        "normal": 0,
        "fire": 0,
        "water": 0,
        "electric": 0,
        "grass": 0,
        "ice": 0,
        "fighting": 1,
        "poison": 0,
        "ground": 0,
        "flying": 0,
        "psychic": 3,
        "bug": 1,
        "rock": 0,
        "ghost": 2,
        "dragon": 0,
        "dark": 2,
        "steel": 0,
        "fairy": 1
    }, 
    "steel": {
        "normal": 2,
        "fire": 1,
        "water": 0,
        "electric": 0,
        "grass": 2,
        "ice": 2,
        "fighting": 1,
        "poison": 3,
        "ground": 1,
        "flying": 2,
        "psychic": 2,
        "bug": 2,
        "rock": 2,
        "ghost": 0,
        "dragon": 2,
        "dark": 0,
        "steel": 2,
        "fairy": 2
    }, 
    "fairy": {
        "normal": 0,
        "fire": 0,
        "water": 0,
        "electric": 0,
        "grass": 0,
        "ice": 0,
        "fighting": 2,
        "poison": 1,
        "ground": 0,
        "flying": 0,
        "psychic": 0,
        "bug": 2,
        "rock": 0,
        "ghost": 0,
        "dragon": 3,
        "dark": 2,
        "steel": 1,
        "fairy": 0
    }
}
