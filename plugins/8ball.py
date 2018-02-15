from random import choice

def run():
    # Make an array of responses.
    responses = [
			"Unclear, ask again later",
			"Soon",
			"Yes",
			"Absolutely!",
			"Never",
			"Na you are too stupid!",
			"Maybe if you get your ma to do it for you",
			"Damn you are a bright spark",
			"You obviously didn\"t have many friends if your asking that question!",
			"Magic 8-ball is currently unavailable, please leave a message after the tone. \\*beep\\*",
			"When you are ready",
			"Hopefully",
			"Hopefully not",
			"Oh my, why would you even ask that?",
			"What kind of a question is that?",
			"Haha, funny joke"
		]
    # Make the value yes initially so that it can run at least once.
    ask_again = "yes"
    while ask_again == "yes" or ask_again == "y":
        input("What is your question for the magic 8ball? ")
        print(f"Magic 8ball says: {choice(responses)}")
        ask_again = input("Ask Again? ")
    if not ask_again == "yes" or ask_again == "y":
        pass
