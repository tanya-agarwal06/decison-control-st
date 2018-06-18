#question 1
'''a=int(input("enter any number"))
if(a%4==0):
    print(" it is leap year")
else:
    print("it is not a leap year")'''

#2
'''l=int(input("enter length"))
b=int(input("enter breadth"))
if(l==b):
    print("it is a square")
else:
    print("it is a rectangle")'''

#3
'''a=int(input("enter age of first person"))
b=int(input("enter age of second person"))
c=int(input("enter age of third person"))
if(a>=b and a>=c):
        print("a is youngest")
elif(b>=a and b>=c):
        print("b is youngest")
else:
        print("c is youngest")

if(a<b and a<c):
        print("a is oldest")
elif(b<a and b<c):
    print("b is oldest")
elif(c<a and c<b):
    print("c is oldest")'''

#4
'''k=int(input("enter points out of 200"))
if(k>=1 and k<=50):
    print("sorry no prize tjis time")
elif(k>=50 and k<=100):
    print("congrats you won a book")
elif(k>=181 and k<=200):
    print("congrats you won chocolates")'''

#5
j=int(input("enter number of units, one unit is 100"))
sum=j*100
if(sum>=1000):
    b=(sum-(sum*10/100))
    print("amount : ", b )
else:
    print("amount : ", sum)
