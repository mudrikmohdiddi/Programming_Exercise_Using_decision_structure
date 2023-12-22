"""1. Day of the Week
Write a program that asks the user for a number in the range of 1 through 7. The program should display 
the corresponding day of the week, where 1 = Monday, 2 = Tuesday, 3 = Wednesday, 4 = Thursday, 5 = 
Friday, 6 = Saturday, and 7 = Sunday. The program should display an error message if the user enters a 
number that is outside the range of 1 through 7."""
try:
    n=int(input("Please enter integer number in the range of 1 through 7:"))
    if(n==1):
        print("Monday")
    elif(n==2):
        print("Tuesday")
    elif(n==3):
        print("Wednesday")
    elif(n==4):
        print("Thursday")
    elif(n==5):
        print("Friday")
    elif(n==6):
        print("Saturday")
    elif(n==7):
        print("Sunday")
    else:
        print("You enter wrong input, please try again")
except ValueError:
    print("You enter wrong colors, please try again")
