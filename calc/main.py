import numpy

# TODO read input with basic parseing


def get_input():
    return True


# TODO build AST and calculations
def calculate(text):
    return text


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
