"""15. Roulette Wheel Colors
On a roulette wheel, the pockets are numbered from 0 to 36. The colors of the pockets 
are as follows:
• Pocket 0 is green.
• For pockets 1 through 10, the odd-numbered pockets are red and the even-numbered
pockets are black.
• For pockets 11 through 18, the odd-numbered pockets are black and the evennumbered pockets are red.
• For pockets 19 through 28, the odd-numbered pockets are red and the evennumbered pockets are black.
• For pockets 29 through 36, the odd-numbered pockets are black and the even 
numbered pockets are red.
Write a program that asks the user to enter a pocket number and displays whether the
pocket is green, red, or black. The program should display an error message if the user
enters a number that is outside the range of 0 through 36"""
try:
    p=int(input("Please enter a pocket number:"))
    if(p==0):
        print(f"Pocket {p} is green")
    elif(p>=1 and p<=10):
        if(p%2==0):
            print(f"Pocket {p} is black")
        else:
            print(f"Pocket {p} is red")
    elif(p>=11 and p<=18):
        if(p%2==0):
            print(f"Pocket {p} is red")
        else:
            print(f"The pocket {p} black")
    elif(p>=19 and p<=28):
        if(p%2==0):
            print(f"Pocket {p} is black")
        else:
            print(f"Pocket {p} is red")
    elif(p>=29 and p<=36):
        if(p%2==0):
            print(f"Pocket {p} is red")
        else:
            print(f"The pocket {p} black")
    else:
        print("You enter wrong input, please try again")
except ValueError:
    print("You enter wrong input, please try agein")

    
