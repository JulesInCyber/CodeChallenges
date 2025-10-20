import random as rd

random_number = rd.randint(1, 10)
user_guess = int(input("Guess a number between 1 and 10: "))

while True:
    if user_guess > random_number:
        user_guess = int(input("Too high! Guess again: "))
    elif user_guess < random_number:
        user_guess = int(input("Too low! Guess again: "))
    else:
        print(f"Great! You win\nThe number was {random_number}")
        play_again = input("Want to play again? (y/n): ")
        if play_again == "y":
            random_number = rd.randint(1,10)
            user_guess = int(input("Guess a number between 1 and 10: "))
        else:
            print("Thank you for Playing\nBYE!")
            break