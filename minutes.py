minutes = int(input("Enter the number of minutes :"))

hour = minutes // 60
remaining = minutes - (hour * 60)
print(f"{hour} hours and {remaining} minutes.")

