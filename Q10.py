"""10. Book Club Points
Serendipity Booksellers has a book club that awards points to its customers based on the number of 
books purchased each month. The points are awarded as follows:
• If a customer purchases 0 books, he or she earns 0 points.
• If a customer purchases 1 book, he or she earns 5 points.
• If a customer purchases 2 books, he or she earns 15 points.
• If a customer purchases 3 books, he or she earns 30 points.
• If a customer purchases 4 or more books, he or she earns 60 points.
Write a program that asks the user to enter the number of books that he or she has purchased this month 
and displays the number of points awarded"""
try:
    book=int(input("Please enter the number of books purchased:"))
    if(book==0):
        print("You purchases 0 books, earns 0 points")
    elif(book==1):
        print("You purchases 1 books, earns 5 points")
    elif(book==2):
        print("You purchases 2 books, earns 15 points")
    elif(book==3):
        print("You purchases 3 books, earns 30 points")
    elif(book>=4):
        print("You purchases 4 books, earns 60 points")
    else:
        print("You enter wrong input, please try again")
except ValueError:
    print("You enter wrong input, please try again")
