num1 = int(input("Enter a number : "))
fact = 1

if(num1 < 0):
    print ("Number is negative.")

else:
   for i in range(1, num1 + 1):
        fact = fact * i
   print (f"Factorial of {num1} is {fact}.")