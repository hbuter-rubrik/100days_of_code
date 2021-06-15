# Add logo 
from art import logo

# Calculator
# Add
def add(n1, n2):
  return n1 + n2
# Subtract
def subtract(n1, n2):
  return n1 - n2
# Multiply
def multiply(n1, n2):
  return n1 * n2
# Divide
def divide(n1, n2):
  return n1 / n2
# Create dictionary with operations
operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
  }
#ask the user for numbers and operation

def calculator():
  print(logo)
  num1 = float(input("What is the first number?: "))
  for symbol in operations:
    print(symbol)
  should_continue = True

  while should_continue:
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What is the next number?: "))
    # Calculate
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)

    print(f"{num1} {operation_symbol} {num2} = {answer}")

    ask_user = input(f"Type 'y' to continue calculating with {answer}, type 'n' to start again, or any other key to exit: ")
    if ask_user == 'y' or ask_user == 'Y':
      num1 = answer
    elif ask_user == 'n' or ask_user == 'N':
      should_continue = False
      calculator()
    else:
      should_continue = False

calculator()






