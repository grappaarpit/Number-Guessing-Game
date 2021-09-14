#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
from art import logo
from random import randint
answer = randint(1,100)

def check_easy():
    global answer
    guessn = 0
    print("You have 10 guesses")
    while (guessn<10):
        guess = int(input("make a guess : "))
        if (guess> answer):
            print("Too high")
            guessn += 1
            
        if (guess< answer):
            print("Too low")
            guessn += 1
    
        if (guess == answer):
            print("Dayumn, you got it right, cONGRATS")
            return
    print("Game Over, you are out of guesses")
    print(f"The correct answer was {answer}")
        
            
def check_hard():
    global answer
    guessn = 0
    print("You have 5 guesses")
    while (guessn<5):
        guess = int(input("make a guess : "))
        if (guess> answer):
            print("Too high")
            guessn += 1
            
        if (guess< answer):
            print("Too low")
            guessn += 1
    
        if (guess == answer):
            print("Dayumn, you got it right, cONGRATS")
            return
    print("Game Over, you are out of guesses")
    print(f"The correct answer was {answer}")


print(logo)
level = input("Choose a level : easy or hard")

if level == "easy":
    check_easy()
else : 
    check_hard()
































