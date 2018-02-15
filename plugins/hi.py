from time import sleep

def run():
    # Colours for logging.
    class pColours: 
        def red(x):
            return(f"\033[91m{x}\33[0m")
        def yellow(x):
            return(f"\033[93m{x}\33[0m")
        def green(x):
            return(f"\033[32m{x}\33[0m")
        def blue(x):
            return(f"\033[34m{x}\33[0m")
    # Make an empty array for responses.
    responses = []
    # Await for imput.
    x = input("What is your name? ")
    responses.append(x)
    print(f"{pColours.red(x)}, you are a sick dude!")
    y = input("What is your favourite activity? ")
    responses.append(y)
    print(f"I like {pColours.yellow(y)} too!")
    z = input(f"{pColours.blue(x)}, what is your favourite meme? ")
    responses.append(z)
    print(f"{pColours.green(z)} is the best {pColours.red('mem')}!")
    # Print responses.
    print("Your responses:")
    print("---------------")
    num = 1
    for x in responses:
        print(num, x)
        num += 1
    sleep(2)
    pass
