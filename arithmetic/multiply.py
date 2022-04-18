# A function that returns the multiplication result of all arguments
# A function that returns the multiplication of all argument numbers numbers

def multiply(*numbers):
    total = 1
    for number in numbers:
    	total *=number
    return total
