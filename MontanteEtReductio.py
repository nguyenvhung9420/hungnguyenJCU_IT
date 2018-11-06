amount = int(input("Type the amount: "))

TAUX_REDUCTION = 0.05

if amount > 100:
    amount = amount * (1 - TAUX_REDUCTION)

print("The final amount is ", amount)
