# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Build the classic word-guessing game using Python strings, loops, and user input. Practice string manipulation, conditionals, and random selection while creating an interactive Hangman game.

## 📝 Tasks

### 🛠️	Set Up the Game

#### Description
Create the foundation of the Hangman game by setting up a word list and game state variables. The program should randomly select a word and prepare the display for the player.

#### Requirements
Completed program should:

- Randomly select a word from a predefined list
- Display the hidden word as underscores (e.g., `_ _ _ _ _`)
- Set the maximum number of incorrect attempts (e.g., 6)


### 🛠️	Implement the Game Loop

#### Description
Build the core gameplay loop where the player guesses letters one at a time. The program should check each guess, update the display, and determine when the game ends.

#### Requirements
Completed program should:

- Accept single-letter guesses from the player
- Reveal correctly guessed letters in the display (e.g., `_ a _ _ e _`)
- Track and display the number of incorrect guesses remaining
- End the game when the word is fully guessed or attempts run out
- Display a win message when the player guesses the word
- Display a lose message showing the correct word when attempts are exhausted
