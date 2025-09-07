num = int(input("Enter the number : "))

def getSum(num):
    sum = 0
    for i in str(num):
        sum += int(i)
    return sum
print(f"Sum of digit in {num} is {getSum(num)} .")