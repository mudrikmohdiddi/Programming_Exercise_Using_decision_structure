"""12. Shipping Charges
The Fast Freight Shipping Company charges the following rates:
Weight of Package Rate per Pound
2 pounds or less $1.10
Over 2 pounds but not more than 6 pounds $2.20
Over 6 pounds but not more than 10 pounds $3.70
Over 10 pounds $3.80
Write a program that asks the user to enter the weight of a package and then displays the shipping 
charges."""
try:
    w=float(input("Please enter the weight of package at pound:"))
    if(w>=0 and w<=2):
        ch=w*1.1
        print("The shiping charges of pounds",w,"is $",ch)
    elif(w>2 and w<=6):
        ch=w*2.2
        print("The shiping charges of pounds",w,"is $",ch)
    elif(w>6 and w<=10):
        ch=w*3.7
        print("The shiping charges of pounds",w,"is $",ch)
    elif(w>10):
        ch=w*3.8
        print("The shiping charges of pounds",w,"is $",ch)
    else:
        print("You enter wrong input, please try angain")
except ValueError:
    print("You enter wrong input, please try angain")
