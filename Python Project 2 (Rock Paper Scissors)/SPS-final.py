import random,array
def vartable():
    global pdat
    
    global player1random
    global player2random
    global player3random
    global player1wins
    global player2wins
    global player3wins
    global player1name
    global player2name
    global player3name
    global player1hand 
    global player2hand
    global player3hand

def main():
    vartable()
    pdat = [[False, 0, "NULL(NIY)", -1],[False, 0, "", -1],[False, 0, "", -1]]
    playeramountfilltime = 0
    player1random = pdat[0][0]
    player2random = pdat[1][0]
    player3random = pdat[2][0]
    player1wins = pdat[0][1]
    player2wins = pdat[1][1]
    player3wins = pdat[2][1]
    player1name = pdat[0][2]
    player2name = pdat[1][2]
    player3name = pdat[2][2]
    player1hand = pdat[0][3]
    player2hand = pdat[1][3]
    player3hand = pdat[2][3]
# Vartable - End
# RandomNames - Start
    randomname = [""] * (8)

    randomname = ["STROS", "Windows", "MacOSX", "Ubuntu", "CentOS", "RHEL", "Arch Linux", "OpenSUSE"]

    # RandomNames - End
    # PlayerAmount - Start
    playeramount = 0
    while playeramount <= 1 or playeramount >= 4:
        if playeramountfilltime == 0:
            print("hoeveel spelers? (2 of 3)")
            playeramountfilltime = playeramountfilltime + 1
        else:
            print("dit aantal spelers is niet mogelijk, je kan dit spelen met 2 of 3 spelers")
            playeramountfilltime = playeramountfilltime + 1
        playeramount = int(input())

    # PlayerAmount - End
    # ChooseNames - Start
    print("Vul hier de naam voor speler 1 (voor een random naam type 'Random'")
    player1name = input()
    if player1name == "random" or player1name == "Random" or player1name == "RANDOM":
        player1random = True
        getrandomcount = int(random.random() * 8)
        player1name = randomname[getrandomcount]
        
        # changing GRC to random higher then excpected
        getrandomcount = 9001
    print("Vul hier de naam voor speler 2 (voor een random naam type 'Random'")
    player2name = input()
    if player2name == "random" or player2name == "Random" or player2name == "RANDOM":
        player2random = True
        getrandomcount = int(random.random() * 8)
        player2name = randomname[getrandomcount]
        getrandomcount = 9001
    if playeramount == 3:
        print("Vul hier de naam voor speler 3 (voor een random naam type 'Random'")
        player3name = input()
        if player3name == "random" or player3name == "Random" or player3name == "RANDOM":
            getrandomcount = int(random.random() * 8)
            player3name = randomname[getrandomcount]
            getrandomcount = 9001

    # ChooseNames - End
    # FixConflictedNames - Start
    while player1name == player2name or player1name == player3name:
        if player1random == True:
            if player2random == True or player3random == True:
                getrandomcount = int(random.random() * 8)
                player1name = randomname[getrandomcount]
                getrandomcount = 9001
            else:
                print("[LOG]: Picked-up Warning: Error_==NotRandom, no action needed")
        else:
            print("[LOG]: Picked-up Warning: Error_==NotRandom, no action needed")
    while player2name == player3name:
        if player2random == True:
            if player3random == True:
                getrandomcount = int(random.random() * 8)
                player2name = randomname[getrandomcount]
                getrandomcount = 9001
            else:
                print("[LOG]: Picked-up Warning: Error_==NotRandom, no action needed")
        else:
            print("[LOG]: Picked-up Warning: Error_==NotRandom, no action needed")

    # FixConflictedNames - End
    # ChoosingHand - Start
    # ChoosingHand - End
    # AutoSelector - Start
    if playeramount == 2:
        while player1wins < 3 and player2wins < 3:
            player1hand = int(random.random() * 2)
            player2hand = int(random.random() * 2)
            if player1hand == 0:
                if player2hand == 0:
                    print("Gelijk, beide Steen")
                else:
                    if player2hand == 1:
                        player2wins = player2wins + 1
                        print("Speler 2(", end='', flush=True)
                        print(player2name, end='', flush=True)
                        print(") heeft deze ronde gewonnen (Papier (Speler 2) > Steen (Speler1))")
                    else:
                        if player2hand == 2:
                            player1wins = player1wins + 1
                            print("Speler 1(", end='', flush=True)
                            print(player1name, end='', flush=True)
                            print(") heeft deze ronde gewonnen (Steen (Speler1) > Schaar (Speler 2))")
                        else:
                            print("Ah yes the program fucked up bigtimes, oops\n")
            else:
                if player1hand == 1:
                    if player2hand == 0:
                        player1wins = player1wins + 1
                        print("Speler 1(", end='', flush=True)
                        print(player1name, end='', flush=True)
                        print(") heeft deze ronde gewonnen (Papier (Speler 1) > Steen (Speler 2))\n")
                    else:
                        if player2hand == 1:
                            print("Gelijk, beide Papier")
                        else:
                            if player2hand == 2:
                                player2wins = player2wins + 1
                                print("Speler 2(", end='', flush=True)
                                print(player2name, end='', flush=True)
                                print(") heeft deze ronde gewonnen (Schaar (Speler 2) > Papier (Speler 1))\n")
                            else:
                                print("Ah yes the program fucked up bigtimes, oops\n")
                else:
                    if player1hand == 2:
                        if player2hand == 0:
                            player2wins = player2wins + 1
                            print("Speler 2(", end='', flush=True)
                            print(player2name, end='', flush=True)
                            print(") heeft deze ronde gewonnen (Papier (Speler 2) > Steen (Speler 1))\n")
                        else:
                            if player2hand == 1:
                                player1wins = player1wins + 1
                                print("Speler 1(", end='', flush=True)
                                print(player1name, end='', flush=True)
                                print(") heeft deze ronde gewonnen (Schaar (Speler 1) > Papier (Speler 2))\n")
                            else:
                                if player2hand == 2:
                                    print("Gelijk, beide Schaar\n")
                                else:
                                    print("Ah yes the program fucked up bigtimes, oops\n")
                    else:
                        print("Ah yes the program fucked up bigtimes, oops\n")
    if playeramount == 3:
        while player1wins < 3 and player2wins < 3 and player3wins < 3:
            if player1hand == 0:
                if player2hand == 0:
                    if player3hand == 0:
                        print("Iedereen heeft hetzelfde, iedereen heeft steen\n")
                    else:
                        if player3hand == 1:
                            print("Speler 3(", end='', flush=True)
                            print(player3name, end='', flush=True)
                            print(") heeft deze ronde gewonnen (Papier (Speler 3) > Steen (Speler 1 & 2))\n")
                            player3wins = player3wins + 1
                        else:
                            if player3hand == 2:
                                print("Speler 1 & 2(", end='', flush=True)
                                print(player1name, end='', flush=True)
                                print(" & ", end='', flush=True)
                                print(player2name, end='', flush=True)
                                print(") heeft deze ronde gewonnen (Steen (Speler 1 & 2 ) > Schaar (Speler 3)\n")
                                player1wins = player1wins + 1
                                player2wins = player2wins + 1
                else:
                    if player2hand == 1:
                        if player3hand == 0:
                            print("Speler 2(", end='', flush=True)
                            print(player2name, end='', flush=True)
                            print(") heeft deze ronde gewonnen (Papier (Speler 2) > Steen (Speler 1 & 3))\n")
                            player2wins = player2wins + 1
                        else:
                            if player3hand == 1:
                                print("Speler 2 & 3(", end='', flush=True)
                                print(player2name, end='', flush=True)
                                print(" & ", end='', flush=True)
                                print(player3name, end='', flush=True)
                                print(") heeft deze ronde gewonnen (Papier (Speler 2 & 3) > Steen (Speler 1))\n")
                                player2wins = player2wins + 1
                                player3wins = player3wins + 1
                            else:
                                if player3hand == 2:
                                    print("gelijk, alles (SPS_i1)\n")
                    else:
                        if player2hand == 2:
                            if player3hand == 0:
                                print("Speler 1 & 3(", end='', flush=True)
                                print(player1name, end='', flush=True)
                                print(" & ", end='', flush=True)
                                print(player3name, end='', flush=True)
                                print(") heeft deze ronde gewonnen (Steen (Speler 1 & 3) > Schaar (Speler 2))\n")
                                player1wins = player1wins + 1
                                player3wins = player3wins + 1
                            else:
                                if player3hand == 1:
                                    print("gelijk, alles (SPS_i1)\n")
                                else:
                                    if player3hand == 2:
                                        print("Speler 1(", end='', flush=True)
                                        print(player1name, end='', flush=True)
                                        print(") heeft deze ronde gewonnen (Steen (Speler 1) > Schaar (Speler 2 & 3))\n")
                                        player1wins = player1wins + 1
            else:
                if player1hand == 1:
                    if player2hand == 0:
                        if player3hand == 0:
                            print("Speler 1(", end='', flush=True)
                            print(player1name, end='', flush=True)
                            print(") heeft deze ronde gewonnen (Papier (Speler 1) > Steen (Speler 2 & 3))\n")
                            player1wins = player1wins + 1
                        else:
                            if player3hand == 1:
                                print("Speler 1 & 3(", end='', flush=True)
                                print(player1name, end='', flush=True)
                                print(" & ", end='', flush=True)
                                print(player3name, end='', flush=True)
                                print(") heeft deze ronde gewonnen (Papier (Speler 1 & 3) > Steen (Speler 2))\n")
                                player1wins = player1wins + 1
                                player3wins = player3wins + 1
                            else:
                                if player3hand == 2:
                                    print("gelijk, alles (SPS_i1)\n")
                    else:
                        if player2hand == 1:
                            if player3hand == 0:
                                print("Speler 1 & 2(", end='', flush=True)
                                print(player1name, end='', flush=True)
                                print(" & ", end='', flush=True)
                                print(player2name, end='', flush=True)
                                print(") heeft deze ronde gewonnen (Papier (Speler 1 & 2) > Steen (Speler 3))\n")
                                player1wins = player1wins + 1
                                player2wins = player2wins + 1
                            else:
                                if player3hand == 1:
                                    print("Iedereen heeft hetzelfde, iedereen heeft papier\n")
                                else:
                                    if player3hand == 2:
                                        print("Speler 3(", end='', flush=True)
                                        print(player3name, end='', flush=True)
                                        print(") heeft deze ronde gewonnen (Schaar (Speler 3) > Papier (Speler 1 & 2))\n")
                                        player3wins = player3wins + 1
                        else:
                            if player2hand == 2:
                                if player3hand == 0:
                                    print("gelijk, alles (SPS_i1)\n")
                                else:
                                    if player3hand == 1:
                                        print("Speler 2(", end='', flush=True)
                                        print(player2name, end='', flush=True)
                                        print(") heeft deze ronde gewonnen (Schaar (Speler 2) > Papier (Speler 1 & 3))\n")
                                        player2wins = player2wins + 1
                                    else:
                                        if player3hand == 2:
                                            print("Speler 2 & 3(", end='', flush=True)
                                            print(player2name, end='', flush=True)
                                            print(" & ", end='', flush=True)
                                            print(player3name, end='', flush=True)
                                            print(") heeft deze ronde gewonnen (Schaar (Speler 2 & 3) > Papier (Speler 1))\n")
                                            player2wins = player2wins + 1
                                            player3wins = player3wins + 1
                else:
                    if player1hand == 2:
                        if player2hand == 0:
                            if player3hand == 0:
                                print("Speler 2 & 3(", end='', flush=True)
                                print(player2name, end='', flush=True)
                                print(" & ", end='', flush=True)
                                print(player3name, end='', flush=True)
                                print(") heeft deze ronde gewonnen (Steen (Speler 2 & 3) > Schaar (Speler 1))\n")
                                player2wins = player2wins + 1
                                player3wins = player3wins + 1
                            else:
                                if player3hand == 1:
                                    print("gelijk, alles (SPS_i1)")
                                else:
                                    if player3hand == 2:
                                        print("Speler 2(", end='', flush=True)
                                        print(player2name, end='', flush=True)
                                        print(") heeft deze ronde gewonnen (Schaar (Speler 2) > Papier (Speler 1 & 3))\n")
                                        player2wins = player2wins + 1
                        else:
                            if player2hand == 1:
                                if player3hand == 0:
                                    print("gelijk, alles (SPS_i1)")
                                else:
                                    if player3hand == 1:
                                        print("Speler 1(", end='', flush=True)
                                        print(player1name, end='', flush=True)
                                        print(") heeft deze ronde gewonnen (Schaar (Speler 1) > Papier (Speler 2 & 3))\n")
                                        player1wins = player1wins + 1
                                    else:
                                        if player3hand == 2:
                                            print(player1name, end='', flush=True)
                                            print(" & ", end='', flush=True)
                                            print(player3name, end='', flush=True)
                                            print(") heeft deze ronde gewonnen (Schaar (Speler 1 & 3) > Papier (Speler 2))\n")
                                            player1wins = player1wins + 1
                                            player3wins = player3wins + 1
                            else:
                                if player2hand == 2:
                                    if player3hand == 0:
                                        print("Speler 3(", end='', flush=True)
                                        print(player3name, end='', flush=True)
                                        print(") heeft deze ronde gewonnen (Steen (Speler 3) > Schaar (Speler 1 & 2))\n")
                                        player3wins = player3wins + 1
                                    else:
                                        if player3hand == 1:
                                            print("Speler 1 & 2(", end='', flush=True)
                                            print(player1name, end='', flush=True)
                                            print(" & ", end='', flush=True)
                                            print(player2name, end='', flush=True)
                                            print(") heeft deze ronde gewonnen (Schaar (Speler 1 & 2) > Papier (Speler 3))\n")
                                            player1wins = player1wins + 1
                                            player2wins = player2wins + 1
                                        else:
                                            if player3hand == 2:
                                                print("Iedereen heeft hetzelfde, iedereen heeft schaar\n")
    if player1wins >= 3:
        print("Player 1 wins")
    if player2wins >= 3:
        print("Player 2 wins")
    if player3wins >= 3:
        print("Player 3 wins")

random.seed()   #Prepare random number generator
main()
# 0 = Steen, 1 = Papier,2 = Schaar
# debug sequence 1 - Start
#print("Start?, click [ENTER]")
#debug = input()

# debug sequence 1 - End
# Vartable - Start


