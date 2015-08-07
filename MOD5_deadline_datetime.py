# Your challenge
# Ask a user to enter the deadline for their project
# Tell them how many days they have to complete the project
# For extra credit, give them the answer as a combination of weeks & days 
# (Hint: you will need some of the math functions from the module on numeric values)

import datetime
# dir(datetime)

currentDate = datetime.date.today()
print(currentDate)
print(currentDate.year)
print(currentDate.month)
print(currentDate.day)

print(currentDate.strftime('%d %b, %Y'))
# %a = abbrev day name
# %A = full day name
# %b = abbrev for month
# %B = full month name
# %d = day
# %y = 2 digit year
# %Y = 4 digit year
# strftime.org

print(currentDate.strftime('Today is %A, %B %d in the year %Y'))

deadDate = input("What is the current requested deadline for the project? (mm/dd/yyyy)  ")
deadline = datetime.datetime.strptime(deadDate, "%m/%d/%Y").date()
difference = deadline - currentDate
print ("Days: " + str(difference.days))
print ("Weeks: " + str(difference.days/7))
