import random
# Generate a random integer between a range
random_number = random.randint(1, 100)
breakpoint()
# Get the user input
user_input = input("Guess a number between 1 and 100: ")
user_guess = int(user_input)
print(F"user guess {user_guess}")