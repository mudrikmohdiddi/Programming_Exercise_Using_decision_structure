"""7. Magic Dates
The date June 10, 1960, is special because when it is written in the following format, the month times the 
day equals the year: 6/10/60
Design a program that asks the user to enter a month (in numeric form), a day, and a two digit year. The 
program should then determine whether the month times the day equals the year. If so, it should display 
a message saying the date is magic. Otherwise, it should display a message saying the date is not magic"""
try:
    month=int(input("Please enter a month in numeric form:"))
    day=int(input("Please enter a day:"))
    year=int(input("Please enter a two digit year:"))
    magic=month*day
    if(magic==year):
        print("Date ",month,"/",day,"/",year," the date is magic")
    else:
        print("Date " ,month,"/",day,"/",year," the date not magic")
except ValueError:
    print("You enter wrong colors, please try again")
