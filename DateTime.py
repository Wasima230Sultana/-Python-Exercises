import datetime
days = int(input("Enter number of days : "))

today = datetime.datetime.now()
print("Current year : ",today.strftime ("%Y"))

years = days // 365
remaining_days = days % 365
weeks = remaining_days // 7
rest_of_days = remaining_days % 7

print(f"{days} days =  {years} years,  {weeks} weeks,  and {rest_of_days} days.")












# convert specified days into years, weeks and the
# rest of the days.