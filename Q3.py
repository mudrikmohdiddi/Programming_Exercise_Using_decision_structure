"""3. Age Classifier
Write a program that asks the user to enter a person’s age. The program should display a message 
indicating whether the person is an infant, a child, a teenager, or an adult.
Following are the guidelines:
• If the person is 1 year old or less, he or she is an infant.
• If the person is older than 1 year, but younger than 13 years, he or she is a child.
• If the person is at least 13 years old, but less than 20 years old, he or she is a teenager.
• If the person is at least 20 years old, he or she is an adult."""
try:
    age=float(input("Please enter your age:"))
    if(age>0 and age<=1):
        print("A person’s age is infant")
    elif(age>1 and age<=13):
        print("A person’s age is child")
    elif(age>13 and age<=20):
        print("A person’s age is teenager")
    elif(age>20):
        print("A person’s age is adult")
    else:
        print("You enter wrong input")
except ValueError:
    print("You enter wrong colors, please try again")

          
         
