from Util.IOHelper import getInput
from Hero import hero
from Items import items
from Monster import goblin
from Monster import orc
from Monster import ogre

#Welcome the user to the game and get the hero's name
print("Welcome to Hero vs Goblin!")
print("You are a hero, and you have to fight a goblin!")
print("The battle is on!")
print("What is your hero's name?")
name = input()

#Create the hero and monster
myHero = hero(name, 20, 2, items[0])
myMonster = goblin()

#Set up the promt for the first action
defaultInput = "A"
inputPrompt = "Do you wish to (A)ttack or (F)lee?"
action = getInput(defaultInput, inputPrompt)

#Loop through the battle until the hero is dead or the user chooses to flee
while myHero.isAlive() and action[0].lower() == "a":
    myHero.attack(myMonster)
    #If the monster is still alive, have it attack the hero
    if myMonster.isAlive():
        myMonster.attack(myHero)
        #Exit loop if hero is dead
        if myHero.isAlive() == False:
            break
        #Set up the promt for the next action
        defaultInput = "A"
        inputPrompt = "The monster still lives! Do you wish to (A)ttack or (F)lee?"
    #If the monster is dead, level up the hero and get a new monster
    else:
        if myHero.monstersSlain % 5 == 0:
            myHero.levelUp()
        if myHero.monstersSlain > 10 and myHero.monstersSlain < 20:
            myMonster = orc()
        elif myHero.monstersSlain > 20:
            myMonster = ogre()
        else:
            myMonster = goblin()
        #Set up the promt for the next action
        defaultInput = "A"
        inputPrompt = "Do you wish to (A)ttack another monster or (F)lee?"
    #Get the next action from the user
    action = getInput(defaultInput, inputPrompt)
    
#Print the results of the battle
if myHero.isAlive():
    if myHero.monstersSlain > 0:
        print(str(myHero) + " retired victorious from the battle after slaying " + str(myHero.monstersSlain) + " monster!")
    else:
        print(str(myHero) + " escaped before being defeated by " + str(myMonster) + "!")
else:
    print(str(myHero) + " was defeated in battle by " + str(myMonster) + " after slaying " + str(myHero.monstersSlain) + " monsters!")

print("The battle is over!")
myHero.printStats()
print("Press Enter to exit.")
input()