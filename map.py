import json

def get_map():
    WALKABLE = 0
    NON_WALKABLE = 1
    WOOD = 2
    map = []
    f = open("mapstate.json","r")
    map = json.loads(f.read())
    f.close()
    
    return map