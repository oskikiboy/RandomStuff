from random import randint

def run():
    # Make the value yes initially so that it can run at least once.
    roll_again = "yes"
    while roll_again == "yes" or roll_again == "y":
        print("Rolling the die...")
        print(randint(1, 6))
        roll_again = input("Roll the die again? ")
    if not roll_again == "yes" or roll_again == "y":
        pass
