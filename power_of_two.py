#!/usr/bin/env python3
# Created By: Boluwatife Dada
# created on April 16
# This program accepts a whole number. It then uses a loop to calculate and display the “square” (power of 2) starting from 0 until this number.


def calculate_squares(limit):
    """Calculates and displays the squares of numbers from 0 up to (and including) the given limit."""
    try:
        num = int(limit)  # Try to convert the input to an integer
        if num < 0:
            print("Please enter a non-negative whole number.")
            return
        else:
            print(f"Squares from 0 to {num}:")
            for i in range(num + 1):
                square = i**2
                print(f"The square of {i} is {square}")
    except ValueError:
        print("Invalid input. Please enter a whole number.")


if __name__ == "__main__":
    user_input = input("Enter a whole number: ")
    calculate_squares(user_input)
