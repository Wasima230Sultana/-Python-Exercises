num = int(input("Enter the number : "))
answer = 1
for i in range(1, 11):
    answer = num * i
    print(f"{num} x {i} = {answer}")