"""8. Color Mixer
The colors red, blue, and yellow are known as the primary colors because they cannot be made by mixing 
other colors. When you mix two primary colors, you get a secondary color, as shown here:
When you mix red and blue, you get purple.
When you mix red and yellow, you get orange.
When you mix blue and yellow, you get green.
Design a program that prompts the user to enter the names of two primary colors to mix. If the user 
enters anything other than “red,” “blue,” or “yellow,” the program should display an error message. 
Otherwise, the program should display the name of the secondary color that results"""
try:
    mix1=input("Please enter the first names of two primary colors to mix:")
    mix2=input("Please enter the second names of two primary colors to mix:")
    if((mix1=="red" or mix1=="RED" or mix1=="Red") and (mix2=="blue" or mix2=="BLUE" or mix2=="Blue")):
        print("You mix red and blue, you get purple")
    elif((mix1=="red" or mix1=="RED" or mix1=="Red") and (mix2=="yellow" or mix2=="YELLOW" or mix2=="Yellow")):
        print("you mix red and yellow, you get orange")
    elif((mix1=="blue" or mix1=="BLUE" or mix1=="Blue") and (mix2=="yellow" or mix2=="YELLOW" or mix2=="Yellow")):
        print("You mix blue and yellow, you get green")
    elif((mix2=="red" or mix2=="RED" or mix2=="Red") and (mix1=="blue" or mix1=="BLUE" or mix1=="Blue")):
        print("You mix red and blue, you get purple")
    elif((mix2=="red" or mix2=="RED" or mix2=="Red") and (mix1=="yellow" or mix1=="YELLOW" or mix1=="Yellow")):
        print("you mix red and yellow, you get orange")
    elif((mix2=="blue" or mix2=="BLUE" or mix2=="Blue") and (mix1=="yellow" or mix1=="YELLOW" or mix1=="Yellow")):
        print("You mix blue and yellow, you get green")
    else:
        print("You enter wrong colors, please try again")
except ValueError:
    print("You enter wrong colors, please try again")
