import random

def display_hangman(mistakes):
    drawings = [
        """
          -----
          |   |
              |
              |
              |
              |
        --------
        """,
        """
          -----
          |   |
          O   |
              |
              |
              |
        --------
        """,
        """
          -----
          |   |
          O   |
          |   |
              |
              |
        --------
        """,
        """
          -----
          |   |
          O   |
         /|   |
              |
              |
        --------
        """,
        """
          -----
          |   |
          O   |
         /|\\  |
              |
              |
        --------
        """,
        """
          -----
          |   |
          O   |
         /|\\  |
         /    |
              |
        --------
        """,
        """
          -----
          |   |
          O   |
         /|\\  |
         / \\  |
              |
        --------
        """
    ]
    return drawings[mistakes]

def play_hangman():
    word_hint_list = [
        ("lipstick", "A cosmetic for adding color to lips."),
        ("unicorn", "A mythical creature with a horn."),
        ("butterfly", "A colorful insect with wings."),
        ("jewelry", "Accessories like necklaces and bracelets."),
        ("tiara", "A small crown often worn by princesses."),
        ("daisy", "A beautiful white flower with a yellow center."),
        ("rainbow", "A colorful arc seen after rain."),
        ("perfume", "A fragrant liquid people wear."),
        ("princess", "A royal female character in fairy tales."),
        ("ballerina", "A graceful dancer in a tutu.")
    ]

    word, hint = random.choice(word_hint_list)
    guessed = set()
    mistakes = 0
    max_mistakes = 6

    print("Welcome to Hangman!")
    print(f"Hint: {hint}")

    while mistakes < max_mistakes:
        print(display_hangman(mistakes))
        word_display = [char if char in guessed else "_" for char in word]
        print("Word: " + " ".join(word_display))

        user_input = input("Guess a letter: ").lower()

        if len(user_input) != 1 or not user_input.isalpha():
            print("Enter a single valid letter.")
            continue

        if user_input in guessed:
            print(f"'{user_input}' was already guessed. Try again.")
        elif user_input in word:
            print(f"Nice! '{user_input}' is in the word.")
            guessed.add(user_input)
        else:
            print(f"'{user_input}' is not in the word.")
            guessed.add(user_input)
            mistakes += 1

        if all(char in guessed for char in word):
            print("Congratulations! You've guessed the word!")
            print(f"The word was: {word}")
            break
    else:
        print(display_hangman(mistakes))
        print("You lost! Better luck next time.")
        print(f"The correct word was: {word}")

play_hangman()
