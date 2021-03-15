from varextract import *
import os,sys
sys.path.append('')

print(q1)
print("A:" + q1a1)
print("B:" + q1a2)
print("C:" + q1a3)
print("D:" + q1a4)
q1a = input()

print(q2)
print("A:" + q2a1)
print("B:" + q2a2)
print("C:" + q2a3)
q2a = input()

print(q3)
print("A:" + q3a1)
print("B:" + q3a2)
print("C:" + q3a3)
print("D:" + q3a4)
q3a = input()

print(q4)
print("A:" + q4a1)
print("B:" + q4a2)
print("C:" + q4a3)
q4a = input()

print(q5)
print("A:" + q5a1)
print("B:" + q5a2)
print("C:" + q5a3)
print("D:" + q5a4)
q5a = input()

print(q6)
print("A:" + q6a1)
print("B:" + q6a2)
print("C:" + q6a3)
q6a = input()

print(q7)
print("A:" + q7a1)
print("B:" + q7a2)
print("C:" + q7a3)
print("D:" + q7a4)
q7a = input()

print(q8)
print("A:" + q8a1)
print("B:" + q8a2)
print("C:" + q8a3)
q8a = input()

print(q9)
print("A:" + q9a1)
print("B:" + q9a2)
q9a = input()

print(q10)
print("A:" + q10a1)
print("B:" + q10a2)
print("C:" + q10a3)
q10a = input()

print(q11)
print('A:' + q11a1)
print('B:' + q11a2)
print('C:' + q11a3)
print('D:' + q11a4)
q11a = input()

print(q12)
print('A:' + q12a1)
print('B:' + q12a2)
print('C:' + q12a3)
print('D:' + q12a4)
q12a = input()

print(q13)
print('A:' + q13a1)
print('B:' + q13a2)
print('C:' + q13a3)
print('D:' + q13a4)
q13a = input()

print(q14)
print('A:' + q14a1)
print('B:' + q14a2)
print('C:' + q14a3)
print('D:' + q14a4)
q14a = input()

print(q15)
print('A:' + q15a1)
print('B:' + q15a2)
print('C:' + q15a3)
print('D:' + q15a4)
q15a = input()

print(q16)
print('A:' + q16a1)
print('B:' + q16a2)
print('C:' + q16a3)
print('D:' + q16a4)
q16a = input()

print(q17)
print('A:' + q17a1)
print('B:' + q17a2)
print('C:' + q17a3)
print('D:' + q17a4)
q17a = input()

print(q18)
print('A:' + q18a1)
print('B:' + q18a2)
print('C:' + q18a3)
print('D:' + q18a4)
q18a = input()

print(q19)
print('A:' + q19a1)
print('B:' + q19a2)
print('C:' + q19a3)
print('D:' + q19a4)
q19a = input()

print(q20)
print('A:' + q20a1)
print('B:' + q20a2)
print('C:' + q20a3)
print('D:' + q20a4)
q20a = input()

print(q21)
print('A:' + q21a1)
print('B:' + q21a2)
print('C:' + q21a3)
q21a = input()

print(q22)
print('A:' + q22a1)
print('B:' + q22a2)
print('C:' + q22a3)
q22a = input()

print(q23)
print('A:' + q23a1)
print('B:' + q23a2)
print('C:' + q23a3)
print('D:' + q23a4)
q23a = input()

print(q24)
print('A:' + q24a1)
print('B:' + q24a2)
print('C:' + q24a3)
q24a = input()

print(q25)
print('A:' + q25a1)
print('B:' + q25a2)
print('C:' + q25a3)
print('D:' + q25a4)
q25a = input()

if q1a == 'A' or q1a == 'a' :
    q1h = 'dit antwoord (antwoord a) is helaas fout  het goede antwoord was antwoord b'
elif q1a == 'B' or q1a == 'b':
    q1h = 'dit antwoord is goed (antwoord b)'
elif q1a == 'C' or q1a == 'c':
    q1h = 'Dit antwoord (antwoord c) is helaas fout het goede antwoord was antwoord b'
    brac = brac + 1
elif q1a == 'D' or q1a == 'd':
    q1h = 'dit antwoord (antwoord d) is helaas fout  het goede antwoord was antwoord b'
else :
    q1h = 'Error could not handle anwser [error 2]'
    

if q2a == 'A' or q2a == 'a' :
    q2h = 'dit antwoord is goed (antwoord a)'
    brac = brac + 1
elif q2a == 'B' or q2a == 'b':
    q2h = 'dit antwoord (antwoord b) is helaas fout  het goede antwoord was antwoord a'
elif q2a == 'C' or q2a == 'c':
    q2h = 'dit antwoord (antwoord c) is helaas fout  het goede antwoord was antwoord a'
else :
    q2h = 'Error could not handle anwser [error 2]'
    
if q3a == 'A' or q3a == 'a' :
    q3h = 'dit antwoord is goed (antwoord a)'
elif q3a == 'B' or q3a == 'b':
    q3h = 'dit antwoord (antwoord b) is helaas fout  het goede antwoord was antwoord a'
    brac = brac + 1
elif q3a == 'C' or q3a == 'c':
    q3h = 'dit antwoord (antwoord c) is helaas fout  het goede antwoord was antwoord a'
elif q3a == 'D' or q3a == 'd':
    q3h = 'dit antwoord (antwoord d) is helaas fout  het goede antwoord was antwoord a'
else :
    q3h = 'Error could not handle anwser [error 2]'
    
if q4a == 'A' or q4a == 'a' :
    q4h = 'dit antwoord is goed (antwoord a)'
    brac = brac + 1
elif q4a == 'B' or q4a == 'b':
    q4h = 'dit antwoord (antwoord b) is helaas fout  het goede antwoord was antwoord a'
elif q4a == 'C' or q4a == 'c':
    q4h = 'dit antwoord (antwoord c) is helaas fout  het goede antwoord was antwoord a'
else :
    q4h = 'Error could not handle anwser [error 2]'
    
if q5a == 'A' or q5a == 'a' :
    q5h = 'dit antwoord (antwoord a) is helaas fout  het goede antwoord was antwoord c'
elif q5a == 'B' or q5a == 'b':
    q5h = 'dit antwoord (antwoord b) is helaas fout  het goede antwoord was antwoord c'
elif q5a == 'C' or q5a == 'c':
    q5h = 'dit antwoord is goed (antwoord c)'
    brac = brac + 1
elif q5a == 'D' or q5a == 'd':
    q5h = 'dit antwoord (antwoord d) is helaas fout  het goede antwoord was antwoord c'
else :
    q5h = 'Error could not handle anwser [error 2]'

if q6a == 'A' or q6a == 'a' :
    q6h = 'dit antwoord (antwoord a) is helaas fout  het goede antwoord was antwoord b'
elif q6a == 'B' or q6a == 'b':
    q6h = 'dit antwoord is goed (antwoord b)'
    brac = brac + 1
elif q6a == 'C' or q6a == 'c':
    q6h = 'dit antwoord (antwoord c) is helaas fout  het goede antwoord was antwoord b'
else :
    q6h = 'Error could not handle anwser [error 2]'
    
if q7a == 'A' or q7a == 'a' :
    q7h = 'dit antwoord (antwoord a) is helaas fout  het goede antwoord was antwoord d'
elif q7a == 'B' or q7a == 'b':
    q7h = 'dit antwoord (antwoord b) is helaas fout  het goede antwoord was antwoord d'
elif q7a == 'C' or q7a == 'c':
    q7h = 'dit antwoord (antwoord c) is helaas fout  het goede antwoord was antwoord d'
elif q7a == 'D' or q7a == 'd':
    q7h = 'Dit antwoord is goed (antwoord d)'
    brac = brac + 1
else :
    q7h = 'Error could not handle anwser [error 2]'
    
if q8a == 'A' or q8a == 'a' :
    q8h = 'dit antwoord is goed (antwoord a)'
    brac = brac + 1
elif q8a == 'B' or q8a == 'b':
    q8h = 'dit antwoord (antwoord b) is helaas fout  het goede antwoord was antwoord a'
elif q8a == 'C' or q8a == 'c':
    q8h = 'dit antwoord (antwoord c) is helaas fout  het goede antwoord was antwoord a'
else :
    q8h = 'Error could not handle anwser [error 2]'
    
if q9a == 'A' or q9a == 'a' :
    q9h = 'dit antwoord is goed (antwoord a)'
    brac = brac + 1
elif q9a == 'B' or q9a == 'b':
    q9h = 'dit antwoord (antwoord b) is helaas fout  het goede antwoord was antwoord a'
else :
    q9h = 'Error could not handle anwser [error 2]'
    
if q10a == 'A' or q10a == 'a' :
    q10h = 'dit antwoord is goed (antwoord a)'
    brac = brac + 1
elif q10a == 'B' or q10a == 'b':
    q10h = 'dit antwoord (antwoord b) is helaas fout  het goede antwoord was antwoord a'
elif q10a == 'C' or q10a == 'c':
    q10h = 'dit antwoord (antwoord c) is helaas fout  het goede antwoord was antwoord a'
else :
    q10h = 'Error could not handle anwser [error 2]'
    
if q11a == 'A' or q11a == 'a' :
    q11h = 'dit antwoord (antwoord a) is helaas fout  het goede antwoord was antwoord b'
    brac = brac + 1
elif q11a == 'B' or q11a == 'b':
    q11h = 'dit antwoord is goed (antwoord b)'
elif q11a == 'C' or q11a == 'c':
    q11h = 'dit antwoord (antwoord c) is helaas fout  het goede antwoord was antwoord b'
elif q11a == 'D' or q11a == 'd':
    q11h = 'dit antwoord (antwoord d) is helaas fout  het goede antwoord was antwoord b'
else :
    q11h = 'Error could not handle anwser [error 2]'
    
if q12a == 'A' or q12a == 'a' :
    q12h = 'dit antwoord (antwoord a) is helaas fout  het goede antwoord was antwoord d'
    brac = brac + 1
elif q12a == 'B' or q12a == 'b':
    q12h = 'dit antwoord (antwoord b) is helaas fout  het goede antwoord was antwoord d'
elif q12a == 'C' or q12a == 'c':
    q12h = 'dit antwoord (antwoord c) is helaas fout  het goede antwoord was antwoord d'
elif q12a == 'D' or q12a == 'd':
    q12h = 'dit antwoord is goed (antwoord d)'
else :
    q12h = 'Error could not handle anwser [error 2]'
    
if q13a == 'A' or q13a == 'a' :
    q13h = 'dit antwoord (antwoord a) is helaas fout  het goede antwoord was antwoord b'
    brac = brac + 1
elif q13a == 'B' or q13a == 'b':
    q13h = 'dit antwoord is goed (antwoord b)'
elif q13a == 'C' or q13a == 'c':
    q13h = 'dit antwoord (antwoord c) is helaas fout  het goede antwoord was antwoord b'
elif q13a == 'D' or q13a == 'd':
    q13h = 'dit antwoord (antwoord d) is helaas fout  het goede antwoord was antwoord b'
else :
    q13h = 'Error could not handle anwser [error 2]'
    
if q14a == 'A' or q14a == 'a' :
    q14h = 'dit antwoord (antwoord a) is helaas fout  het goede antwoord was antwoord d'
    brac = brac + 1
elif q14a == 'B' or q14a == 'b':
    q14h = 'dit antwoord (antwoord b) is helaas fout  het goede antwoord was antwoord d'
elif q14a == 'C' or q14a == 'c':
    q14h = 'dit antwoord (antwoord c) is helaas fout  het goede antwoord was antwoord d'
elif q14a == 'D' or q14a == 'd':
    q14h = 'dit antwoord is goed (antwoord d)'
else :
    q14h = 'Error could not handle anwser [error 2]'
    
if q15a == 'A' or q15a == 'a' :
    q15h = 'dit antwoord (antwoord a) is helaas fout  het goede antwoord was antwoord c'
    brac = brac + 1
elif q15a == 'B' or q15a == 'b':
    q15h = 'dit antwoord (antwoord b) is helaas fout  het goede antwoord was antwoord c'
elif q15a == 'C' or q15a == 'c':
    q15h = 'dit antwoord is goed (antwoord c)'
elif q15a == 'D' or q15a == 'd':
    q15h = 'dit antwoord (antwoord d) is helaas fout  het goede antwoord was antwoord c'
else :
    q15h = 'Error could not handle anwser [error 2]'
    
if q16a == 'A' or q16a == 'a' :
    q16h = 'dit antwoord is goed (antwoord a)'
    brac = brac + 1
elif q16a == 'B' or q16a == 'b':
    q16h = 'dit antwoord (antwoord b) is helaas fout  het goede antwoord was antwoord a'
elif q16a == 'C' or q16a == 'c':
    q16h = 'dit antwoord (antwoord c) is helaas fout  het goede antwoord was antwoord a'
elif q16a == 'D' or q16a == 'd':
    q16h = 'dit antwoord (antwoord d) is helaas fout  het goede antwoord was antwoord a'
else :
    q16h = 'Error could not handle anwser [error 2]'

if q17a == 'A' or q17a == 'a' :
    q17h = 'dit antwoord (antwoord a) is helaas fout  het goede antwoord was antwoord c'
    brac = brac + 1
elif q17a == 'B' or q17a == 'b':
    q17h = 'dit antwoord (antwoord b) is helaas fout  het goede antwoord was antwoord c'
elif q17a == 'C' or q17a == 'c':
    q17h = 'dit antwoord is goed (antwoord c)'
elif q17a == 'D' or q17a == 'd':
    q17h = 'dit antwoord (antwoord d) is helaas fout  het goede antwoord was antwoord c'
else :
    q17h = 'Error could not handle anwser [error 2]'

if q18a == 'A' or q18a == 'a' :
    q18h = 'dit antwoord (antwoord a) is helaas fout  het goede antwoord was antwoord c'
    brac = brac + 1
elif q18a == 'B' or q18a == 'b':
    q18h = 'dit antwoord (antwoord b) is helaas fout  het goede antwoord was antwoord c'
elif q18a == 'C' or q18a == 'c':
    q18h = 'dit antwoord is goed (antwoord c)'
elif q18a == 'D' or q18a == 'd':
    q18h = 'dit antwoord (antwoord d) is helaas fout  het goede antwoord was antwoord c'
else :
    q18h = 'Error could not handle anwser [error 2]'

if q19a == 'A' or q19a == 'a' :
    q19h = 'dit antwoord (antwoord a) is helaas fout  het goede antwoord was antwoord d'
    brac = brac + 1
elif q19a == 'B' or q19a == 'b':
    q19h = 'dit antwoord (antwoord b) is helaas fout  het goede antwoord was antwoord d'
elif q19a == 'C' or q19a == 'c':
    q19h = 'dit antwoord (antwoord c) is helaas fout  het goede antwoord was antwoord d'
elif q19a == 'D' or q19a == 'd':
    q19h = 'dit antwoord is goed (antwoord d)'
else :
    q19h = 'Error could not handle anwser [error 2]'

if q20a == 'A' or q20a == 'a' :
    q20h = 'dit antwoord (antwoord a) is helaas fout  het goede antwoord was antwoord b'
    brac = brac + 1
elif q20a == 'B' or q20a == 'b':
    q20h = 'dit antwoord is goed (antwoord b)'
elif q20a == 'C' or q20a == 'c':
    q20h = 'dit antwoord (antwoord c) is helaas fout  het goede antwoord was antwoord b'
elif q20a == 'D' or q20a == 'd':
    q20h = 'dit antwoord (antwoord d) is helaas fout  het goede antwoord was antwoord b'
else :
    q20h = 'Error could not handle anwser [error 2]'  
    
if q21a == 'A' or q21a == 'a' :
    q21h = 'dit antwoord (antwoord a) is helaas fout  het goede antwoord was antwoord b'
    brac = brac + 1
elif q21a == 'B' or q21a == 'b':
    q21h = 'dit antwoord is goed (antwoord b)'
elif q21a == 'C' or q21a == 'c':
    q21h = 'dit antwoord (antwoord c) is helaas fout  het goede antwoord was antwoord b'
elif q21a == 'D' or q21a == 'd':
    q21h = 'dit antwoord (antwoord d) is helaas fout  het goede antwoord was antwoord b'
else :
    q21h = 'Error could not handle anwser [error 2]'  

if q22a == 'A' or q22a == 'a' :
    q22h = 'dit antwoord (antwoord a) is helaas fout  het goede antwoord was antwoord c'
    brac = brac + 1
elif q22a == 'B' or q22a == 'b':
    q22h = 'dit antwoord (antwoord b) is helaas fout  het goede antwoord was antwoord c'
elif q22a == 'C' or q22a == 'c':
    q22h = 'dit antwoord is goed (antwoord c)'
elif q22a == 'D' or q22a == 'd':
    q22h = 'dit antwoord (antwoord d) is helaas fout  het goede antwoord was antwoord c'
else :
    q22h = 'Error could not handle anwser [error 2]'  

if q23a == 'A' or q23a == 'a' :
    q23h = 'dit antwoord (antwoord a) is helaas fout  het goede antwoord was antwoord b'
    brac = brac + 1
elif q23a == 'B' or q23a == 'b':
    q23h = 'dit antwoord is goed (antwoord b)'
elif q23a == 'C' or q23a == 'c':
    q23h = 'dit antwoord (antwoord c) is helaas fout  het goede antwoord was antwoord b'
elif q23a == 'D' or q23a == 'd':
    q23h = 'dit antwoord (antwoord d) is helaas fout  het goede antwoord was antwoord b'
else :
    q23h = 'Error could not handle anwser [error 2]'  

if q24a == 'A' or q24a == 'a' :
    q24h = 'dit antwoord (antwoord a) is helaas fout  het goede antwoord was antwoord b'
    brac = brac + 1
elif q24a == 'B' or q24a == 'b':
    q24h = 'dit antwoord is goed (antwoord b)'
elif q24a == 'C' or q24a == 'c':
    q24h = 'dit antwoord (antwoord c) is helaas fout  het goede antwoord was antwoord b'
elif q24a == 'D' or q24a == 'd':
    q24h = 'dit antwoord (antwoord d) is helaas fout  het goede antwoord was antwoord b'
else :
    q24h = 'Error could not handle anwser [error 2]'    

if q25a == 'A' or q25a == 'a' :
    q25h = 'dit antwoord (antwoord a) is helaas fout  het goede antwoord was antwoord b'
    brac = brac + 1
elif q25a == 'B' or q25a == 'b':
    q25h = 'dit antwoord is goed (antwoord b)'
elif q25a == 'C' or q25a == 'c':
    q25h = 'dit antwoord (antwoord c) is helaas fout  het goede antwoord was antwoord b'
elif q25a == 'D' or q25a == 'd':
    q25h = 'dit antwoord (antwoord d) is helaas fout  het goede antwoord was antwoord b'
else :
    q25h = 'Error could not handle anwser [error 2]'


if brac < 0:
 ec = 'Error Could not handle anwser counter, counter to low errorcode [error1.1]'
elif brac >= 26 :
 ec = 'Error could not handle anwser counter, counter to high errorcode [error1.2]'
elif brac <= 7 :
 ec = 'onvoldoende'
elif brac >= 14 and brac <= 20 :
 ec = 'voldoende'
elif brac > 20 and brac <= 25 :
 ec = 'goed'
else :
 ec = "Error EC.var Could not load correctly [error3]"


print('uitslag is:', ec)
print('goede antwoorden:', brac,'/25')

print('hieronder staan alle vragen, en wat je goed en fout hebt gemaakt')

print('Vraag 1:')
print(q1h)
print('Vraag 2:')
print(q2h)
print('Vraag 3:')
print(q3h)
print('Vraag 4:')
print(q4h)
print('Vraag 5:')
print(q5h)
print('Vraag 6:')
print(q6h)
print('Vraag 7:')
print(q7h)
print('Vraag 8:')
print(q8h)
print('Vraag 9:')
print(q9h)
print('Vraag 10:')
print(q10h)
print('Vraag 11:')
print(q11h)
print('Vraag 12:')
print(q12h)
print('Vraag 13:')
print(q13h)
print('Vraag 14:')
print(q14h)
print('Vraag 15:')
print(q15h)
print('Vraag 16:')
print(q16h)
print('Vraag 17:')
print(q17h)
print('Vraag 18:')
print(q18h)
print('Vraag 19:')
print(q19h)
print('Vraag 20:')
print(q20h)
print('Vraag 21:')
print(q21h)
print('Vraag 22:')
print(q22h)
print('Vraag 23:')
print(q23h)
print('Vraag 24:')
print(q24h)
print('Vraag 25:')
print(q25h)


print('Do you want to restart this quiz?, type y or yes, if not use any other key')
ekb = input()

if ekb == 'Y' or ekb == 'y' or ekb == 'Yes' or ekb == 'yes' or ekb == 'YES' :
    print('starting new process...')
    os.system('python main.py')
else :
    print('closing quiz...')