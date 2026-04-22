
# 📘 Assignment: Games in Python - Hangman

## 🎯 Objective

Build a classic Hangman game in Python to practice strings, loops, conditionals, and user input handling.

## 📝 Tasks

### 🛠️ [Set Up the Word and Game State]

#### Description
Create the initial structure of the Hangman game. Define a list of words, select one word at random, and initialize the variables needed to track guessed letters and remaining attempts.

#### Requirements
Completed program should:

- Define a predefined list of possible words.
- Randomly select one word for the current match.
- Initialize a hidden progress view (for example: `_ _ _ _`) based on the selected word.
- Track guessed letters in a dedicated variable or collection.
- Set a fixed number of allowed incorrect attempts.


### 🛠️ [Implement Guess Loop and End Conditions]

#### Description
Implement the gameplay loop where the player enters letter guesses. Update progress after each guess, decrease attempts for incorrect guesses, and end the game with a win or loss message.

#### Requirements
Completed program should:

- Repeatedly ask the player for a letter guess until the game ends.
- Reveal correct letters in all matching positions.
- Decrease remaining attempts only for incorrect guesses.
- Stop the game when the full word is guessed or attempts reach zero.
- Display a clear final message for victory or defeat.