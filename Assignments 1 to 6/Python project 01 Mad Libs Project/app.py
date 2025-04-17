
def madlib():
    # Get user input
    name = input("Enter your name: ")
    snack = input("What’s your favorite snack? ")
    pet = input("What kind of pet do you have or want? ")
    place = input("Name a place you like: ")
    language = input("What's a programming language you like? ")
    bug = input("Name a funny bug or error you've seen: ")

    # Madlib story
    story = f"One fine morning, {name} woke up, grabbed a bag of {snack}, and sat in front of their computer.\n" \
            f"Next to them sat their loyal {pet}, watching curiously. They opened their laptop and started coding in {language}.\n" \
            f"But suddenly... BOOM! The screen flashed with an error: '{bug}'! 😱\n" \
            f"Instead of panicking, {name} smiled, took a deep breath, and whispered, 'Time for a break.'\n" \
            f"So they packed their {snack}, grabbed their {pet}, and went to {place} for a peaceful break before debugging the universe again. 🧑‍💻"

    print("\n--- Your Fun Coder Story ---\n")
    print(story)

madlib()

