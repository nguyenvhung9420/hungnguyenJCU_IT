numbersToPrint = [0, 50, 100]

for i in range(len(numbersToPrint)):
    print("This is {:>15}".format(numbersToPrint[i]))


#Another way:

for i in range(0, 101, 50):
    print("This is {:>15}".format(i))
