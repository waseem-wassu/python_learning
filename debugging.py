import pdb

def some_function():
    x = 5
    y = 10
    pdb.set_trace()  # Start debugging here

    z = x + y
    return z

result = some_function()
print(result)
