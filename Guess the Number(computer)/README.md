# Number Guessing Game

This is a simple Python program where the user tries to guess a randomly generated number within a specified range.

# How to Play

1. Run the guess(x) function, where x is the maximum number allowed in the range.
2. The program will generate a random number between 1 and x.
3. You'll be prompted to guess the number.
4. After each guess, the program will inform you if your guess is too high or too low.
5. Keep guessing until you correctly guess the random number.
6. Once you guess the number correctly, the program will congratulate you.

# About the Random Module

The random module in Python provides functions for generating random numbers. It includes various methods for generating random integers, selecting random elements from a sequence, and shuffling sequences randomly.

Some commonly used functions from the random module include:
- random(): Returns a random floating-point number between 0 and 1.
- randint(a, b): Returns a random integer between a and b, inclusive.
- choice(seq): Returns a random element from the given sequence.
- shuffle(seq): Randomly shuffles the elements of a sequence in place.

For this number guessing game, we use random.randint(a, b) to generate a random number within a specified range.

In this game, we use randint(1, x) to generate a random number between 1 and x.
