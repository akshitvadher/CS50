from cs50 import

while Ture:
    cents = get_float("Charge: ")
    if cents > 0:
        break

cents = round(cents*100)

count = 0

while cents >= 25:
    cents = cents - 25
    count += 1