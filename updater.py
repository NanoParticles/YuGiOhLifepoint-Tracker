#updater.py
#Author: Mike Hollis

import lifepoints
import playerName

drawFilter = 0
#For Damage Calculation
def updateLife(name, damage):
    global drawFilter
    if name == playerName.MainplayerName or name == playerName.OpponentName:
        global damageTaken
        if name == playerName.MainplayerName:
            global OldLifeM
            OldLifeM = lifepoints.MainplayerLife
            damageTaken = damage
            global NewLifeM
            NewLifeM = int(OldLifeM) - int(damageTaken)
            lifepoints.MainplayerLife = str(NewLifeM)
            lifepoints.lifepointChecker()
            if lifepoints.OpponentLife == 0 or lifepoints.MainplayerLife == 0: 
                if lifepoints.OpponentLife == 0:
                    print(" ")
                    print("" + str(playerName.OpponentName) + " : " + str(lifepoints.OpponentLife))
                    print("> " + str(playerName.MainplayerName) + " < : " + str(lifepoints.MainplayerLife))
                    print(" ")
                    print("Mainplayer wins!")
                    return
                if lifepoints.MainplayerLife == 0:
                    print(" ")
                    print("> " + str(playerName.OpponentName) + " < : " + str(lifepoints.OpponentLife))
                    print("" + str(playerName.MainplayerName) + " : " + str(lifepoints.MainplayerLife))
                    print(" ")
                    print("Opponent wins!")
                    return
        if name == playerName.OpponentName:
            global OldLifeO
            OldLifeO = lifepoints.OpponentLife
            damageTaken = damage
            global NewLifeO
            NewLifeO = int(OldLifeO) - int(damageTaken)
            lifepoints.OpponentLife = str(NewLifeO)
            lifepoints.lifepointChecker()
            if lifepoints.OpponentLife == 0 or lifepoints.MainplayerLife == 0: 
                if lifepoints.OpponentLife == 0:
                    print(" ")
                    print("" + str(playerName.OpponentName) + " : " + str(lifepoints.OpponentLife))
                    print("> " + str(playerName.MainplayerName) + " < : " + str(lifepoints.MainplayerLife))
                    print(" ")
                    print("Mainplayer wins!")
                    return
                if lifepoints.MainplayerLife == 0:
                    print(" ")
                    print("> " + str(playerName.OpponentName) + " < : " + str(lifepoints.OpponentLife))
                    print("" + str(playerName.MainplayerName) + " : " + str(lifepoints.MainplayerLife))
                    print(" ")
                    print("Opponent wins!")
                    return
                        
    else:
        print("[Updater Module]: Expected a player name.")
        return

def gainLife(name, amount):
    if name == playerName.OpponentName or name == playerName.MainplayerName:
        global amountGained
        if name == playerName.OpponentName:
            amountGained = amount
            global OldLifeO
            OldLifeO = lifepoints.OpponentLife
            global NewLifeO
            NewLifeO = int(OldLifeO) + int(amountGained)
            lifepoints.OpponentLife = str(NewLifeO)
            print("Life gained.")
            return
        if name == playerName.MainplayerName:
            amountGained = amount
            global OldLifeM
            OldLifeM = str(lifepoints.MainplayerLife)
            global NewLifeM
            NewLifeM = int(OldLifeM) + int(amountGained)
            lifepoints.MainplayerLife = NewLifeM
            print("Life gained.")
            return
        else:
            print("Invalid Player.")
            return
    if amount == 0:
        print("Okay. You gained 0 life. I bet you feel great gaining that amount.")
        return
