num = int(input("Enter the number : "))
is_prime = True


for i in range(2, num):
    if(num % i == 0):
        is_prime = False
if(is_prime):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")

