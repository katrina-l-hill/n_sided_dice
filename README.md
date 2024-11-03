# Probability Calculator for N-sided Dice

## Author: Katrina Hill

## Description
This Python program simulates rolling dice and calculates the probability distribution of the sums obtained from rolling multiple dice. It allows users to specify the number of sides on the dice, the number of dice to roll, and the number of times to roll them.

## Features
- Roll a specified number of dice with a defined number of sides.
- Simulate multiple rolls and store the results.
- Calculate and display the probability distribution of possible sums from rolling the dice.

## Files
- `app.py`: The main program that performs the probability simulations.
- `tests.py`: A suite of tests for validating the functionality of the simulations.

## Requirements
- Python 3.11

## How to Run
1. **Clone the repository** (or download the files):
   - git clone https://github.com/katrina-l-hill/n_sided_dice
   - cd into the repository directory
2. **Run the Main program**:
   - run python app.py to run the program
   - the first prompt will be to enter the number of sides of the dice (n)
     - press enter after entering the number
   - the second prompt will be to enter the number of dice (m)
     - press enter after entering the number
   - the third prompt will be to enter the number of rolls (k)
     - press enter after entering the number
3. **Run the tests**:
   - run python -m pytest tests.py to run the tests