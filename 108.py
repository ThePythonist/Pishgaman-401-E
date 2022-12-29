from random import randint

numbers = randint(1, 10)
chances = 5

print("Welcome to number guessing game")

while chances > 0:
    print(f"You have {chances} chances left")

    guess = input("Guess the number : ")
    try:
        guess = int(guess)
        if guess == numbers:
            print("You won!")
            break
        elif guess > numbers:
            print("Try smaller than", guess)
        else:
            print("Try bigger than", guess)
        chances -= 1
    except ValueError:
        print("Invalid input. Try again")

if chances == 0:
    print("Game Over! The number was :", numbers)
