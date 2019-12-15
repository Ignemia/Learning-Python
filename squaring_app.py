# This is how you make comments
# Haven't yet figured out how to effectively make multi-line comments - will work on that
# def is something like "function" in javascript
# weird Python doesn't use curly braces
# I would love to figure out how to force types for function parameters
# I should get people to input. I need to get the grip of handleing user inputs
def square(a):
    # well this is not the way
    #a = (int) a

    # somehow this is how you are supposed to cast types in python. I don't like it.
    # Well... it throws errors if I input characters or string into terminal. Will look into that and figure out try catch blocks.
    a = int(a)

    return print(a*a)

# this is weird you define variables without declaring either whether it is variable or constant for as much as I know atm. Not even datatypes. This feels off
user_input = input()
# this is simple. Method input is the only thing you need to get user to input into terminal.
square(user_input)
# ah s#17 doens't even work for numbers what is wrong
# The error says that it doesn't work because I'm giving it string even tho I am using the number 5 as input. Why does it do that?
# I'll try to cast it