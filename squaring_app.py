end = False
# and I almost did it again. Damn you semicolons
def square(a):
    # That worked?
    global end
    # K boomer
    # ffs... || doesn't work in this language
    #if (a == 'quit') || (a == 'Quit'):

    if (a == 'quit') or (a == 'Quit'):
        # well this sucks...
        # I just tried this type of code. Doesn't make the game stop. I'll try to print out what value this has. And depending on that answer just google.
        end = True
        # print here gives me True. Which means that it is not having any effect on the global variable @end
        #print(end)
    else:
        # seriously the tabbind drives me crazy. Just use semicolons like any other language
        try:
            a = int(a)
            # i moved it here so I can call new input after.
            return print(a*a)

        except:
            return print("Try number next time.")
#I'll want to call this function recursively after end of every iteration of the same function so it is in a cycle and I do not need to restart it all the time.
def __main__():
    print("Give me a number to square or type 'quit' to exit the app")
    user_input = input()
    square(user_input)
    # Exactly as I said. No effect on the global variable. I'll try the same thing that I know from javascript.
    # Use the keyword Global to say that I want to effect the variable globally 
    #print(end)

    # I tried to use short syntax to test @end but it doesn't work like that obviously
    #if !(end):

    # Somehow intuitively I figured this out on the first try
    if not(end):
        __main__()
# It works!
# I should add a cycle break keyword. Because now I have to stop it manually. 
# My optimistic plan is to define a boolean variable that will store whether user used the word "quit" instead of real input. Which will tell me whether to quit or not...
__main__()