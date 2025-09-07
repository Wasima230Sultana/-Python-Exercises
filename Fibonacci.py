terms = int(input("How many terms ?  "))


def fibonacci(number):
    n1 , n2 = 0, 1
    count = 0
    if(terms <= 0):
        print("Please enter a positive number.")
    else:
        print("Fibonacci sequences : ")
        while(count < terms):
            print (f"{n1} ")
            n3 = n1 + n2
            n1 = n2
            n2 = n3
            
            count += 1
        

fibonacci(terms)

        


