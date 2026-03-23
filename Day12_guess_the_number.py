# Let's start by defining the game without difficulty and number of attempts
# Simple guess the number

from random import randint

# I define the function I'll play with!
def game(my_num, trials):
    """
    Counts the number of turns and evaluates if the number is greater, smaller or equal to the random number
    """
    given = randint(1,100)
    while True:
        while trials > 1:
            if my_num > given:
                print("Too high!")
                trials -= 1
                my_num = int(input(f"You have {trials} attempts remaining. Make a guess: "))
            elif my_num < given:
                print("Too low!")
                trials -= 1
                my_num = int(input(f"You have {trials} attempts remaining. Make a guess: "))
            elif my_num == given:
                print(f"You guessed it, the number is: {given}")
                break
        if trials == 1:    
            print("You have no more attempts. Reload the script to play: ")
        else: 
            print("Reload the script to play again.")
        break      
        

# Start of the game:
print("""
    _________          _______  _______    _______  _______  _______  _______ _________         _________ _        _______   
    \__   __/|\     /|(  ____ )(  ____ \  (  ____ \(  ___  )(       )(  ____ \\__   __/|\     /|\__   __/( (    /|(  ____ \  
       ) (   ( \   / )| (    )|| (    \/  | (    \/| (   ) || () () || (    \/   ) (   | )   ( |   ) (   |  \  ( || (    \/  
       | |    \ (_) / | (____)|| (__      | (_____ | |   | || || || || (__       | |   | (___) |   | |   |   \ | || |        
       | |     \   /  |  _____)|  __)     (_____  )| |   | || |(_)| ||  __)      | |   |  ___  |   | |   | (\ \) || | ____   
       | |      ) (   | (      | (              ) || |   | || |   | || (         | |   | (   ) |   | |   | | \   || | \_  )  
       | |      | |   | )      | (____/\  /\____) || (___) || )   ( || (____/\   | |   | )   ( |___) (___| )  \  || (___) |  
       )_(      \_/   |/       (_______/  \_______)(_______)|/     \|(_______/   )_(   |/     \|\_______/|/    )_)(_______)  
                                                                                                                         

""")

print("Welcome to Guess the Number!")
print("I'm thinking of a number between 1 and 100")

difficulty = input("Choose the difficulty level 'easy' or 'hard': ")

def diffi(level):
    if level == "easy":
        return 10
    if level == "hard":
        return 5
    else:
        print("You didn't enter a valid level, easy set as default.")
        return 10
    

my_num = int(input(f"You have {diffi(difficulty)} attempts remaining. Make a guess: "))
game(my_num, diffi(difficulty))