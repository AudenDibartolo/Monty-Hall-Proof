import random


def switch():
    tries = 0
    numWin = 0
    for i in range(10000):
        tries += 1
        doors = ['goat', 'goat', 'goat']
        doors[random.randint(0,2)] = 'prize'
        firstChoice = 1
        for door in doors:
            if door == 'goat' and firstChoice != doors.index(door):
                doors.pop(doors.index(door))
            
        if doors[firstChoice] != 'prize':
            numWin += 1
    
    return round(numWin/tries, 2)
        
def stay():
    tries = 0
    numWin = 0
    for i in range(10000):
        tries += 1
        doors = ['goat', 'goat', 'goat']
        doors[random.randint(0,2)] = 'prize'
        firstChoice = 1
        for door in doors:
            if door == 'goat' and firstChoice != doors.index(door):
                doors.pop(doors.index(door))
            
        if doors[firstChoice] == 'prize':
            numWin += 1
    
    return round(numWin/tries, 2)
        

    
print(stay() * 100)