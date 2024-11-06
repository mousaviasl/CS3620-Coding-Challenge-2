def divide_numbers(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    return result


num1 = float(input("Enter numerator: "))
num2 = float(input("Enter denominator: "))
print(divide_numbers(num1, num2))