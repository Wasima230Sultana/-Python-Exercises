number = int(input("Enter a number : "))

if(number%5 == 0):
    print(f"{number} is divisible by 5.")
elif(number%11 == 0):
    print(f"{number} is divisible by 11.")    
else:
    print(f"{number} is not divisible by 5 or 11.")    
