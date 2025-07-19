import random

#           the main game functuion

def guess_the_number():

    print("welcome to the number guessing game"/n)
    print("imma guess a number 1-100, and your going to have to guess that number")
    
    #main variables
    
    number = random.randint(1, 100)
    guesses_taken = 0
    
    #main game loop
    
    while True:
        guess = input("Enter your guess (or type 'quit' to give up): ")
        if guess.lower() == 'quit':
            print(f"Sorry to see you go! The number was {number}.")
            break
        if not guess.isdigit():
            print("Please enter a valid number.")
            continue
        guess = int(guess)
        guesses_taken += 1
        if guess < number:
            print(" higher! Try again.")
        elif guess > number:
            print(" lower! Try again.")
        else:
            print(f"Congratulations! You guessed the number in {guesses_taken} tries.")
            break

#           Lastly we need to call the function



guess_the_number()