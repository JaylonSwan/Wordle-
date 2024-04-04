from colorama import init as colorama_init
from colorama import Fore
from colorama import Style
from colorama import Back
import os
import random

#main game is done
#todo: add a letter list
#todo: add a win condition
#todo: add a lose condition
#todo: fix word check function with multiple words

f = open("data.txt", "r")
colorama_init()
words = f.read().split()


win = False

def RandomWord():
    num = random.randint(0, len(words))
   # print(words[num])
    return words[num]

def PrintList(list):
    for i in list:
        print(i, end=" ")
    print("")


lose = False
awnser = RandomWord()
word1 = ["-","-","-","-","-"]
word2 = ["-","-","-","-","-"]
word3 = ["-","-","-","-","-"]
word4 = ["-","-","-","-","-"]
word5 = ["-","-","-","-","-"]


letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']        

testout = "idk"

def GuessCheck():
    global win
    if not win:
        inps = input("Enter a word: ")
    if inps == awnser:
        win = True
        return inps
    while inps not in words:
        inps = input("Enter a word: ")
    return inps

def updatewords():
    os.system('cls')
    print(awnser)
    print(Fore.MAGENTA + "Welcome to wordle!" + Style.RESET_ALL)
    PrintList(word1) 
    PrintList(word2) 
    PrintList(word3) 
    PrintList(word4) 
    PrintList(word5) 
    if (win == True):
        os.system('cls')
        print(Fore.MAGENTA + "You win!" + Style.RESET_ALL)
        print(Fore.GREEN + "The word was: " + awnser + Style.RESET_ALL)
    if (lose):
        os.system('cls')
        print(Fore.RED + "You Lose!" + Style.RESET_ALL)
        print(Fore.GREEN + "The word was: " + awnser + Style.RESET_ALL)
        
    
    #PrintList(letters)

def checkword(words):
    
    for i in range(0, len(awnser)):
        words[i] = inp[i]  
    for char, word in zip(awnser, words):
        if word in awnser and word in char:
            words[words.index(word)] = Fore.GREEN + word + Style.RESET_ALL
        elif word in awnser:
            words[words.index(word)] = Fore.YELLOW + word + Style.RESET_ALL  
        
updatewords()
print("")
    


inp = GuessCheck()
checkword(word1)
updatewords()


inp = GuessCheck()
checkword(word2)
updatewords()

inp = GuessCheck()
checkword(word3)
updatewords()

inp = GuessCheck()
checkword(word4)
updatewords()

inp = GuessCheck()
checkword(word5)
updatewords()

lose = True
updatewords()

      
f.close()