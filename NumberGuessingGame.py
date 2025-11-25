import random

print("Welcome to the Number Guessing Game\n")
print("I'm picking a number between 1 and 100.\n")
def set_difficulty():
    difficulty = input("Choose a difficulty. 'easy' or 'hard': ")
    if (difficulty == "easy"):
        return 10
    elif (difficulty == "hard"):
        return 5


def game():
    """The main logic for the guessing game."""
    number = random.randint(1, 100)
    attempts = set_difficulty()
    print(f"You have {attempts} attempts to guess the number.")
    
    while (attempts > 0):
        guess = int(input("Make a guess: "))

        if (guess == number):
            print(f"Got it! The answer was {number}")
            return
        
        if (guess > number):
            print("Too high.\n")
        elif (guess < number):
            print("Too low.\n")
            
        attempts -= 1
        print(f"You have {attempts} attempts remaining.")
        
        if attempts == 0:
            print("You couldn't find the number. You lose!")
            print(f"The number was {number}")
            return

game()
