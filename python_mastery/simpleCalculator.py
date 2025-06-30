# Ask the user for the first number
print("Enter the first number: ")
first = float(input('>'))
# Ask the user for the second number
print("Enter the second number: ")
# Get the second number
second = float(input('>'))
# Ask the user for the operation
print("Enter the operation +, -, *, /: ")
operation = input()
if operation == "+":
    print('The sum is: ' + str(first + second))
elif operation == "-":
    print('The difference is: ' + str(first - second))
elif operation == "*":
    print('The product is: ' + str(first * second))
elif operation == "/":
    print('The quotient is: ' + str(round(first / second, 3)))
else:
    print('Invalid operation')