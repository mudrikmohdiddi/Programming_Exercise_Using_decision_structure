"""4. Roman Numerals
Write a program that prompts the user to enter a number within the range of 1 through 10. The program 
should display the Roman numeral version of that number. If the number is outside the range of 1 
through 10, the program should display an error message. The following table shows the Roman numerals 
for the numbers 1 through 10:
Number Roman Numeral
1       I
2       II
3       III
4       IV
5       V
6       VI
7       VII
8       VIII
9       IX
10      X
"""
try:
    n=int(input("Please enter number within the range of 1 through 10:"))
    if(n==1):
        print("""
    Number Roman Numeral
    1      I
    """)
    elif(n==2):
        print("""
    Number Roman Numeral
    2      II
    """)
    elif(n==3):
        print("""
    Number Roman Numeral
    3      III
    """)
    elif(n==4):
        print("""
    Number Roman Numeral
    4      IV
    """)
    elif(n==5):
        print("""
    Number Roman Numeral
    5      V
    """)
    elif(n==6):
        print("""
    Number Roman Numeral
    6      VI
    """)
    elif(n==7):
        print("""
    Number Roman Numeral
    7      VII
    """)
    elif(n==8):
        print("""
    Number Roman Numeral
    8      VIII
    """)
    elif(n==9):
        print("""
    Number Roman Numeral
    9      IX
    """)
    elif(n==10):
        print("""
    Number Roman Numeral
    10     X
    """)
    else:
        print("You enter wrong integer, please try again")
except ValueError:
    print("You enter wrong colors, please try again")
