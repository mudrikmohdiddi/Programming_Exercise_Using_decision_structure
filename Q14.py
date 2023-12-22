"""14. Time Calculator
Write a program that asks the user to enter a number of seconds, and works as follows:
• There are 60 seconds in a minute. If the number of seconds entered by the user is greater than or equal 
to 60, the program should display the number of minutes in that many seconds.
• There are 3,600 seconds in an hour. If the number of seconds entered by the user is greater than or 
equal to 3,600, the program should display the number of hours in that many seconds.
• There are 86,400 seconds in a day. If the number of seconds entered by the user is greater than or equal 
to 86,400, the program should display the number of days in that many seconds"""
try:
    s=float(input("Please enter number of seconds:"))
    m=s/60
    h=s/3600
    d=s/86400
    if(s>=86400):
        print(f"There are {d} days in seconds {s}")
    elif(s>=3600):
        print(f"There are {h} hours in seconds {s}")
    elif(s>=60):
        print(f"There are {m} minites in seconds {s}")
    elif(s>=0):
        print(f"There are {s} seconds")
    else:
        print("You enter wrong input, please try again")
except ValueError:
    print("You enter wrong input, please try again")
