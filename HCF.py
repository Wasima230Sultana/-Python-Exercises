num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))

def hcf_is(x, y):
    if(x < y):
        smaller = x
    else:
        smaller = y
    for i in range(1, smaller+1):
        if(x % i == 0) and (y % i == 0):
            hcf = i
    return hcf


print(f"H.C.F is {(hcf_is(num1, num2))}")

lcm = (num2 * num1) / (hcf_is(num1, num2))
print(f"LCM is {lcm}")
