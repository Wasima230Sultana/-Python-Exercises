marks = []
count = 0
while(count < 5):
    mark = float(input(f"Enter subject {count + 1} marks : "))
    marks.append(mark)
    count += 1

total = sum(marks)
average = total / len(marks) 
percentage = (total / (len(marks) * 100)) * 100 
print (f"Total = {total:.3f}")
print (f"Average = {average:.3f}")
print (f"Percentage = {percentage:.3f}%")
