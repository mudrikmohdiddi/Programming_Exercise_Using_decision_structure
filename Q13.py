"""3. Body Mass Index Program Enhancement
In programming Exercise #6 in Chapter 3 you were asked to write a program that calculates a person’s 
body mass index (BMI). Recall from that exercise that the BMI is often used to determine whether a 
person is overweight or underweight for their height. A person’s BMI is calculated with the formula
BMI =weight * 703 / height2
where weight is measured in pounds and height is measured in inches. Enhance the program so it displays 
a message indicating whether the person has optimal weight, is underweight, or is overweight. A person’s 
weight is considered to be optimal if his or her BMI is between 18.5 and 25. If the BMI is less than 18.5, 
the person is considered to be underweight. If the BMI value is greater than 25, the person is considered 
to be overweight."""
try:
    w=float(input("Please enter a person's weight in pounds:"))
    h=float(input("Please enter a person's height in inches:"))
    BMI=w*703/h**2
    if(BMI>0 and BMI<18.5):
        print("He or she has underweight at BMI ",BMI)
    elif(BMI>=18.5 and BMI<=25):
        print("He or she has optimalweight at BMI ",BMI)
    elif(BMI>25):
        print("He or she has overweight at BMI ",BMI)
    else:
        print("You enter wrong input, please try again")
except ValueError:
    print("You enter wrong input, please try again")
