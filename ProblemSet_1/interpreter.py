def calculate_expression(expression):
    x, operator, y = expression.split()
    x = float(x)
    y = float(y)

    if operator == '+':
        result = x + y
    elif operator == '-':
        result = x - y
    elif operator == '*':
        result = x * y
    elif operator == '/':
        if y == 0:
            return "Error: Division by zero!"
        result = x / y
    else:
        return ("")

    return round(result, 1)

def main():
    user_input = input("Enter an arithmetic expression (e.g., '5 + 3'): ")
    result = calculate_expression(user_input)
    print("Result:", result)

if __name__ == "__main__":
    main()
