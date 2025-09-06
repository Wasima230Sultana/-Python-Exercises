import math

number = float(input("Enter a number : "))
root = math.sqrt(number)
print(f"Square root of {number} is {root :.5f}.")

if(number % 2 == 0):
    print(f"{int(number)} is even.")
else:
    print(f"{int(number)} is odd.")


