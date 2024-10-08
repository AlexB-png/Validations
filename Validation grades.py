import os
percent=0

percent=input("What was your test percentage \n")
while percent== "":
    percent=str(input("Try again"))

x=0
while x != 1:
    try:
        percent = int(percent)
        break
        x=1
    except:
        os.system('CLS')
        print("fail")
        percent=input("Try again 0-100\n")
os.system('CLS')
if percent< 10:
    print("F")
elif percent< 20:
    print("C")
elif percent< 40:
    print("C+")
elif percent< 50:
    print("B")
elif percent< 70:
    print("B+")
elif percent< 90:
    print("A")
elif percent <= 100:
    print("A+")