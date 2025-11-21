import random

def guess_number():
    number = random.randint(1, 20)
    print("Guess the number between 1 and 20!")
    trial = 0

    while trial < 5:
        try:
            guess = int(input("Your guess: "))
        except ValueError:
            print("Please enter a valid number!")
            continue

        trial += 1

        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
        else:
            print("Correct! You guessed it!")
            return

    print(f"Sorry, the number was {number}.")

def main():
    guess_number()

main()

# completion of program 