import random

# Word list dictionary
WORD_LIST = {
    "fruits": [
        "apple", "banana", "cherry", "date", "elderberry", "fig", 
        "grape", "kiwi", "lemon", "mango", "orange", "papaya"
    ],
    "animals": [
        "cat", "dog", "elephant", "giraffe", "hippopotamus", "lion",
        "monkey", "panda", "rhinoceros", "tiger", "zebra"
    ],
    "countries": [
        "brazil", "canada", "egypt", "france", "germany", "india",
        "japan", "mexico", "nigeria", "spain", "thailand"
    ]
}

# Hangman art stages
HANGMAN_PICS = [
    '''
       +---+
       |   |
           |
           |
           |
           |
    =========
    ''', '''
       +---+
       |   |
       O   |
           |
           |
           |
    =========
    ''', '''
       +---+
       |   |
       O   |
       |   |
           |
           |
    =========
    ''', '''
       +---+
       |   |
       O   |
      /|   |
           |
           |
    =========
    ''', '''
       +---+
       |   |
       O   |
      /|\  |
           |
           |
    =========
    ''', '''
       +---+
       |   |
       O   |
      /|\  |
      /    |
           |
    =========
    ''', '''
       +---+
       |   |
       O   |
      /|\  |
      / \  |
           |
    =========
    '''
]

def choose_word(category):
    """Returns a random word from the given category list."""
    return random.choice(WORD_LIST[category])

def display_word(word, guessed_letters):
    """Shows the word with blanks for unguessed letters."""
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()

def choose_category():
    """Asks the user to choose a word category and validates the input."""
    print("Choose a category:")
    categories = list(WORD_LIST.keys())
    
    for i, category in enumerate(categories, 1):
        print(f"  {i}. {category.capitalize()}")

    while True:
        try:
            choice = input(f"Enter the number (1-{len(categories)}): ")
            choice_num = int(choice)
            
            if 1 <= choice_num <= len(categories):
                return categories[choice_num - 1]
            else:
                print("Invalid number. Please try again.")
        except ValueError:
            print("That's not a number. Please try again.")

def hangman():
    """Runs a single game of Hangman from start to finish."""
    print("=======================")
    print(" Welcome to Hangman! ")
    print("=======================")
    
    chosen_category = choose_category()
    secret_word = choose_word(chosen_category)
    
    guessed_letters = []
    lives = 6
    won = False

    while lives > 0:
        print(HANGMAN_PICS[6 - lives])
        print("\n" + "="*30)
        print(f"Category: {chosen_category.capitalize()}")
        print("Word:", display_word(secret_word, guessed_letters))
        print("Lives left:", lives)
        
        if guessed_letters:
            print(f"Guessed letters: {' '.join(sorted(guessed_letters))}")

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("\nInvalid input. Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print(f"\nYou already guessed '{guess}'. Try again.")
            continue
        
        guessed_letters.append(guess)
        
        if guess in secret_word:
            print(f"\nGood guess! '{guess}' is in the word.")
            if set(guessed_letters) >= set(secret_word):
                won = True
                break
        else:
            print(f"\nIncorrect guess. '{guess}' is not in the word.")
            lives -= 1

    print("\n" + "="*30)
    if won:
        print("🎉 Congratulations! You guessed the word!")
        print(f"The word was: {secret_word}")
    else:
        print(HANGMAN_PICS[6])
        print("😢 Sorry, you ran out of lives.")
        print(f"The word was: {secret_word}")

if __name__ == "__main__":
    while True:
        hangman()  # Run the full game

        # Ask the user to play again
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        
        # If the answer isn't 'yes' or 'y', break the loop
        if play_again not in ('yes', 'y'):
            print("\nThanks for playing! Goodbye! 👋")
            break
        
        # Otherwise, the loop will repeat for a new game
        print("\nStarting a new game... 🎉\n")
