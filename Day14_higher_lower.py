'''
100 Days of Python: Day 14
Higher o Lower Game

Rules: THe user is presented with two celebrities A and B and has to guess which of the two has 
the highest follower count in millions on instagram. 
        If the user guesses it right, the user is presented with another celebrity to be compared 
        with the previous B option.

The game has the possibility to be played indefinitely as long as the user keeps selecting Y to continue the game.
'''

import random
import os

# List containing the celebrity dataset (list of dictionaries)
celebrity_data = [
    {"name": "Cristiano Ronaldo", "follower_count": 620},
    {"name": "Lionel Messi", "follower_count": 500},
    {"name": "Selena Gomez", "follower_count": 430},
    {"name": "Kylie Jenner", "follower_count": 400},
    {"name": "Dwayne Johnson", "follower_count": 390},
    {"name": "Ariana Grande", "follower_count": 380},
    {"name": "Kim Kardashian", "follower_count": 360},
    {"name": "Beyoncé", "follower_count": 320},
    {"name": "Justin Bieber", "follower_count": 295},
    {"name": "Taylor Swift", "follower_count": 280},
    {"name": "Neymar Jr", "follower_count": 220},
    {"name": "Katy Perry", "follower_count": 200},
    {"name": "Rihanna", "follower_count": 155},
    {"name": "LeBron James", "follower_count": 160},
    {"name": "Cardi B", "follower_count": 170},
    {"name": "Billie Eilish", "follower_count": 110},
    {"name": "Zendaya", "follower_count": 185},
    {"name": "Shakira", "follower_count": 90},
    {"name": "Ed Sheeran", "follower_count": 45},
    {"name": "Miley Cyrus", "follower_count": 215},
    {"name": "Drake", "follower_count": 145},
    {"name": "Post Malone", "follower_count": 27},
    {"name": "Elon Musk", "follower_count": 12},
    {"name": "Ryan Reynolds", "follower_count": 50},
    {"name": "Will Smith", "follower_count": 65},
    {"name": "Tom Holland", "follower_count": 75},
    {"name": "Gal Gadot", "follower_count": 85},
    {"name": "Priyanka Chopra", "follower_count": 90},
    {"name": "Chris Hemsworth", "follower_count": 60},
    {"name": "Kevin Hart", "follower_count": 175},
]

# game function
def game(celebrity_data):
    '''
    Function that activates the higher or lower game.
    '''
    score = 0
    right_ans = ''
    playing = True
    os.system('cls' if os.name == 'nt' else 'clear')

    print('''
    __        __            __                           
    /  |      /  |          /  |                          
    $$ |____  $$/   ______  $$ |____    ______    ______  
    $$      \ /  | /      \ $$      \  /      \  /      \ 
    $$$$$$$  |$$ |/$$$$$$  |$$$$$$$  |/$$$$$$  |/$$$$$$  |
    $$ |  $$ |$$ |$$ |  $$ |$$ |  $$ |$$    $$ |$$ |  $$/ 
    $$ |  $$ |$$ |$$ \__$$ |$$ |  $$ |$$$$$$$$/ $$ |      
    $$ |  $$ |$$ |$$    $$ |$$ |  $$ |$$       |$$ |      
    $$/   $$/ $$/  $$$$$$$ |$$/   $$/  $$$$$$$/ $$/       
                /  \__$$ |                              
                $$    $$/                               
                $$$$$$/                                
    __                                                   
    /  |                                                  
    $$ |  ______   __   __   __   ______    ______        
    $$ | /      \ /  | /  | /  | /      \  /      \       
    $$ |/$$$$$$  |$$ | $$ | $$ |/$$$$$$  |/$$$$$$  |      
    $$ |$$ |  $$ |$$ | $$ | $$ |$$    $$ |$$ |  $$/       
    $$ |$$ \__$$ |$$ \_$$ \_$$ |$$$$$$$$/ $$ |            
    $$ |$$    $$/ $$   $$   $$/ $$       |$$ |            
    $$/  $$$$$$/   $$$$$/$$$$/   $$$$$$$/ $$/             
                                                        
                                                        
                                                        
    ''')

    A = random.choice(celebrity_data)
    B = random.choice(celebrity_data)
    while playing:
        print(f"Compare {A['name']}\n")
        print('''          
        __     __  _______ 
        /  \   /  |/       |
        $$  \ /$$//$$$$$$$/ 
        $$  /$$/ $$      \ 
        $$ $$/   $$$$$$  |
        $$$/   /     $$/ 
            $/    $$$$$$$/                  
        \n''')
        print(f"with {B['name']}")
        answer = input("Select one (A/B): ")

        diff = A['follower_count'] - B['follower_count']
        if diff > 0:
            right_ans = 'A'
        else:
            right_ans = 'B'
        if answer == right_ans:
            score +=1
            A = B           # the second item becomes the first one of the comparison
            B = random.choice(celebrity_data)   # the second item is picked again from the list
        else:
            score += 0
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"Wrong! Your final score is: {score}")
            playing = False

# Body of the program
# Inizial global variabiles
start_game = input("Do you want to play the Higher o Lower game (Y/N)?: ")
keep_going = True

if start_game == "Y":
    # Playing loop
    while keep_going:
        game(celebrity_data)
        exit = input("Do you want to keep going? (Y/N): ")
        if exit == "N":
            print("Ok, bye!")
            keep_going = False
        else:
            continue
else:
    print("Ok, bye!")

        

