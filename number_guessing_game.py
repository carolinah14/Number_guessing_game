import random
from art_game import logo

difficulty = {
        "easy": 10,
        "hard": 5,
    }

def guesses(easy_or_hard, number, u_guess):
    if u_guess == number:
        return f"You guessed correctly! the number was {number}."
    elif u_guess < number:
        difficulty[easy_or_hard] -= 1
        return "Too low!"
    difficulty[easy_or_hard] -= 1
    return "Too high!"

def game():
    print(logo)
    chosen_number = random.randint(1, 100)
    print("Welcome to the Number Guessing Game!\n"
          "I'm thinking of a number between 1 and 100.")


    difficulty_chosen = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    game_over = False

    while not game_over:
        print(f"You have {difficulty[difficulty_chosen]} attempts remaining to guess the number.")
        user_guess = int(input("Enter your guess: "))
        print(guesses(difficulty_chosen, chosen_number, user_guess))
        if user_guess == chosen_number:
            game_over = True
        elif difficulty[difficulty_chosen] != 0:
            print("Guess again.")
        elif difficulty[difficulty_chosen] == 0:
            print(f"You ran out of guesses. The number was {chosen_number}.")
            game_over = True

game()
input("\nPress ENTER to close the game.")
