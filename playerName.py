#playerNameVal.py
#Author: Mike Hollis

OpponentName = ""
MainplayerName = ""
SetNameLockOpponent = 1
SetNameLockMainPlayer = 1
NewOpponentName = ""
NewMainPlayerName = ""

def DefineName(parameter, fieldpos, name):
    if parameter == "Set Name" or parameter == "set name":
        if fieldpos == "Opponent" or parameter == "opponent":
            global SetNameLockOpponent
            if SetNameLockOpponent == 1:
                global OpponentName
                OpponentName = name
                print("[Player Name Module]: Opponent's Name set, and locked.")
                SetNameLockOpponent = 0
                return
            else:
                print("[Player Name Module]: The Opponent's name is locked in. Use the parameter, 'change name'.")
        if fieldpos == "Mainplayer" or fieldpos == "mainplayer":
            global SetNameLockMainPlayer
            if SetNameLockMainPlayer == 1:
                global MainplayerName
                MainplayerName = name
                print("[Player Name Module]: Main Player's Name set, and locked.")
                SetNameLockMainPlayer = 0
                return
            else:
                print("[Player Name Module]: The Main Player's Name is locked in. Use the parameter, 'change name'.")
                return
        else:
            print("[Player Name Module]: Invaild Field Side. Expected Opponent, or Main Player.")
    if parameter == "Change Name" or parameter == "change name":
        if fieldpos == "Opponent" or fieldpos == "opponent":
            NewOpponentName = str(name)
            OpponentName = NewOpponentName
            print("[Player Name Module]: Opponent Name has been changed.")
            return
        if fieldpos == "Mainplayer" or fieldpos == "mainplayer":
            NewMainPlayerName = str(name)
            MainplayerName = NewMainPlayerName
            print("[Player Name Module]: Main Player Name has been changed.")
            return
        else:
            print("[Player Name Module]: Invaild Field Side. Expected Opponent, or Main Player.")
            return
    else:
        print("[Player Name Module]: Invaild parameter. Expected 'Set Name', or 'Change Name'.")
        return


        
