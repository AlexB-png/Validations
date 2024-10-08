import os
passw = input("Input a password\n")
while len(passw) < 8:
    print("Invalid password")
    passw=input("Input a new password! \n")
os.system('CLS')
print("Your password has been changed to", passw)