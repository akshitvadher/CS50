def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = (dollars * percent)/100
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    dollar = d.replace("$","")
    return float(dollar)


def percent_to_float(p):
    percen = p.replace("%","")
    return float(percen)


main()