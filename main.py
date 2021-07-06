def compute(number1, operation, number2):
    if is_number(number1) and "+-*/^".__contains__(operation) and is_number(number2):
        result = 0
        if operation == "+":
            result = float(number1) + float(number2)
        elif operation == "-":
            result = float(number1) - float(number2)
        elif operation == "*":
            result = float(number1) * float(number2)
        elif operation == "/":
            result = float(number1) / float(number2)
        elif operation == "^":
            result = pow(float(number1), float(number2))
        print(number1 + " " + operation + " " + number2 + " = " + format(result, ".2f"))
    else:
        print("Error, some character is not ok")


def is_number(string):
    try:
        float(string)
        return True
    except ValueError:
        return False


if __name__ == '__main__':
    input_a = input("First number? ")
    input_b = input("Operation (+, -, /, *, ^)? ")
    input_c = input("Second number? ")
    compute(input_a, input_b, input_c)
