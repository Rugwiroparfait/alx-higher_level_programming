#!/usr/bin/python3
# 12-fizzbuzz.py
# Rugwiro G Parfait <rugwiroparfait003@gmail.com?

def fizzbuzz():
    """Print the number from 1 to 100 separated by a space.

    for multiple of five, print Buzz instead of the number.
    for multiple of three,print Fizz instead of the number.
    for multiple of three, and five , print FizzBuzz instead of the number.
    """
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz ", end="")
        elif number % 3 == 0:
            print("Fizz ", end="")
        elif number % 5 == 0:
            print("Buzz ", end="")
        else:
            print("{} ".format(number), end="")
