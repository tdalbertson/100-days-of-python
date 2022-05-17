# Day 10 - Python Calculator Program

# Modules
from calculator_art import logo
import pyinputplus as pyip

# Function Definitions
def add(num1, num2):
    """Adds 2 numbers together

    Args:
        num1 (int/float): First number
        num2 (int/float): Second number

    Returns:
        int/float: Sum of 2 numbers
    """
    return num1 + num2

def subtract(num1, num2):
    """Subtract 2 numbers

    Args:
        num1 (int/float): First number
        num2 (int/float): Second number
    
    Returns:
        int/float: Difference of 2 numbers
    """
    return num1 - num2

def multiply(num1, num2):
    """Multiply 2 numbers

    Args:
        num1 (int/float): First number
        num2 (int/float): Second number

    Returns:
        int/float: Product of 2 numbers
    """
    return num1 * num2

def divide(num1, num2):
    """Divide 2 numbers

    Args:
        num1 (int/float): First number
        num2 (int/float): Second number

    Returns:
        int/float: Quotient of 2 numbers
    """
    return num1 / num2

def calculator():
    # Get initial numbers to calculate
    n1 = float(pyip.inputNum(prompt="What's the first number? "))
    n2 = float(pyip.inputNum(prompt="What's the second number? "))
    
    while True:
     # Get operation
        operation_symbol = pyip.inputChoice(['+', '-', '*', '/'], prompt="+\n-\n*\n/\nPick an operation: ")

        # Get associated function
        operation_function = operations[operation_symbol]
        # Process data
        result = operation_function(n1, n2)

        # Output the results
        print(f"{n1} {operation_symbol} {n2} = {result}")
        
        # Check if user wants to continue calculations
        if pyip.inputYesNo(prompt=f"Type 'yes' to continue calculating for {result} or type 'no' to start a new calculation: ") == 'yes':
            # Gather and reassign new data
            n1 = result
            n2 = pyip.inputNum(prompt="What's the next number?: ")
            print(n1, n2)
        else:
            calculator()

# Global variable

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

# Main program flow
print(logo)

calculator()
