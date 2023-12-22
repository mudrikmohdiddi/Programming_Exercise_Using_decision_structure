"""5. Areas of Rectangles
The area of a rectangle is the rectangle’s length times its width. Write a program that asks for the length 
and width of two rectangles. The program should tell the user which rectangle has the greater area, or if 
the areas are the same."""
try:
    L1=float(input("Please enter length of rectangle_1:"))
    W1=float(input("Please enter width of rectangle_1:"))
    L2=float(input("Please enter length of rectangle_2:"))
    W2=float(input("Please enter width of rectangle_2:"))
    area_rectangle_1=L1*W1
    area_rectangle_2=L2*W2
    print("Area of rectangle_1 is: ",area_rectangle_1)
    print("Area of rectangle_2 is: ",area_rectangle_2)
    if(area_rectangle_1>area_rectangle_2):
        print("Area of rectangle_1 is greater area of rectangle_2")
    elif(area_rectangle_1<area_rectangle_2):
        print("Area of rectangle_2 is greater area of rectangle_1")
    else:
        print("Area of rectangle_1 is equal to area of rectangle_2")
except ValueError:
    print("You enter wrong colors, please try again")
