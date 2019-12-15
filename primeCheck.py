import math as m
end = False
def primeCheck(num):
    global end
    if (num == 'quit') or (num == 'Quit'):
        end = True
        return False
    try:
        isPrime = True
        num = int(num)
        # my for loop doesn't work. Need to google why
        if num <= 1:
            isPrime = False
        else:
            for a in range(2, m.ceil(num/2)+1):
                if num % a == 0:
                    isPrime = False
    except:
        print("Words or letters cannot be prime")
        return False
        #I'm getting confused by this syntax. Who puts negative results first? Obviously creator of python
    return print(("Number "+str(num)+" is prime", "Number "+str(num)+" is not prime")[not(isPrime)])
def __main__():
    if not(end):
        print("Give me a number to check:")
        userInput = input()
        primeCheck(userInput)
        __main__()
    
__main__()