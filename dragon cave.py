import random
import time



def displayIntro():
    print('''You are in a land full of Dragons. In front of you, you see two caves.
     In, one cave, the dragon is friendly and will share his tresure with you.
     The other dragon is greedy and hungry and will eat you on sight. ''')
    print()


def chooseCave():
    cave = ''
    while cave != '1' and cave != '2':
        print ('Which will you go into? (1 or 2)')
        cave = input()

    return cave

def checkCave(chosenCave):
    print ('You apporoach the cave ...')
    time.sleep(2)
    print ('It is dark and spooky')
    time.sleep(2)
    print('a large dragon jumps out in front of you! he opens his jaws and...')
    print()
    time.sleep(2)

    friendlyCave = random.randint(1,2)#
    if chosenCave == str(friendlyCave):
        print ('Gives you money!')
    else:
        print ('Gobbles you up')
playAgain = 'Yes'
while playAgain == 'yes' or playAgain == 'y':
    displayIntro
    caveNumber = chooseCave()
    checkCave(caveNumber)

    print( 'play again')
    playAgain = input
