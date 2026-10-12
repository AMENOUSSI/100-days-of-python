from random import randint
import art

print(art.logo)
# Function to check user's guess number against the actual answer

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def check_answer(user_guess,actual_answer, turns):
    """Checks anwer against guess, returns the number of turns"""
    if user_guess > actual_answer:
        print("Too high.")

        return turns - 1
    elif user_guess < actual_answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {actual_answer}.")

# Function to set difficulty
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def game():
    # Choosing a random number between 1 and 100
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100")
    answer = randint(1,100)
    print(f"Pssst, the correct answer is {answer}")

    turns = set_difficulty()
    print(f"You have {turns} attempts remaining to guess the number.")

    # Repeat the guessing functionality if they get it wrong
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        # Let the user guess the number
        guess = int(input("Make a guess: "))

        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out of the guesses, you lose")
            return
        elif guess != answer:
            print("Guess again!")


game()
    # Track the number of turns and reduce by 1 if they get it wrong

