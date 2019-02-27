from random import randint
import random
from time import sleep

def main():
    infraction = 1 #randint(1,6)
    rulesList = [1,4]
    rules = random.choice(rulesList) #randint(1,6)

    print("This program is designed to simulate academic and team rules violations by\nplayers in NCAA Football 14. The program will randomly determine if an\ninfraction occurred. If so, it will decide on a player who committed the\ninfraction (if the player chosen does not exist, reroll) and check whether\nthey broke team, academic, or NCAA rules and how long they are suspended for.\n")
    print("Checking on players...")
    sleep(1)
    
    if (infraction == 1 or infraction == 4):
        print("There has been an infraction. Taking action...\n")
        sleep(1)
        player(infraction, rules)
    else:
        print("There is no infraction this week.")
        
    return infraction
    return rules

def player(infraction, rules):
    playerIsOnTeam = False

    while playerIsOnTeam == False:
        playerNumber = randint(1, 99)
        playerNumberCheck = input("The player who has committed the infraction is #" + str(playerNumber) + ". Does a player with this\nnumber exist on your team? (Enter Y or N) ").upper()

        if (playerNumberCheck == 'Y'):
            sleep(1)
            print("-------------------------------------")
            playerInfraction(infraction, rules, playerNumber)
            return playerNumber
            break
        
def playerInfraction(infraction, rules, playerNumber):    
    if (rules == 1 or rules == 4):
        teamRules = randint(1,5)
        print("#" + str(playerNumber) + " has broken team rules.")
        #print("1 = 1 Game\n2 = 2 Games\n3 = 3 Games\n4 = First half\n5 = 5 games")

        if (teamRules == 1):
            print("#" + str(playerNumber) + " is suspended for 1 game.")
        elif (teamRules == 4):
            print("#" + str(playerNumber) + " is suspended for the first half of the next game.")
        else:
            print("#" + str(playerNumber) + " is suspended for " + str(teamRules) + " games.")

        return teamRules

    if (rules == 2 or rules == 5):
        print("#" + str(playerNumber) + " has broken academic rules.")
        academicsPreseason = input("Is it preseason? ").upper()

        if (academicsPreseason == 'N'):
            academicsPostseason = input("Is it postseason? ").upper()
        
        if (academicsPreseason == 'Y'):
            academicsPostseason = 'N'
            print("Ineligible for the regular season plus the conference championship (if applicable).")
            
        if (academicsPostseason == 'Y'):
            print("Ineligible for bowl game.")
            
        if (academicsPreseason == 'N' and academicsPostseason == 'N'):
            print("Player cannot be academically ineligible during this time. There is no infraction this week.")


    if (rules == 3 or rules == 6):
        ncaaRules = randint(1,7)
        print("#" + str(playerNumber) + " has broken NCAA rules.")

        if (ncaaRules == 1):
            print("#" + str(playerNumber) + " is suspended for " + str(ncaaRules) + " game.")
        else:
            print("#" + str(playerNumber) + " is suspended for " + str(ncaaRules) + " games.")
    
main()
