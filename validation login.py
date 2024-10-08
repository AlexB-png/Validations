import os #imports the terminal cleanser#

user=input("What is the username?\n") #First input of Username#
password=input("What is your password\n") #First input of password#

os.system('CLS') #Clears the terminal#

while user == "":
    print("There was an error with your username") #Alert the user#
    user= input("What is the username\n")#repeat the username#
    os.system('CLS') #Clear the terminal#

while password == "":
    print("There was an error with your password")#alert the user#
    password=input("What is your password \n")#repeat the password#
    os.system('CLS') #Clears terminal#

os.system('CLS') #clear terminal#

print("Thank you for logging in", user) #welcomes the user#