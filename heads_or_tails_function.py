import random

def get_user_guess():
    user_guess = input('Guess the coin flip! Enter heads or tails (h/t):')
    return user_guess

random_number = random.randint(0, 1)


def get_coin_flip():
    if random_number == 0:
        print('The coin flip was: heads')
        return 'h'
    else:
        print('The coin flip was: tails')
        return 't'
    
if __name__ == '__main___':
    
    user_guess = get_user_guess()    
    random_flip = get_coin_flip()

    if (random_flip == user_guess):
        print('you guessed correct')
    else:
        print('you guessed wrong')    
