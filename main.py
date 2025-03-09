# main.py
# Author: NanoParticles

title = "Lifepoint Tracker"
version = "1.1"
print(str(title) + " v" + str(version))
print(" ")

import playerName
import lifepoints
import updater
import globalvar
import math

#Setting the window title

import ctypes
ctypes.windll.kernel32.SetConsoleTitleW("Lifepoint Tracker")

nameLock = 0
lifeLock = 0
ChallengeTurn = 0
firstStrike = ""
awaitingExit1 = 0
awaitingExit2 = 0
toggleDamageCalc = int(1)
damageCalcVar = "ENABLED"

def endTurn():
    global ChallengeTurn
    if ChallengeTurn == 1:
        ChallengeTurn = 2
        print("Turn End.")
        return
    if ChallengeTurn == 2:
        ChallengeTurn = 1
        print("Turn End.")
        return

def optionsUI():
    global ChallengeTurn
    global nameLock
    global lifeLock
    global awaitingExit1
    global awaitingExit2
    global damageCalcVar
    global toggleDamageCalc
    print("+=========+")
    print("| Options |")
    print("+=========+")
    print(" ")
    print("Default Lifepoint value: " + str(lifepoints.lifepointval))
    print("Mainplayer Name: " + str(playerName.MainplayerName))
    print("Opponent Name: " + str(playerName.OpponentName))
    print("Auto-Calculations : " + str(damageCalcVar))
    print(" ")
    print("+----------+")
    print("| Commands |")
    print("+----------+")
    print(" ")
    print("Change Name - Changes the names of the players")
    print("Restart by Setting Lifepoints - Changes the default lifepoints and restarts the duel")
    print("Restart Duel - Restarts the duel")
    print("Reset Duel - Resets all defined varibles, creates a new duel, and navigates to the command line user interface")
    print("Toggle Damage Calculation: When Enabled, it automatically calculates the damage inflicted between players. Default: Enabled")
    print("Return to Duel Menu - Goes back to the Duel Menu")
    print(" ")
    global optionsInput
    print("Please enter a command.")
    optionsInput = input('Duel Menu > Options > ')
    if optionsInput == "Change Name" or optionsInput == "change name":
        global OptioninputNameO
        print("What's your Opponent's Name?")
        OptioninputNameO = input()
        print("Enter your name.")
        global OptioninputNameM
        OptioninputNameM = input()
        playerName.DefineName("Change Name", "Opponent", OptioninputNameO)
        playerName.DefineName("Change Name", "Mainplayer", OptioninputNameM)
        optionsUI()
        return
    if optionsInput == "Restart by Setting Lifepoints" or optionsInput == "restart by setting lifepoints" or optionsInput == "restart by setting life":
        print("WARNING: This will restart the duel. Are you sure you want to do this?")
        restartWarn = input('Speak now or forever hold your peace: ')
        if restartWarn == "Yes" or restartWarn == "yes":
            print("What is the new starting lifepoints?")
            NewLifepointVal = input()
            if int(NewLifepointVal.isdigit()) == True:
                lifepoints.DefineLife("change", NewLifepointVal)
                #Lifepoints changed. Now to apply the changes when the user leaves the Options menu
                awaitingExit1 = 1
                print("The changes will apply when you return to the duel menu")
                optionsUI()
                return
            else:
                print("Invalid input. Expected a numerical value.")
                optionsUI()
                return
        if restartWarn == "No" or restartWarn == "no":
            optionsUI()
            return
    if optionsInput == "Restart" or optionsInput == "restart":
        print("WARNING! This will restart the duel. Are you sure you want this?")
        restartWarn = input('Speak now or forever hold your peace: ')
        if restartWarn == "Yes" or restartWarn == "yes":
            awaitingExit2 = 1
            print("The duel will restart when you return to the duel menu.")
            optionsUI()
            return
        if restartWarn == "No" or restartWarn == "no":
            optionsUI()
            return
    if optionsInput == "Reset Duel" or optionsInput == "reset duel":
        print("WARNING: This will reset the duel. Are you sure you want to do this?")
        global resetWarn
        resetWarn = input('Speak now or forever hold your piece: ')
        if resetWarn == "Yes" or resetWarn == "No" or resetWarn == "yes" or resetWarn == "no":
            if resetWarn == "Yes" or resetWarn == "yes":
                global firstStrike
                nameLock = 0
                lifeLock = 0
                ChallengeTurn = 0
                playerName.SetNameLockOpponent = 1
                playerName.SetNameLockMainPlayer = 1
                playerName.OpponentName = ""
                playerName.MainplayerName = ""
                lifepoints.startingLifeFilter = 1
                lifepoints.lifepointval = 0
                firstStrike = ""
                print("Values reset. Returning to command UI...")
                print(" ")
                cmdUI()
                return
            if resetWarn == "No" or resetWarn == "no":
                optionsUI()
                return
        else:
            print("Invalid Choice. Returning to Options...")
            optionsUI()
            return
    if optionsInput == "Toggle Damage Calculation" or optionsInput == "toggle damage calculation":
        if toggleDamageCalc == int(1):
            damageCalcVar = "DISABLED"
            toggleDamageCalc = int(0)
            print("Damage Calculation is disabled.")
            optionsUI()
            return
        if toggleDamageCalc == int(0):
            damageCalcVar = "ENABLED"
            toggleDamageCalc = int(1)
            print("Damage Calculation is enabled.")
            optionsUI()
            return
    if optionsInput == "Return to Duel Menu" or optionsInput == "return to duel menu":
        if awaitingExit1 == 1:
            #Time to change the lifepoints and restart the duel
            lifepoints.MainplayerLife = lifepoints.LifepointFilter
            lifepoints.OpponentLife = lifepoints.LifepointFilter
            lifepoints.lifepointval = lifepoints.LifepointFilter
            #We set the counter, but we need to redefine the turn rotation
            print("Redetermining the turn rotation.")
            print(" ")
            print("Who's attacking first?")
            redeterminationTurn = input()
            if redeterminationTurn == playerName.OpponentName or redeterminationTurn == playerName.MainplayerName:
                if redeterminationTurn == playerName.OpponentName:
                    ChallengeTurn = 1
                    awaitingExit1 = 0
                    awaitingExit2 = 0
                    duelmenuUI()
                    return
                if redeterminationTurn == playerName.MainplayerName:
                    ChallengeTurn = 2
                    awaitingExit1 = 0
                    awaitingExit2 = 0
                    duelmenuUI()
                    return
                else:
                    print("Expected Player Name. Returning to Options...")
                    optionsUI()
                    awaitExit1 = 1
                    return
        if awaitingExit2 == 1:
            lifepoints.MainplayerLife = lifepoints.lifepointval
            lifepoints.OpponentLife = lifepoints.lifepointval
            #Lifepoints reset. Redetermining turn.
            print("Redetermining the turn rotation...")
            print(" ")
            print("Who's attacking first?")
            redeterminationTurn = input()
            if redeterminationTurn == playerName.OpponentName or redeterminationTurn == playerName.MainplayerName:
                if redeterminationTurn == playerName.OpponentName:
                    ChallengeTurn = 1
                    awaitingExit1 = 0
                    awaitingExit2 = 0
                    duelmenuUI()
                    return
                if redeterminationTurn == playerName.MainplayerName:
                    ChallengeTurn = 2
                    awaitingExit1 = 0
                    awaitingExit2 = 0
                    duelmenuUI()
                    return
                else:
                    print("Expected Player Name. Returning to Options...")
                    optionsUI()
                    awaitExit2 = 1
                    return
        else:
            duelmenuUI()
            return
    if optionsInput == "":
        print("You didn't type anything in.")
        optionsUI()
        return
    else:
        print("Invalid command.")
        optionsUI()
        return
def monsterStatUI():
    global monsterStatCalcInput
    global baseAttackInput
    global baseDefenseInput
    global amountAddedInput
    global amountSubtractedInput
    global result
    baseAttackInput = 0
    baseDefenseInput = 0
    amountAddedInput = 0
    amountSubtractedInput = 0
    result = 0
    print(" ")
    print("+=========================+")
    print("| Monster Stat Calculator |")
    print("+=========================+")
    print(" ")
    print("+----------+")
    print("| Commands |")
    print("+----------+")
    print(" ")
    print("Add Attack - adds the base attack from x amount")
    print("Subtract Attack - Subtracts the base attack from x amount")
    print("Half Attack - Halves the base attack")
    print("Double Attack - doubles the base attack.")
    print("Add Defense - adds the base defense from x amount")
    print("Subtract Defense - Subtracts the base defense from x amount")
    print("Return to Duel Menu - returns to the duel menu")
    print(" ")
    print("Please enter a command.")
    monsterStatCalcInput = input('Duel Menu > Monster Stat Calculator > ')
    if monsterStatCalcInput == "Add Attack" or monsterStatCalcInput == "add attack" or monsterStatCalcInput == "add atk":
        print("Whats the base attack of the monster?")
        baseAttackInput = input()
        if int(baseAttackInput.isdigit()) == True:
            print("How much is being added?")
            amountAddedInput = input()
            if int(amountAddedInput.isdigit()) == True:
                result = int(baseAttackInput) + int(amountAddedInput)
                print("Your monster's new attack is " + str(result) + ".")
                monsterStatUI()
                return
            else:
                print("Invalid input. Please try again.")
                monsterStatUI()
                return
        else:
            print("Invalid input. Please try again.")
            monsterStatUI()
            return
    if monsterStatCalcInput == "Subtract Attack" or monsterStatCalcInput == "subtract attack" or monsterStatCalcInput == "subtract atk":
        print("Whats the base attack of the monster?")
        baseAttackInput = input()
        if int(baseAttackInput.isdigit()) == True:
            print("How much is being subtracted?")
            amountSubtractedInput = input()
            if int(amountSubtractedInput.isdigit()) == True:
                result = int(baseAttackInput) - int(amountSubtractedInput)
                print("Your monster's new attack is " + str(result) + ".")
                monsterStatUI()
                return
            else:
                print("Invalid input. Please try again.")
                monsterStatUI()
                return
        else:
            print("Invalid input. Please try again.")
            monsterStatUI()
            return
    if monsterStatCalcInput == "Half Attack" or monsterStatCalcInput == "half attack":
        print("Whats the base attack of the monster?")
        baseAttackInput = input()
        if int(baseAttackInput.isdigit()) == True:
            result = int(baseAttackInput) / int(2)
            print("Your monster's new attack is " + str(math.trunc(result)) + ".")
            monsterStatUI()
            return
        else:
            print("Invalid input. Please try again.")
            monsterStatUI()
            return
    if monsterStatCalcInput == "Double Attack" or monsterStatCalcInput == "double attack":
        print("Whats the base attack of the monster?")
        baseAttackInput = input()
        if int(baseAttackInput.isdigit()) == True:
            result = int(baseAttackInput) * int(2) 
            print("Your monster's new attack is " + str(result) + ".")
            monsterStatUI()
            return
        else:
            print("Invalid input. Please try again.")
            monsterStatUI()
            return
    if monsterStatCalcInput == "Add Defense" or monsterStatCalcInput == "add defense":
        print("Whats the base defense of the monster?")
        baseDefenseInput = input()
        if int(baseDefenseInput.isdigit()) == True:
            print("How much is being added?")
            amountAddedInput = input()
            if int(amountAddedInput.isdigit()) == True:
                result = int(baseDefenseInput) + int(amountAddedInput)
                print("Your monster's new defense is " + str(result) + ".")
                monsterStatUI()
                return
            else:
                print("Invalid input. Please try again.")
                monsterStatUI()
                return
        else:
            print("Invalid input. Please try again.")
            monsterStatUI()
            return
    if monsterStatCalcInput == "Subtract Defense" or monsterStatCalcInput == "subtract defense":
        print("Whats the base defense of the monster?")
        baseDefenseInput = input()
        if int(baseDefenseInput.isdigit()) == True:
            print("How much is being subtracted?")
            amountSubtractedInput = input()
            if int(amountSubtractedInput.isdigit()) == True:
                result = int(baseDefenseInput) - int(amountSubtractedInput)
                print("Your monster's new attack is " + str(result) + ".")
                monsterStatUI()
                return
            else:
                print("Invalid input. Please try again.")
                monsterStatUI()
                return
        else:
            print("Invalid input. Please try again.")
            monsterStatUI()
            return
    if monsterStatCalcInput == "Return to Duel Menu" or monsterStatCalcInput == "return to duel menu":
        duelmenuUI()
        return
    if monsterStatCalcInput == "":
        print("You didn't type anything.")
        monsterStatUI()
        return
    else:
        print("Invalid command.")
        monsterStatUI()
        return
    

def duelmenuUI():
    global duelmenuInput
    global inflictDamage
    global attackUsingDEF
    global inflictDamageUsingDEF
    global opponentMonsterPos
    global opponentMonsterATK
    global opponentMonsterDEF
    global highestMonster
    global inflictDamage
    global inflictDamageUsingDEF
    global attackUsingDEF
    global damageFilter
    global piercingDamageInput
    global ChallengeTurn
    global gainInput
    global payAmount
    global toggleDamageCalc
    if ChallengeTurn == 1:
        print(" ")
        print("+===================+")
        print("|     Duel Menu     |")
        print("+===================+")
        print(" ")
        print("+------------+")
        print("| Lifepoints |")
        print("+------------+")
        print(" ")
        print("> " + str(playerName.MainplayerName) + " < : " + str(lifepoints.MainplayerLife))
        print(str(playerName.OpponentName) + " : " + str(lifepoints.OpponentLife))
        print(" ")
        print("+----------+")
        print("| Commands |")
        print("+----------+")
        print(" ")
        print("Gain Life - Increases lifepoints by x amount")
        print("Pay Life - Pays x amount of lifepoints")
        if toggleDamageCalc == int(1):
            print("Attack Directly - Attack your opponent directly")
            print("Attack Monster - Attack your opponent's monster")
        else:
            print("Damage Lifepoints - Inflicts damage your Opponent's lifepoints by x amount")
        print("Options - Navigates to the Options")
        print("Monster Stat Calculator - Opens the monster stat calculator")
        print("End Turn - Ends your turn")
        print("Quit Duel - Quits the duel by exiting the module.")
        print(" ")
        print("Please enter a command.")
        duelmenuInput = input('Lifepoint Tracker> Duel Menu> ')
        if duelmenuInput == "Gain Life" or duelmenuInput == "gain life":
            print("How much did you gain?")
            gainInput = input()
            if int(gainInput.isdigit()) == False:
                print("Expected a number.")
                duelmenuUI()
                return
            else:
                updater.gainLife(playerName.MainplayerName, gainInput)
                duelmenuUI()
                gainInput = 0
                return
        if duelmenuInput == "Pay Life" or duelmenuInput == "pay life":
            print("How much is being paid?")
            payAmount = input()
            if int(payAmount.isdigit()) == True:
                updater.updateLife(playerName.MainplayerName, payAmount)
                print("Amount paid.")
                if int(lifepoints.MainplayerLife) == 0:
                    lifelock = 0
                    lifepoints.lifepointval = 0
                    cmdUI()
                    return
        if duelmenuInput == "Attack Directly" or duelmenuInput == "attack directly" or duelmenuInput == "atk directly":
            if toggleDamageCalc == int(0):
                print("Damage Calculations is disabled. To enable, go to options.")
                duelmenuUI()
                return
            print("Are you attacking using your monster's Defense?")
            attackUsingDEF = input()
            if attackUsingDEF == "Yes" or attackUsingDEF == "yes":
                print("What's your monsters defense?")
                inflictDamageUsingDEF = input()
                if int(inflictDamageUsingDEF.isdigit()) == True:
                    updater.updateLife(playerName.OpponentName, inflictDamageUsingDEF)
                    if int(lifepoints.OpponentLife) == 0:
                        lifelock = 0
                        lifepoints.lifepointval = 0
                        cmdUI()
                        return
                    else:
                        duelmenuUI()
                        return
                else:
                    print("Expected a numerical value.")
                    duelmenuUI()
                    return
            if attackUsingDEF == "No" or attackUsingDEF == "no":
                print("What's your monster's attack?")
                inflictDamage = input()
                if int(inflictDamage.isdigit()) == True:
                    updater.updateLife(str(playerName.OpponentName), inflictDamage)
                    if int(lifepoints.OpponentLife) == 0:
                        cmdUI()
                        return
                    else:
                        duelmenuUI()
                        return
                else:
                    print("Expected a numerical value.")
                    duelmenuUI()
                    return
            else:
                print("Invalid Answer.")
                duelmenuUI()
                return
        if duelmenuInput == "Attack Monster" or duelmenuInput == "attack monster" or duelmenuInput == "atk monster":
            if toggleDamageCalc == int(0):
                print("Damage calculations is disabled. To enable, go to options.")
                duelmenuUI()
                return
            opponentMonsterPos = ""
            globalvar.opponentMonsterATK = 0
            globalvar.opponentMonsterDEF = 0
            highestMonster = 0
            inflictDamage = 0
            inflictDamageUsingDEF = 0
            attackUsingDEF = ""
            damageFilter = 0
            print("Are you attacking using your monster's defense?")
            attackUsingDEF = input()
            if attackUsingDEF == "Yes" or attackUsingDEF == "yes":
                print("Whats your Opponent's Monsters Position?")
                opponentMonsterPos = input('--- DEF vs --- > ')
                if opponentMonsterPos == "Attack" or opponentMonsterPos == "attack" or opponentMonsterPos == "ATK" or opponentMonsterPos == "atk":
                    print("Whats your monsters defense?")
                    inflictDamageUsingDEF = input('--- DEF vs --- ATK > ')
                    if int(inflictDamageUsingDEF.isdigit()) == True:
                        print("Whats your opponent's monster attack?")
                        globalvar.opponentMonsterATK = input('' + str(inflictDamageUsingDEF) + ' DEF vs --- ATK > ')
                        if int(str(globalvar.opponentMonsterDEF).isdigit()) == True:
                            #Alright, time to find the highest Stat.
                            if int(inflictDamageUsingDEF) > int(globalvar.opponentMonsterATK) or int(inflictDamageUsingDEF) < int(globalvar.opponentMonsterATK):
                                if int(inflictDamageUsingDEF) > int(globalvar.opponentMonsterATK):
                                    highestMonster = str(inflictDamageUsingDEF)
                                    damageFilter = int(highestMonster) - int(globalvar.opponentMonsterATK)
                                    updater.updateLife(playerName.OpponentName, str(damageFilter))
                                    opponentsMonsterPos = ""
                                    inflictDamageUsingDEF = 0
                                    globalvar.opponentMonsterATK = 0
                                    if int(lifepoints.OpponentLife) == 0:
                                            lifelock = 0
                                            lifepoints.lifepointval = 0
                                            cmdUI()
                                            return
                                    else:
                                        duelmenuUI()
                                        return
                                if int(inflictDamageUsingDEF) < int(globalvar.opponentMonsterATK):
                                    highestMonster = str(globalvar.opponentMonsterATK)
                                    damageFilter = int(highestMonster) - int(globalvar.opponentMonsterATK)
                                    updater.updateLife(playerName.MainplayerName, str(damageFilter))
                                    opponentsMonsterPos = ""
                                    inflictDamageUsingDEF = 0
                                    globalvar.opponentMonsterATK = 0
                                    if int(lifepoints.OpponentLife) == 0:
                                            lifelock = 0
                                            lifepoints.lifepointval = 0
                                            cmdUI()
                                            return
                                    else:
                                        duelmenuUI()
                                        return
                        else:
                            print("Expected numerical value.")
                            duelmenuUI()
                            return
                    else:
                        print("Expected numerical value.")
                        duelmenuUI()
                        return
                if opponentMonsterPos == "Defense" or opponentMonsterPos == "defense" or opponentMonsterPos == "DEF" or opponentMonsterPos == "def":
                    print("Whats your monsters defense?")
                    inflictDamageUsingDEF = input('--- DEF vs --- DEF > ')
                    if int(str(inflictDamageUsingDEF).isdigit()) == True:
                        print("Whats your opponent's monster defense?")
                        globalvar.opponentMonsterDEF = input('' + str(inflictDamageUsingDEF) + ' DEF vs --- DEF > ')
                        if int(str(globalvar.opponentMonsterDEF).isdigit()) == True:
                            #Hold on a minute. We're attacking a defensive Position monster. Is it piercing damage?
                            global piercingDamageInput
                            print("Is it piercing damage?")
                            piercingDamageInput = input()
                            if piercingDamageInput == "Yes" or piercingDamageInput == "yes":
                                if int(inflictDamageUsingDEF) > int(globalvar.opponentMonsterDEF) or int(inflictDamageUsingDEF) < int(globalvar.opponentMonsterDEF):
                                    if int(inflictDamageUsingDEF) > int(globalvar.opponentMonsterDEF):
                                        highestMonster = str(inflictDamageUsingDEF)
                                        damageFilter = int(highestMonster) - int(globalvar.opponentMonsterDEF)
                                        updater.updateLife(playerName.OpponentName, str(damageFilter))
                                        opponentsMonsterPos = ""
                                        inflictDamageUsingDEF = 0
                                        globalvar.opponentMonsterDEF = 0
                                        if int(lifepoints.OpponentLife) == 0:
                                            lifelock = 0
                                            lifepoints.lifepointval = 0
                                            cmdUI()
                                            return
                                        else:
                                            duelmenuUI()
                                            return
                                    if int(inflictDamageUsingDEF) < int(globalvar.opponentMonsterDEF):
                                        highestMonster = str(globalvar.opponentMonsterDEF)
                                        damageFilter = int(highestMonster) - int(globalvar.opponentMonsterDEF)
                                        updater.updateLife(playerName.MainplayerName, str(damageFilter))
                                        opponentsMonsterPos = ""
                                        inflictDamageUsingDEF = 0
                                        globalvar.opponentMonsterDEF = 0
                                        if int(lifepoints.OpponentLife) == 0:
                                            lifelock = 0
                                            lifepoints.lifepointval = 0
                                            cmdUI()
                                            return
                                        else:
                                            duelmenuUI()
                                            return
                                else:
                                    print("Expected numerical value.")
                                    duelmenuUI()
                                    return
                            if piercingDamageInput == "No" or piercingDamageInput == "no":
                                if inflictDamageUsingDEF > opponentMonsterDEF:
                                    print("Your opponent's Monster is destroyed.")
                                    duelmenuUI()
                                    return
                                if inflictDamageUsingDEF < opponentMonsterDEF:
                                    print("Your monster is destroyed.")
                                    duelmenuUI()
                                    return
                        else:
                            print("Expected numerical value.")
                            duelmenuUI()
                            return
                    else:
                        print("Invalid Monster Position.")
                        duelmenuUI()
                        return
            if attackUsingDEF == "No" or attackUsingDEF == "no":
                print("Whats your Opponent's Monsters Position?")
                opponentMonsterPos = input('--- ATK vs --- > ')
                if opponentMonsterPos == "Attack" or opponentMonsterPos == "attack" or opponentMonsterPos == "ATK" or opponentMonsterPos == "atk":
                    print("Whats your monsters attack?")
                    inflictDamageUsingATK = input('--- ATK vs --- ATK > ')
                    if int(inflictDamageUsingATK.isdigit()) == True:
                        print("Whats your opponent's monster attack?")
                        globalvar.opponentMonsterATK = input('' + str(inflictDamageUsingATK) + ' ATK vs --- ATK > ')
                        if int(str(globalvar.opponentMonsterATK).isdigit()) == True:
                            #Alright, time to find the highest Stat.
                            if int(inflictDamageUsingATK) > int(globalvar.opponentMonsterATK) or int(inflictDamageUsingATK) < int(globalvar.opponentMonsterATK):
                                if int(inflictDamageUsingATK) > int(globalvar.opponentMonsterATK):
                                    highestMonster = str(inflictDamageUsingATK)
                                    damageFilter = int(highestMonster) - int(globalvar.opponentMonsterATK)
                                    updater.updateLife(playerName.OpponentName, str(damageFilter))
                                    globalvar.opponentsMonsterPos = ""
                                    inflictDamageUsingATK = 0
                                    globalvar.opponentMonsterATK = 0
                                    if int(lifepoints.OpponentLife) == 0:
                                        lifelock = 0
                                        lifepoints.lifepointval = 0
                                        cmdUI()
                                        return
                                    else:
                                        duelmenuUI()
                                        return
                                if int(inflictDamageUsingATK) < int(globalvar.opponentMonsterATK):
                                    highestMonster = str(globalvar.opponentMonsterATK)
                                    damageFilter = int(highestMonster) - int(inflictDamageUsingATK)
                                    updater.updateLife(playerName.MainplayerName, str(damageFilter))
                                    globalvar.opponentsMonsterPos = ""
                                    inflictDamageUsingATK = 0
                                    globalvar.opponentMonsterATK = 0
                                    if int(lifepoints.OpponentLife) == 0:
                                        lifelock = 0
                                        lifepoints.lifepointval = 0
                                        cmdUI()
                                        return
                                    else:
                                        duelmenuUI()
                                        return
                        else:
                            print("Expected numerical value.")
                            duelmenuUI()
                            return
                    else:
                        print("Expected numerical value.")
                        duelmenuUI()
                        return
                if opponentMonsterPos == "Defense" or opponentMonsterPos == "defense" or opponentMonsterPos == "DEF" or opponentMonsterPos == "def":
                    print("Whats your monsters attack?")
                    inflictDamageUsingATK = input('--- ATK vs --- DEF > ')
                    if int(str(inflictDamageUsingATK).isdigit()) == True:
                        print("Whats your opponent's monster defense?")
                        globalvar.opponentMonsterDEF = input('' + str(inflictDamageUsingATK) + ' ATK vs --- DEF > ')
                        if int(str(globalvar.opponentMonsterDEF).isdigit()) == True:
                            #Hold on a minute. We're attacking a defensive Position monster. Is it piercing damage?
                            print("Is it piercing damage?")
                            piercingDamageInput = input()
                            if piercingDamageInput == "Yes" or piercingDamageInput == "yes":
                                if int(inflictDamageUsingATK) > int(globalvar.opponentMonsterDEF) or int(inflictDamageUsingATK) < int(globalvar.opponentMonsterDEF):
                                    if int(inflictDamageUsingATK) > int(globalvar.opponentMonsterDEF):
                                        highestMonster = str(inflictDamageUsingATK)
                                        damageFilter = int(highestMonster) - int(globalvar.opponentMonsterDEF)
                                        updater.updateLife(playerName.OpponentName, str(damageFilter))
                                        opponentsMonsterPos = ""
                                        inflictDamageUsingDEF = 0
                                        globalvar.opponentMonsterDEF = 0
                                        if int(lifepoints.OpponentLife) == 0:
                                            lifelock = 0
                                            lifepoints.lifepointval = 0
                                            cmdUI()
                                            return
                                        else:
                                            duelmenuUI()
                                            return
                                    if int(inflictDamageUsingATK) < int(globalvar.opponentMonsterDEF):
                                        highestMonster = str(globalvar.opponentMonsterDEF)
                                        damageFilter = int(highestMonster) - int(globalvar.opponentMonsterDEF)
                                        updater.updateLife(playerName.MainplayerName, str(damageFilter))
                                        opponentsMonsterPos = ""
                                        inflictDamageUsingATK = 0
                                        globalvar.opponentMonsterDEF = 0
                                        if int(lifepoints.OpponentLife) == 0:
                                            lifelock = 0
                                            lifepoints.lifepointval = 0
                                            cmdUI()
                                            return
                                        else:
                                            duelmenuUI()
                                            return
                    
                                else:
                                    print("Expected numerical value.")
                                    duelmenuUI()
                                    return
                            if piercingDamageInput == "No" or piercingDamageInput == "no":
                                if int(inflictDamageUsingDEF) < int(globalvar.opponentMonsterDEF):
                                    print("Your opponent's Monster is destroyed.")
                                    duelmenuUI()
                                    return
                                if int(inflictDamageUsingDEF) > int(globalvar.opponentMonsterDEF):
                                    print("Your monster is destroyed.")
                                    duelmenuUI()
                                    return
                        else:
                            print("Expected numerical value.")
                            duelmenuUI()
                            return
                    else:
                        print("Invalid Monster Position.")
                        duelmenuUI()
                        return
            else:
                print("Invalid Choice.")
                duelmenuUI()
                return
        if duelmenuInput == "Damage Lifepoints" or duelmenuInput == "damage lifepoints" or duelmenuInput == "damage life" or duelmenuInput == "Damage Life":
            if toggleDamageCalc == int(1):
                print("Damage calculations is enabled. To use this command, go to options, and disable it.")
                duelmenuUI()
                return
            else:
                print("How much damage is being inflicted?")
                inflictDamage = input()
                if int(inflictDamage.isdigit()) == True:
                    updater.updateLife(playerName.OpponentName, inflictDamage)
                    duelmenuUI()
                    return
                else:
                    print("Invalid input. Expected a numerical value.")
                    duelmenuUI()
                    return
        if duelmenuInput == "Options" or duelmenuInput == "options":
            optionsUI()
            return
        if duelmenuInput == "Monster Stat Calculator" or duelmenuInput == "monster stat calculator":
            monsterStatUI()
            return
        if duelmenuInput == "End Turn" or duelmenuInput == "end turn":
            endTurn()
            duelmenuUI()
            return
        if duelmenuInput == "Quit Duel" or duelmenuInput == "quit duel" or duelmenuInput == "quit" or duelmenuInput == "exit":
            exit()
            return
        if duelmenuInput == "":
            print("You didn't type anything in.")
            duelmenuUI()
            return
        else:
            print("Invalid command. Please re-enter the command.")
            duelmenuUI()
            return
    if ChallengeTurn == 2:
        print(" ")
        print("+===================+")
        print("|     Duel Menu     |")
        print("+===================+")
        print(" ")
        print("+------------+")
        print("| Lifepoints |")
        print("+------------+")
        print(" ")
        print(str(playerName.MainplayerName) + " : " + str(lifepoints.MainplayerLife))
        print("> " + str(playerName.OpponentName) + " < : " + str(lifepoints.OpponentLife))
        print(" ")
        print("+----------+")
        print("| Commands |")
        print("+----------+")
        print(" ")
        print("Gain Life - Increases lifepoints by x amount")
        print("Pay Life - Pays x amount of lifepoints")
        if toggleDamageCalc == int(1):
            print("Attack Directly - Attack your opponent directly")
            print("Attack Monster - Attack your opponent's monster")
        else:
            print("Damage Lifepoints - Inflicts damage your Opponent's lifepoints by x amount")
        print("Options - Navigates to the Options")
        print("Monster Stat Calculator - Opens the monster stat calculator")
        print("End Turn - Ends your turn")
        print("Quit Duel - Quits the duel by exiting the module")
        print(" ")
        print("Please enter a command.")
        duelmenuInput = input('Lifepoint Tracker> Duel Menu> ')
        if duelmenuInput == "Gain Life" or duelmenuInput == "gain life":
            print("How much did you gain?")
            gainInput = input()
            if int(gainInput.isdigit()) == False:
                print("Expected a number.")
                duelmenuUI()
                return
            else:
                updater.gainLife(playerName.OpponentName, gainInput)
                duelmenuUI()
                gainInput = 0
                return
        if duelmenuInput == "Pay Life" or duelmenuInput == "pay life":
            print("How much is being paid?")
            payAmount = input()
            if int(payAmount.isdigit()) == True:
                updater.updateLife(playerName.OpponentName, payAmount)
                print("Amount paid.")
                if int(lifepoints.OpponentLife) == 0:
                    lifelock = 0
                    lifepoints.lifepointval = 0
                    cmdUI()
                    return
                else:
                    duelmenuUI()
                    return
        if duelmenuInput == "Attack Directly" or duelmenuInput == "attack directly" or duelmenuInput == "atk directly":
            if toggleDamageCalc == int(0):
                print("Damage Calculations are disabled. To enable, go to options.")
                duelmenuUI()
                return
            print("Are you attacking using your monster's Defense?")
            attackUsingDEF = input()
            if attackUsingDEF == "Yes" or attackUsingDEF == "yes":
                print("What's your monsters defense?")
                inflictDamageUsingDEF = input()
                if int(inflictDamageUsingDEF.isdigit()) == True:
                    updater.updateLife(playerName.MainplayerName, inflictDamageUsingDEF)
                    if int(lifepoints.MainplayerLife) == 0:
                        lifelock = 0
                        lifepoints.lifepointval = 0
                        cmdUI()
                        return
                    else:
                        duelmenuUI()
                        return
                else:
                    print("Expected a numerical value.")
                    duelmenuUI()
                    return
            if attackUsingDEF == "No" or attackUsingDEF == "no":
                print("What's your monster's attack?")
                inflictDamage = input()
                if int(inflictDamage.isdigit()) == True:
                    updater.updateLife(str(playerName.MainplayerName), inflictDamage)
                    if int(lifepoints.MainplayerLife) == 0:
                        lifelock = 0
                        lifepoints.lifepointval = 0
                        cmdUI()
                        return
                    else:
                        duelmenuUI()
                        return
                else:
                    print("Expected a numerical value.")
                    duelmenuUI()
                    return
            else:
                print("Invalid Answer.")
                duelmenuUI()
                return
        if duelmenuInput == "Attack Monster" or duelmenuInput == "attack monster":
            if toggleDamageCalc == int(0):
                print("Damage calculations are disabled. To enable, go to options.")
                duelmenuUI()
                return
            global MainplayerMonsterATK
            global MainplayerMonsterDEF
            MainplayerMonsterPos = ""
            MainplayerMonsterATK = 0
            MainplayerMonsterDEF = 0
            highestMonster = 0
            inflictDamage = 0
            inflictDamageUsingDEF = 0
            attackUsingDEF = ""
            damageFilter = 0
            print("Are you attacking using your monster's defense?")
            attackUsingDEF = input()
            if attackUsingDEF == "Yes" or attackUsingDEF == "yes":
                print("Whats your Opponent's Monsters Position?")
                MainplayerMonsterPos = input('--- DEF vs --- > ')
                if MainplayerMonsterPos == "Attack" or MainplayerMonsterPos == "attack" or MainplayerMonsterPos == "ATK" or MainplayerMonsterPos == "atk":
                    print("Whats your monsters defense?")
                    inflictDamageUsingDEF = input('--- DEF vs --- ATK > ')
                    if int(inflictDamageUsingDEF.isdigit()) == True:
                        print("Whats your opponent's monster attack?")
                        globalvar.MainplayerMonsterATK = input('' + str(inflictDamageUsingDEF) + ' DEF vs --- ATK > ')
                        if int(str(globalvar.MainplayerMonsterATK).isdigit()) == True:
                            #Alright, time to find the highest Stat.
                            if int(inflictDamageUsingDEF) > int(globalvar.MainplayerMonsterATK) or int(inflictDamageUsingDEF) < int(globalvar.MainplayerMonsterATK):
                                if int(inflictDamageUsingDEF) > int(globalvar.opponentMonsterATK):
                                    highestMonster = str(inflictDamageUsingDEF)
                                    damageFilter = int(highestMonster) - int(globalvar.MainplayerMonsterATK)
                                    updater.updateLife(playerName.MainplayerName, str(damageFilter))
                                    MainplayerMonsterPos = ""
                                    inflictDamageUsingDEF = 0
                                    globalvar.MainplayerMonsterATK = 0
                                    if int(lifepoints.MainplayerLife) == 0:
                                        lifelock = 0
                                        lifepoints.lifepointval = 0
                                        cmdUI()
                                        return
                                    else:
                                        duelmenuUI()
                                        return
                                if int(inflictDamageUsingDEF) < int(globalvar.MainplayerMonsterATK):
                                    highestMonster = str(globalvar.MainplayerMonsterATK)
                                    damageFilter = int(highestMonster) - int(globalvar.MainplayerMonsterATK)
                                    updater.updateLife(playerName.OpponentName, str(damageFilter))
                                    MainplayerMonsterPos = ""
                                    inflictDamageUsingDEF = 0
                                    globalvar.MainplayerMonsterATK = 0
                                    if int(lifepoints.MainplayerLife) == 0:
                                        lifelock = 0
                                        lifepoints.lifepointval = 0
                                        cmdUI()
                                        return
                                    else:
                                        duelmenuUI()
                                        return
                        else:
                            print("Expected numerical value.")
                            duelmenuUI()
                            return
                    else:
                        print("Expected numerical value.")
                        duelmenuUI()
                        return
                if MainplayerMonsterPos == "Defense" or MainplayerMonsterPos == "defense" or MainplayerMonsterPos == "DEF" or MainplayerMonsterPos == "def":
                    print("Whats your monsters defense?")
                    inflictDamageUsingDEF = input('--- DEF vs --- DEF > ')
                    if int(str(inflictDamageUsingDEF).isdigit()) == True:
                        print("Whats your opponent's monster defense?")
                        globalvar.MainplayerMonsterDEF = input('' + str(inflictDamageUsingDEF) + ' DEF vs --- DEF > ')
                        if int(str(globalvar.MainplayerMonsterDEF).isdigit()) == True:
                            #Hold on a minute. We're attacking a defensive Position monster. Is it piercing damage?
                            print("Is it piercing damage?")
                            piercingDamageInput = input()
                            if piercingDamageInput == "Yes" or piercingDamageInput == "yes":
                                if int(inflictDamageUsingDEF) > int(globalvar.MainplayerMonsterDEF) or int(inflictDamageUsingDEF) < int(globalvar.MainplayerMonsterDEF):
                                    if int(inflictDamageUsingDEF) > int(globalvar.MainplayerMonsterDEF):
                                        highestMonster = str(inflictDamageUsingDEF)
                                        damageFilter = int(highestMonster) - int(globalvar.MainplayerMonsterDEF)
                                        updater.updateLife(playerName.MainplayerName, str(damageFilter))
                                        MainplayerMonsterPos = ""
                                        inflictDamageUsingDEF = 0
                                        globalvar.MainplayerMonsterDEF = 0
                                        if int(lifepoints.MainplayerLife) == 0:
                                            lifelock = 0
                                            lifepoints.lifepointval = 0
                                            cmdUI()
                                            return
                                        else:
                                            duelmenuUI()
                                            return
                                    if int(inflictDamageUsingDEF) < int(globalvar.MainplayerMonsterDEF):
                                        highestMonster = str(globalvar.MainplayerMonsterDEF)
                                        damageFilter = int(highestMonster) - int(globalvar.MainplayerMonsterDEF)
                                        updater.updateLife(playerName.OpponentName, str(damageFilter))
                                        MainplayerMonsterPos = ""
                                        inflictDamageUsingDEF = 0
                                        globalvar.MainplayerMonsterDEF = 0
                                        if int(lifepoints.MainplayerLife) == 0:
                                            lifelock = 0
                                            lifepoints.lifepointval = 0
                                            cmdUI()
                                            return
                                        else:
                                            duelmenuUI()
                                            return
                                else:
                                    print("Expected numerical value.")
                                    duelmenuUI()
                                    return
                            if piercingDamageInput == "No" or piercingDamageInput == "no":
                                if int(inflictDamageUsingDEF) > int(globalvar.MainplayerMonsterDEF):
                                    print("Your opponent's Monster is destroyed.")
                                    duelmenuUI()
                                    return
                                if int(inflictDamageUsingDEF) < int(globalvar.MainplayerMonsterDEF):
                                    print("Your monster is destroyed.")
                                    duelmenuUI()
                                    return
                        else:
                            print("Expected numerical value.")
                            duelmenuUI()
                            return
                    else:
                        print("Invalid Monster Position.")
                        duelmenuUI()
                        return
            if attackUsingDEF == "No" or attackUsingDEF == "no":
                print("Whats your Opponent's Monsters Position?")
                MainplayerMonsterPos = input('--- ATK vs --- > ')
                if MainplayerMonsterPos == "Attack" or MainplayerMonsterPos == "attack" or MainplayerMonsterPos == "ATK" or MainplayerMonsterPos == "atk":
                    print("Whats your monsters attack?")
                    inflictDamageUsingATK = input('--- ATK vs --- ATK > ')
                    if int(inflictDamageUsingATK.isdigit()) == True:
                        print("Whats your opponent's monster attack?")
                        globalvar.MainplayerMonsterATK = input('' + str(inflictDamageUsingATK) + ' ATK vs --- ATK > ')
                        if int(str(globalvar.MainplayerMonsterATK).isdigit()) == True:
                            #Alright, time to find the highest Stat.
                            if int(inflictDamageUsingATK) > int(globalvar.MainplayerMonsterATK) or int(inflictDamageUsingATK) < int(globalvar.MainplayerMonsterATK):
                                if int(inflictDamageUsingATK) > int(globalvar.MainplayerMonsterATK):
                                    highestMonster = str(inflictDamageUsingATK)
                                    damageFilter = int(highestMonster) - int(globalvar.MainplayerMonsterATK)
                                    updater.updateLife(playerName.MainplayerName, str(damageFilter))
                                    MainplayerMonsterPos = ""
                                    inflictDamageUsingATK = 0
                                    globalvar.MainplayerMonsterATK = 0
                                    if int(lifepoints.MainplayerLife) == 0:
                                        lifelock = 0
                                        lifepoints.lifepointval = 0
                                        cmdUI()
                                        return
                                    else:
                                        duelmenuUI()
                                        return
                                if int(inflictDamageUsingATK) < int(globalvar.MainplayerMonsterATK):
                                    highestMonster = str(globalvar.MainplayerMonsterATK)
                                    damageFilter = int(highestMonster) - int(globalvar.MainplayerMonsterATK)
                                    updater.updateLife(playerName.OpponentName, str(damageFilter))
                                    MainplayerMonsterPos = ""
                                    inflictDamageUsingATK = 0
                                    globalvar.MainplayerMonsterATK = 0
                                    if int(lifepoints.MainplayerLife) == 0:
                                        lifelock = 0
                                        lifepoints.lifepointval = 0
                                        cmdUI()
                                        return
                                    else:
                                        duelmenuUI()
                                        return
                        else:
                            print("Expected numerical value.")
                            duelmenuUI()
                            return
                    else:
                        print("Expected numerical value.")
                        duelmenuUI()
                        return
                if MainplayerMonsterPos == "Defense" or MainplayerMonsterPos == "defense" or MainplayerMonsterPos == "DEF" or MainplayerMonsterPos == "def":
                    print("Whats your monsters attack?")
                    inflictDamageUsingATK = input('--- ATK vs --- DEF > ')
                    if int(str(inflictDamageUsingATK).isdigit()) == True:
                        print("Whats your opponent's monster defense?")
                        globalvar.MainplayerMonsterDEF = input('' + str(inflictDamageUsingATK) + ' ATK vs --- DEF > ')
                        if int(str(globalvar.MainplayerMonsterDEF).isdigit()) == True:
                            #Hold on a minute. We're attacking a defensive Position monster. Is it piercing damage?
                            print("Is it piercing damage?")
                            piercingDamageInput = input()
                            if piercingDamageInput == "Yes" or piercingDamageInput == "yes":
                                if int(inflictDamageUsingATK) > int(globalvar.MainplayerMonsterDEF) or int(inflictDamageUsingATK) < int(globalvar.MainplayerMonsterDEF):
                                    if int(inflictDamageUsingATK) > int(globalvar.MainplayerMonsterDEF):
                                        highestMonster = str(inflictDamageUsingATK)
                                        damageFilter = int(highestMonster) - int(globalvar.MainplayerMonsterDEF)
                                        updater.updateLife(playerName.MainplayerName, str(damageFilter))
                                        MainplayerMonsterPos = ""
                                        inflictDamageUsingDEF = 0
                                        globalvar.MainplayerMonsterDEF = 0
                                        if int(lifepoints.MainplayerLife) == 0:
                                            lifelock = 0
                                            lifepoints.lifepointval = 0
                                            cmdUI()
                                            return
                                        else:
                                            duelmenuUI()
                                            return
                                    if int(inflictDamageUsingATK) < int(globalvar.MainplayerMonsterDEF):
                                        highestMonster = str(globalvar.MainplayerMonsterDEF)
                                        damageFilter = int(highestMonster) - int(globalvar.MainplayerMonsterDEF)
                                        updater.updateLife(playerName.OpponentName, str(damageFilter))
                                        MainplayerMonsterPos = ""
                                        inflictDamageUsingATK = 0
                                        globalvar.MainplayerMonsterDEF = 0
                                        if int(lifepoints.MainplayerLife) == 0:
                                            lifelock = 0
                                            lifepoints.lifepointval = 0
                                            cmdUI()
                                            return
                                        else:
                                            duelmenuUI()
                                            return
                    
                                else:
                                    print("Expected numerical value.")
                                    duelmenuUI()
                                    return
                            if piercingDamageInput == "No" or piercingDamageInput == "no":
                                if int(inflictDamageUsingDEF) < int(globalvar.MainplayerMonsterDEF):
                                    print("Your opponent's Monster is destroyed.")
                                    duelmenuUI()
                                    return
                                if int(inflictDamageUsingDEF) > int(globalvar.MainplayerMonsterDEF):
                                    print("Your monster is destroyed.")
                                    duelmenuUI()
                                    return
                        else:
                            print("Expected numerical value.")
                            duelmenuUI()
                            return
                    else:
                        print("Invalid Monster Position.")
                        duelmenuUI()
                        return
            else:
                print("Invalid Choice.")
                duelmenuUI()
                return
        if duelmenuInput == "Damage Lifepoints" or duelmenuInput == "damage lifepoints" or duelmenuInput == "damage life" or duelmenuInput == "Damage Life":
            if toggleDamageCalc == int(1):
                print("Damage calculations is enabled. To use this command, go to options, and disable it.")
                duelmenuUI()
                return
            else:
                print("How much damage is being inflicted?")
                inflictDamage = input()
                if int(inflictDamage.isdigit()) == True:
                    updater.updateLife(playerName.MainplayerName, inflictDamage)
                    duelmenuUI()
                    return
                else:
                    print("Invalid input. Expected a numerical value.")
                    duelmenuUI()
                    return
        if duelmenuInput == "Options" or duelmenuInput == "options":
            optionsUI()
            return
        if duelmenuInput == "Monster Stat Calculator" or duelmenuInput == "monster stat calculator":
            monsterStatUI()
            return
        if duelmenuInput == "End Turn" or duelmenuInput == "end turn":
            endTurn()
            duelmenuUI()
            return
        if duelmenuInput == "Quit Duel" or duelmenuInput == "quit duel" or duelmenuInput == "quit" or duelmenuInput == "exit":
            exit()
            return
        if duelmenuInput == "":
            print("You didn't type anything in.")
            duelmenuUI()
            return
        else:
            print("Invalid command. Please re-enter the command.")
            duelmenuUI()
            return

def cmdUI():
    global turnInput
    global ChallengeTurn
    global firstStrike
    print("Mainplayer Name: " + str(playerName.MainplayerName))
    print("Opponent Name: " + str(playerName.OpponentName))
    print("Starting Lifepoints: " + str(lifepoints.lifepointval))
    print("First Strike: " + str(firstStrike))
    print(" ")
    print("Commands")
    print("========")
    print(" ")
    print("Set Name - sets and locks name")
    print("Determine Turn - determines who goes first and locks it")
    print("Set Lifepoints - sets and locks the lifepoint counter")
    print("Duel Menu - Opens the duel menu")
    print("Please input a command.")
    print(" ")
    global cmdInput
    cmdInput = input('Lifepoint Tracker: ')
    if cmdInput == "Set Name" or cmdInput == "set name":
        global nameLock
        if nameLock == 0:
            global inputNameO
            print("What's your Opponent's Name?")
            inputNameO = input()
            if inputNameO == "":
                cmdUI()
                return
            else:
                print("Enter your name.")
                global inputNameM
                inputNameM = input()
                if inputNameM == "":
                    cmdUI()
                    return
                else:
                    playerName.DefineName("Set Name", "Opponent", inputNameO)
                    playerName.DefineName("Set Name", "Mainplayer", inputNameM)
                    nameLock = 1
                    cmdUI()
                    return
        else:
            print("You can't define names again, ya goof.")
            cmdUI()
            return
    if cmdInput == "Set Lifepoints" or cmdInput == "set lifepoints" or cmdInput == "set life" or cmdInput == "Set Life":
        global lifeInput
        global lifeLock
        if lifeLock == 0:
            print("Enter the starting lifepoints.")
            lifeInput = input()
            if int(str(lifeInput).isdigit()) == True:
                lifepoints.lifepointval = lifeInput
                lifepoints.DefineLife("Starting", lifeInput)
                lifeLock = 1
                cmdUI()
                return
            else:
                print("Expected numerical value. Returning to User Interface...")
                cmdUI()
                return
        else:
            print("Can't determine the starting lifepoints when it was already determined.")
            cmdUI()
            return
    if cmdInput == "Determine Turn" or cmdInput == "determine turn":
        if ChallengeTurn == 0:
            if nameLock == 0:
                print("We can't determine the turn if we don't know you and your opponent's name.")
                cmdUI()
                return
            if nameLock == 1:
                print("Who's attacking first?")
                turnInput = input()
                if turnInput == playerName.OpponentName or turnInput == playerName.MainplayerName:
                    if turnInput == playerName.OpponentName:
                        firstStrike = playerName.OpponentName
                        ChallengeTurn = 1
                        cmdUI()
                        return
                    if turnInput == playerName.MainplayerName:
                        firstStrike = playerName.MainplayerName
                        ChallengeTurn = 2
                        cmdUI()
                        return
                else:
                    print("Expected Player Name. Returning to User Interface...")
                    cmdUI()
                    return
            else:
                print("We can't determine who goes first when it's already determined.")
                cmdUI()
                return
    if cmdInput == "Duel Menu" or cmdInput == "duel menu":
        if nameLock == 1 and lifeLock == 1 and ChallengeTurn == 1 or ChallengeTurn == 2:
            print("Requirements met. Proceeding to Duel Menu.")
            duelmenuUI()
            return
    if cmdInput == "":
        print("You didn't type anything in.")
        cmdUI()
        return
    else:
        print("Invalid Command.")
        cmdUI()
        return

cmdUI()
