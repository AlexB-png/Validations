import os
length=input("What is the length\n")
width=input("What is the width\n")
os.system('CLS')
x=1
while x == 1:
    try:
        length = int(length)
        x=0
        break
    except:
        print("There is an error with the length")
        length = input("Try again \n")

y=1
while y == 1:
    try:
        width = int(width)
        y=0
        break
    except:
        print("There is an error with the width")
        width = input("Try again \n")

total=0
total=width*length
os.system('CLS')
print("The area of the rectangle is",total)...
