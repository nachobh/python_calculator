import math


def compute(number1, operation, number2):
    if number1.isnumeric() and "+-*/^".__contains__(operation) and number2.isnumeric():
        result = 0
        if operation == "+":
            result = float(number1) + float(number2)
        if operation == "-":
            result = float(number1) - float(number2)
        if operation == "*":
            result = float(number1) * float(number2)
        if operation == "/":
            result = float(number1) / float(number2)
        if operation == "^":
            result = pow(float(number1), float(number2))
        print(number1 + " " + operation + " " + number2 + " = " + format(result, ".2f"))
    else:
        print("Error, some character is not ok")


if __name__ == '__main__':
    input_a = input("First number? ")
    input_b = input("Operation (+, -, /, *, ^)? ")
    input_c = input("Second number? ")
    compute(input_a, input_b, input_c)
