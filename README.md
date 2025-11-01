# 🎮 Python Hangman Game

A classic command-line Hangman game built with Python. This script includes multiple word categories, ASCII art for the hangman, and a "play again" feature.

---

## 🚀 Features

* **Word Categories:** Players can choose from multiple categories (Fruits, Animals, Countries) for a varied experience.
* **ASCII Art:** Displays the classic hangman drawing as the player makes incorrect guesses.
* **Robust Input:** Handles invalid inputs (e.g., non-letters, duplicate guesses) gracefully.
* **Win/Loss Logic:** Correctly manages player lives, only decrementing on incorrect guesses.
* **Play Again:** Asks the user if they want to play another round after a game ends.
* **Clean UI:** Shows the category, guessed letters, and remaining lives on each turn.

---

## 💻 How to Play

You must have Python 3 installed to run this game.

1.  **Clone or Download:**
    Get the code from this repository.
    ```sh
    git clone [https://github.com/YOUR-USERNAME/python-hangman.git](https://github.com/YOUR-USERNAME/python-hangman.git)
    cd python-hangman
    ```

2.  **Run the Game:**
    Execute the Python script from your terminal.
    ```sh
    python hangman.py
    ```

3.  **Follow the Prompts:**
    The game will first ask you to pick a category, and then you can start guessing letters!

    ```
    =======================
     Welcome to Hangman! 
    =======================
    Choose a category:
      1. Fruits
      2. Animals
      3. Countries
    Enter the number (1-3): 2
    
           +---+
           |   |
               |
               |
               |
               |
    =========
    
    ==============================
    Category: Animals
    Word: _ _ _ _ _ _ _ _ _ _ _ _
    Lives left: 6
    Guess a letter: e
    ```

---

## 📜 License

This project is licensed under the MIT License. See the `LICENSE` file for details.
