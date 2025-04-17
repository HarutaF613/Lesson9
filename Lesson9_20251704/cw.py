import pgzrun
import random

HEIGHT=400
WEIDTH=750
TITLE="Guess the Flag"

number_of_flags = 2
answer = 0
flags = []

#Choose the correct answer flag
#Make that as 1 of the flags that are showing
def showflag():
    #make blanc list / Like this → ["","",""]
    global number_of_flags,answer
    for i in range(number_of_flags):
        flags.append("")
    print("1 : " + flags)
    
    #Decide which flag is the answer
    answer = random.randient(0,18)

    #Put answer in the list
    answer_no = random.randient(0,number_of_flags)
    flags[answer_no] = answer

    #Put flag in to other box
    for i in range(number_of_flags):
        if i != answer_no:
            value = random.randient(0,18)
            if value == answer:
                if value == 0:
                    value = 1
                elif value == 18:
                    value = 17
                else:
                    value += 1