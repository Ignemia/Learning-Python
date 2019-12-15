# Plan: Make an app that works just like the square app but returns and prints factorial with full inscription
end = False
def factorial(a):
    if (a == 'quit') or (a == 'Quit'):
        end = True
        # after the quare app this feels so much easier.
        # I actually feel like I'm getting somewhere without much trouble
        return False
    try:
        a = int(a)
        x = 1
        value_storage = 1
        string_to_print = ""
        while x <= a:
            x = x+1
            # trying to do a lambda here but doesn't work. Will need to look into lambdas in next commit
            #string_to_print += x == a ? x : x+"*"
            if x == a:
                string_to_print += x+"*"
            else: 
                string_to_print += x
            value_storage = value_storage*x
        
        return print(value_storage)
    # I wrote catch agane... Python has to be queer doesn't it
    #catch:
    except:
        return print("We need a number to make factorial of. Try agane!")

def __main__():
    if not(end):
        print("Give me a number to make factorial off:")
        user_input = input()
        factorial(user_input)
        __main__()

__main__()
# I'm about to run it for the first time. It feel like it could work. Let's hope.

