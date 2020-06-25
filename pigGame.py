import random as rd

humanWins = False
cpuWins = False
isGameFinished = False
humanHold = False
cpuScore = 0
cpuTempScore = 0
humanScore = 0
humanTempScore = 0
turn = 0
rolledA = 0

#ask if you want to play

ask = input('Would you like to play pigs y/n?  ')

if ask.lower() == 'n' or ask.lower() == 'y' :
    if ask.lower() == 'n':
        quit() 
else: 
    print('Oops, learn what y/n means and try again!')
    quit()    

#setup

def roll():
    global rolledA
    rolledA = rd.randint(1,6) 

def is_above_100():
    global cpuWins
    global humanWins

    if humanScore or cpuScore >= 100:
        if turn % 2 == 1:
            cpuWins = True
        else:
            humanWins = True
    else:
        humanWins = False
        cpuWins = False

def won():
    if cpuWins == True:
        print('I reached 100!')
        quit()
    elif humanWins == True:
        print('You reached 100!')
        quit()
    else:
        return
        
while True and turn < 1000:
    
    #turn one
    if turn == 0:
        roll()
        
        #1 check
        if rolledA == 1:
            print('Looks like you rolled a 1. Better luck next time')
            humanTempScore = 0
            turn+=1
            continue
        
        #immediately roll
        print('You rolled a',rolledA, '!')
        humanHold = int(input('Enter 1 to hold or 0 to continue rolling: '))
        #continue rolling
        if humanHold == 0:    
            while humanHold == 0:
                roll()
                #1 check
                if rolledA ==1:
                    print('Looks like you rolled a 1. Better luck next time')
                    humanTempScore = 0
                    turn+=1
                    continue
                print('You rolled a',rolledA,'!')
                humanTempScore += rolledA
                humanHold = int(input('Enter 1 to hold or 0 to continue rolling: '))
        #held, store temp as perm score, advance to cpu
        if humanHold == 1:
            humanTempScore = humanScore
            print('You held, smart')
            turn += 1
            continue

    #normal play
    #cpu play
    if turn % 1 == 0:
        
        roll()
        #1check
        if rolledA == 1:
            print('Looks like I rolled a',rolledA,'. Better luck next time')
            turn+=1
        
        else:
            is_above_100()
            won()
            print('I rolled a', rolledA,", Awesome!\nYour turn!")
            cpuScore += rolledA
            turn += 1

    #human play     
    if turn %2 == 0 :
        roll()
        
        #1 check
        if rolledA == 1:
            print('Looks like you rolled a 1. Better luck next time')
            humanTempScore = 0
            turn+=1
            continue
        #check if game has been won
        is_above_100()
        won()
        #immediately roll
        print('You rolled a',rolledA, '!')

        humanHold = int(input('Enter 1 to hold or 0 to continue rolling: '))
        #continue rolling
        if humanHold == 0:    
            while humanHold == 0:
                roll()
                #1 check
                if rolledA ==1:
                    print('Looks like you rolled a 1. Better luck next time')
                    humanTempScore = 0
                    turn+=1
                    continue
                print('You rolled a',rolledA,'!')
                humanTempScore += rolledA
                humanHold = int(input('Enter 1 to hold or 0 to continue rolling: '))
        #held, store temp as perm score, advance to cpu
        if humanHold == 1:
            humanTempScore = humanScore
            print('You held, smart')
            turn += 1
            continue
    else:
        #debug line
        print('Open an issue, turn conditions weren\'t met')
        quit()
print('Exited the loop, please open an issue')