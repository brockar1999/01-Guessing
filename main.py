import sys, random

assert sys.version_info >= (3,7), "This script requires at least Python 3.7"

"""
OBJECTIVES:
+ Select random number in a set range
  + Indicate said range to player
+ Ask player to choose number
  + Give feedback on this number
+ Allow player to continue playing until correct number is found
+ Provide player with a report of their success.
"""

'''
Generates random number within a given range
'''
def randomGen(rangeNum):
    return random.randint(0,rangeNum)

def main():
    playAgain = "Y" #whether the player wants to play again
    print("Welcome to the number generator!")
    while (playAgain == "Y"):
        userTries = 0 #keeping track of how many attempts player uses
        genNum = -1 #number generated
        rangeNum = 0 #range of numbers to guess within
        while (genNum == -1): #ensuring that the player chooses a valid difficulty
            playerChoice = input("Choose your difficulty between [E]asy, [M]edium, and [H]ard. ").upper()
            if playerChoice == "E":
                genNum = randomGen(10)
                rangeNum = 10
            elif playerChoice == "M":
                genNum = randomGen(100)
                rangeNum = 100
            elif playerChoice == "H":
                genNum = randomGen(500)
                rangeNum = 500
            else:
                print("That's not an option!")

        userNum = int(input("Choose a number between 0 and {}: ".format(rangeNum))) #getting user input
        userTries += 1
        while (userNum != genNum): #continues until player guesses the right number
            print("~~~")
            print("Nice try! You have guessed %d times." %(userTries))
            if (userNum < genNum):
                print("Try guessing higher.")
            else:
                print("Try guessing lower.")
            userNum = int(input("Choose a number between 0 and {}: ".format(rangeNum)))
            userTries += 1

        #IF HERE: the player has guessed the correct number. so...
        print("Congratulations! You took %d tries to guess the right number." %(userTries))
        if (userTries < 10):
            print("Wow! You must be a master guesser.")
        elif (userTries > 50):
            print("I'm sure you'll do better next time.")
        
        playAgain = input("Do you want to play again? [Y]es or [N]o. ").upper()
        while (playAgain != "Y" and playAgain != "N"):
            print("That's not an option!")
            playAgain = input("Do you want to play again? [Y]es or [N]o. ").upper()

    print("Thank you for playing!")
    return 0

if __name__ == "__main__":
    main()

