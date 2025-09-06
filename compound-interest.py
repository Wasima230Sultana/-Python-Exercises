p = float(input("Enter the number :"))
T = float(input("Enter the number :"))
R = float(input("Enter the number :"))

amount = p * (1 + R/100) ** T
compoundInterest = amount - p
print(f"Compound Interest {compoundInterest:.2f}")
