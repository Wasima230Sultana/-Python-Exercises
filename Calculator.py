def add(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def multiplication(num1, num2):
    return num2 * num1

def division(num1, num2):
    return num1 / num2

print("Select Operation")
print("1 -> Addition")
print("2 -> Subtraction")
print("3 -> Multiplication")
print("4 -> Division")


while(True):
    choice = input("Enter choice : ")

    if choice in {'1','2','3','4'}:
        num1 = float(input("Enter first number : "))
        num2 = float(input("Enter second number : "))

        if choice == '1':
            print(f"{num1} + {num2} = {(add(num1, num2))}")
        elif choice == '2':
            print(f"{num1} - {num2} = {(sub(num1, num2))}")
        elif(choice == '3'):
            print(f"{num1} * {num2} = {(multiplication(num1, num2))}")
        else:
            print(f"{num1} / {num2} = {(division(num1, num2))}")

        next = input("Let's exit calculation , Yes/No : ")
        if(next == 'No'):
            break

    else:
        print("Invalid input.")



    


