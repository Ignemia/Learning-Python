# I removed all the comments from previous commit.
# Need more space to think about what is wrong with it.
end = False
def factorial(a):
    global end
    if (a == 'quit') or (a == 'Quit'):
        end = True
        return False
    try:
        a = int(a)
        x = 1
        value_storage = 1
        string_to_print = ""
        while x < a:
            x = x+1
            # Looks like issue with concatination
            if x == a:
                string_to_print += str(x)
            else:
                string_to_print += str(x)+"*"
            #print(string_to_print)
            value_storage = value_storage*x
        return print("Factorial of "+str(a)+" is "+"1*"+string_to_print+" = "+str(value_storage))
        #return print(value_storage)
    except:
        return print("We need a number to make factorial of. Try agane!")

def __main__():
    if not(end):
        print("Give me a number to make factorial off:")
        user_input = input()
        factorial(user_input)
        __main__()

__main__()
