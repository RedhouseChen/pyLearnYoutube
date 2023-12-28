# ex_lambda_func.py
# Lambda function is a concise way to create anonymous functions on the fly.
# Usage: lambda arguments: expression

 # Instead of this:
def add(x,y):
    return x+y

#
z = add(5,6)
print(z)

# You can do this with a lambda function
# add_lambda = lambda x,y: x+y
x=5
y=7
add_lambda = lambda x,y: x+y
print(add_lambda)
