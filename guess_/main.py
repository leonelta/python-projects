import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess is random_number:
        