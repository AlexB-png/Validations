import os
user=input("What is the username?\n")
password=input("What is your password\n")
os.system('CLS')
while user == "":
    print("There was an error with your username")
    user= input("What is the username\n")
    os.system('CLS')
while password == "":
    print("There was an error with your password")
    password=input("What is your password \n")
    os.system('CLS')
os.system('CLS')
print("Thank you for logging in", user)