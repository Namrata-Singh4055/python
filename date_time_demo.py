import datetime

current = input("Enter the deadline:")

print("Deadline is "+current)

d1 = datetime.datetime.strptime(current,"%m/%d/%Y").date()
deadline = datetime.date.today()
diff =(d1 - deadline)
diff = diff.days
print("The remaining days to complete the project is "+str(diff))

week = int(diff/7)

diff = int(diff% 7)

print("This is equivalent to : "+str(week)+" weeks and "+str(diff)+" days.")

