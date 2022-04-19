# Afunction that reverse the order of a string 
def reverse_string_with_loop(input_string):
    reversed_str = ""
    for char in input_string:
        reversed_str = char + reversed_str
    return reversed_str
