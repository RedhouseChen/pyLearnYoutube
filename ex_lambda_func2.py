# ex_lambda_func2.py
# Lambda function is a concise way to create anonymous functions on the fly.
# Usage: lambda arguments: expression

# Example: Using lambda function with higher-order function (map)
# List of numbers
numbers = [1,2,3,4,5]

# Using map() with a lambda function to square each number
squared_numbers = map(lambda x: x**2, numbers)

# Displaying the squared numbers
print("Squared Numbers:", list(squared_numbers))