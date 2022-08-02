from varextract import *
import os,sys
sys.path.append('')
for x in range(0,len(questions)):
    print("")
    print(questions[x]);
    for y in range(0,len(answers[x])):
        print(anwserblock[y] + answers[x][y]);
    tinp = input("Your answer: ")
    if tinp == "1" or tinp.lower() == "a":
        response[x] = "a"
    elif tinp == "2" or tinp.lower() == "b":
        response[x] = "b"
    elif tinp == "3" or tinp.lower() == "c":
        response[x] = "c"
    elif tinp == "4" or tinp.lower() == "d":
        response[x] = "d"
    else:
        response[x] = tinp
for x in range (0,len(questions)):
    if response[x] == correctanwsers[x]:
        print("Vraag " + str(x+1) + ": " + "Goed!")
    else:
        print("Vraag " + str(x+1) + ": " + "Helaas fout, het goede antwoord was: " + correctanwsers[x] + ", uw antwoord was: " + response[x])

print('Do you want to restart this quiz?, type y or yes, if not use any other key')
ekb = input()

if ekb.lower() == "y" or ekb.lower() == "yes":
    print('starting new process...')
    os.system('python main.py')
else :
    print('closing quiz...')