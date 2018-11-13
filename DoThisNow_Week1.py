#Write Python code to ask the user for a number, and then print that number multiplied by 2:

finished = False
resultToPrint = 0

while finished == False:

    try:
        user_input = int(input("Please type a number: "))
        resultToPrint = user_input*2
        finished = True

    #In case user has entered a value that cannot be parsed to number:
    except ValueError:
        print("It seems not to be a valid number, please try again below:")

print("The result is: {0} x 2 = {1}".format(user_input, resultToPrint))