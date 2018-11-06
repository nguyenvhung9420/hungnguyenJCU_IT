import random

MIN_PRICE =0.01
MAX_PRICE = 1000

INCREASE_RATE = 0.1
DECREASE_RATE = 0.05

FIRST_PRICE = 10

price = FIRST_PRICE

print("${:,.2f}".format(price))

while price >= MIN_PRICE and price <= MAX_PRICE:
    amountToChange = 0

    if random.randint(1, 2) == 1: #then decrease:
        amountToChange = random.uniform(-DECREASE_RATE, 0)
    else:
        amountToChange = random.uniform(0, INCREASE_RATE)

    price = price*(1 + amountToChange)
    print("The price is ${:,.2f}".format(price))