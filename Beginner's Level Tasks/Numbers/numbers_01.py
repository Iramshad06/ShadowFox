#1. Write a function that takes two arguments, 145 and 'o', and uses the `format` function to return a formatted string. Print the result. Try to identify the representation used.
def formatfunc(num, char):
    val = "{},{}".format(num, char)
    return val
str = formatfunc(145, 'o')
print("The Formatted String is :", str)
print("The Representation used is:", type(str).__name__)
