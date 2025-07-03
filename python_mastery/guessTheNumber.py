import random
secret_number = random.randint(1, 20)
print("I'm thinking of a number between 1 and 20")

#Ask player to guess 6 times
for guesses_taken in range(7):
    print("Take a guess: ")
    guess = int(input("> "))
    
    if guess < secret_number:
        print("Your guess is too low!")
    elif guess > secret_number:
        print("Your guess is too high")
    else:
        break
if guess == secret_number:
    print(f"Great Job! You got it in {guesses_taken + 1} guesses!")
else:
    print(f"Nope. The number was {secret_number}")