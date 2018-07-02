#lifepoints.py
#Author: Mike Hollis

startingLifeFilter = 1
lifepointval = 0
LifepointFilter = lifepointval
MainplayerLife = 0
OpponentLife = 0

import updater
import playerName

def DefineLife(parameter, lifepoints):
    if parameter == "Starting" or parameter == "starting":
        global startingLifeFilter
        if startingLifeFilter == 1:
            if int(lifepoints.isdigit()) == False:
                print("[Lifepoints Module]: Expected a numerical value. Returning 0.")
                return 0
            else:
                global lifepointval
                lifepointval = int(lifepoints)
                global OpponentLife
                OpponentLife = int(lifepoints)
                global MainplayerLife
                MainplayerLife = int(lifepoints)
                print("[Lifepoint Module]: Lifepoints set, and locked.")
        else:
            print("[Lifepoint Module]: Lifepoints is already locked.")
    if parameter == "Change" or parameter == "change":
        if int(lifepoints.isdigit()) == True:
            global LifepointFilter
            LifepointFilter = int(lifepoints)
            print("[Lifepoint Module]: Lifepoint default value has been changed. It will be applied to the next duel in this instance.")
        else:
            print("[Lifepoint Module]: A 'word' was used instead of a numerical value.")

def lifepointChecker():
    global OpponentLife
    global MainplayerLife
    #We need to check the lifepoints to see if its a negative value
    if int(OpponentLife) < 0:
        #Duel Result: Mainplayer Wins
        OpponentLife = int(0)
        return
    if int(MainplayerLife) < 0:
        #Duel Result: Opponent Wins
        MainplayerLife = int(0)
        return
    if int(MainplayerLife) < 0 and int(OpponentLife) < 0:
        #Duel Result: Draw
        MainplayerLife = int(0)
        OpponentLife = int(0)
        return
    else:
        print("[Lifepoint Module]: Lifepoints checked. No Negative Number.")
