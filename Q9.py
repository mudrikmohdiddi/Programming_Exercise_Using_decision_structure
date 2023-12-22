"""9. Change for a Dollar Game
Create a change-counting game that gets the user to enter the number of coins required to make exactly 
one dollar. The program should prompt the user to enter the number of pennies, nickels, dimes, and 
quarters. If the total value of the coins entered is equal to one dollar, the program should congratulate 
the user for winning the game. Otherwise, the program should display a message indicating whether the 
amount entered was more than or less than one dollar."""
try:
    pennies=int(input("Please enter number of pennies:"))
    nickels=int(input("Please enter number nickels:"))
    dimes=int(input("Please enter number dimes:"))
    quarters=int(input("Please enter number quarters:"))
    total_value=pennies+5*nickels+10*dimes+25*quarters
    if(total_value==100):
        print("Congratulation you win the game")
    elif(total_value>100):
        print("Sorry, you enter amount more than one dollar")
    else:
        print("Sorry, you enter amount less than one dollar")
except ValueError:
    print("Sorry, you enter amount less than one dollar")
