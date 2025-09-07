ask_again = True

while ask_again:
    year = int(input("Enter the year : "))

    if(year%400 == 0):
       print(f"{year} is a Leap Year.")
    elif(year%100 == 0):
       print(f"{year} is not a Leap Year.")
    elif(year%4 == 0):
       print(f"{year} is a Leap Year.")
    else:
       print(f"{year} is not a Leap Year.")
    question = input("Do you want check another year ? Y/N  ").lower()
    if(question == 'y'):
       ask_again = True
    elif(question == 'n'):
       print("Stop")
       ask_again = False
    else:
       print("Invalid")
       ask_again = False
       






