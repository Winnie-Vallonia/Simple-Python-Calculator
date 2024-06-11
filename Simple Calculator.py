### build a simple calculator

### take input from user
def Calculator():
    n1 =float(input("Enter a number: "))
    n2 = float(input ("Enter a second number: "))
    operation = input("What operation would you like to perform on these two numbers? addition, subtraction, multiplication, division: ").lower()

    if operation == "addition":
        output = n1 + n2
        return output
    elif operation == "subtraction":
        output = n1 - n2
        return output
    elif operation == "multiplication":
        output = n1 * n2
        return output
    elif operation == "division":
        if n2 != 0:
            output = n1 / n2
        else:
            return "Error: Division by zero is not allowed."
    else:
        return "Error: Invalid operation."
    return output
    
result = Calculator()
print("Result:", result)
