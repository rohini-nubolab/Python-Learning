# program to find Compound Interest

def compound_interest(principle, rate, time):

    amount = principle * (pow((1 + rate / 100) , time))
    CI = amount - principle
    print("compound interest", CI)

compound_interest(10000, 5.5, 3)

