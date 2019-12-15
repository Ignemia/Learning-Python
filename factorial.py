# Plan: Make an app that works just like the square app but returns and prints factorial with full inscription
end = False
def factorial(a):
    # I again forgot to put the global variable definition
    global end
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
        # I'm gonna debug by printing all out right here
        print(a)
        print(x)
        print(value_storage)
        print(string_to_print)
        # It returns this for input of 5
        # 5
        # 5
        # 1
        # 1
        # Which is really weird because string_to_print is empty string.
        # What was  I thinking? I build the factorial app like 1500 times in js and I stupidly put <= there
        #while x <= a:
        while x < a:
            x = x+1
            # trying to do a lambda here but doesn't work. Will need to look into lambdas in next commit
            #string_to_print += x == a ? x : x+"*"
            #if x == a:
            #    string_to_print += x+"*"
            #else: 
            #    string_to_print += x
            value_storage = value_storage*x
        # I just realized that I did not add string_to_print to the print output
        # Adding it didn't change anything about the output.
        # I'll try and disable the work with string in general

        #return print(string_to_print+value_storage)
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
# I was so wrong as I could possibly be.
# It's saying that it has issue with the game at parsing numbers but I do not know why
