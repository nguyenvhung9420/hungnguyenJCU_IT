import random

STARTING_PRICE = 10
RATE_INCREASE = 0.175

OUTPUT_FILE = "/Users/admin/Desktop/ToPrint.txt"
out_file = open(OUTPUT_FILE,'w')


days_amount = random.randint(1, 1000)
price = STARTING_PRICE

print("Starting price: ${:,.2f}".format(price))

for i in range(days_amount):
    while price >=1 and price <=100:
        price = price*(1 + RATE_INCREASE)
        print("${:,.2f}".format(price))
        print("${:,.2f}".format(price), file=out_file)

out_file.close()

