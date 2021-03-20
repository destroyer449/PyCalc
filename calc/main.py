import numpy
from math import *
import sys

# TODO read input with basic parseing
def get_input():
    text = input(">")
    if text == "quit":
        print("Exiting")
        sys.exit()
    for i in text:
        if not (i.isalnum or i in "-+/*()[]^|,;"):
            print("symbol not recognized", i)
            return False
    return text


# TODO build AST and calculations
def calculate(text):
    if text == False:
        return "ERROR"
    return exec(f"print({text})")


def main():
    while True:
        text = get_input()
        result = calculate(text)
        if result in ["NaN", "Inf", "-Inf", "ERROR"]:
            print("Calculation failed")
        else:
            print(result)
