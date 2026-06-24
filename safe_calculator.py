def calculator(first, second, operator):
        if operator == "+":
            return first + second
        elif operator == "-":
            return first - second
        elif operator == "*":
            return first * second
        elif operator == "/":
            return first / second
        else:
            raise ValueError("Invalid operator")


try:
    first = int(input("First No: "))
    second = int(input("Second No: "))
    operator = input("Operator: ")
    result = calculator(first, second, operator)
    print(result)
except ValueError:
    print("Please enter a valid number.")
except ZeroDivisionError:
    print("Cant divided by zero")

