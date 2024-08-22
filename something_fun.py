import random 

def guessing_game():
    number_to_guess = random.randint(1, 100)
    guess = None
    attempts = 0

    print("welcome to the number guessing game")
    print("I'm thinking of a number one and one hundred")

    while guess != number_to_guess:

        guess = int(input("Take a guess: "))
        attempts += 1
        maxattempts = 10


        if guess < number_to_guess:
            print(f"Too low! Try again. {attempts} attempts")
        elif guess > number_to_guess:
            print(f"Too High! Try again. {attempts} attempts")
        
        else: 
            print(f"Congratulations! You guessed the number in {attempts} attempts.")


guessing_game()


#max attempts
#add a quit feature after 3 attempts