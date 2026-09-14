def additoin(x, y):
    x = 10
    y = 20
    print("Addition:", x + y)

try:
    additoin(10, 20)
    print("The operation is successful")
except NameError:
    print("The operation failed: a variable is not defined")
