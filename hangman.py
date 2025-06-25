import random

def display_hangman(wrong_guesses):
    stages = [
        """
           ------
           |    |
           |
           |
           |
           |
        --------
        """,
        """
           ------
           |    |
           |    O
           |
           |
           |
        --------
        """,
        """
           ------
           |    |
           |    O
           |    |
           |
           |
        --------
        """,
        """
           ------
           |    |
           |    O
           |   /|
           |
           |
        --------
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |
           |
        --------
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |   /
           |
        --------
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |   / \\
           |
        --------
        """
    ]
    return stages[wrong_guesses]

def display_word(word, guessed_letters):
    return " ".join(letter if letter in guessed_letters else "_" for letter in word)

def hangman_game():
    words = ["python", "computer", "programming", "hangman", "challenge"]
    word = random.choice(words)
    guessed_letters = []
    wrong_guesses = 0
    max_wrong_guesses = 6

    print("Welcome to Hangman!")
    print(f"You have {max_wrong_guesses} incorrect guesses allowed.\n")

    while wrong_guesses < max_wrong_guesses:
        print(display_hangman(wrong_guesses))
        print(f"Word: {display_word(word, guessed_letters)}")
        print(f"Guessed letters: {', '.join(sorted(guessed_letters))}")
        print(f"Wrong guesses: {wrong_guesses}/{max_wrong_guesses}")

        if all(letter in guessed_letters for letter in word):
            print(f"\nCongratulations! You guessed the word: {word}")
            break

        guess = input("\nEnter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print(f"Good guess! '{guess}' is in the word.")
        else:
            print(f"Sorry, '{guess}' is not in the word.")
            wrong_guesses += 1

        print("-" * 40)

    if wrong_guesses >= max_wrong_guesses:
        print(display_hangman(wrong_guesses))
        print(f"Game Over! The word was: {word}")

    play_again = input("\nWould you like to play again? (y/n): ").lower()
    if play_again in ['y', 'yes']:
        hangman_game()
    else:
        print("Thanks for playing!")

if __name__ == "__main__":
    hangman_game()
