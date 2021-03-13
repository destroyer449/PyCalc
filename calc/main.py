import numpy
import math

# TODO read input with basic parseing
def get_input():
    text = input(">")
    for i in text:
        if i not in "1234567890-+/*()[]^|":
            print("symbol not recognized", i)
            return "ERROR"
    return text


# TODO build AST and calculations
def calculate(text):
    return exec(f"print({text})")


def main():
    while True:
        text = get_input()
        if text == "quit":
            print("Leave; see if I care!")
            break
        result = calculate(text)
        if result in ["NaN", "Inf", "-Inf", "ERROR"]:
            print("Calculation failed")
        else:
            print(result)
