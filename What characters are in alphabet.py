characters = input("Input a word \n")
success=0
fail = 0
valid = False
while not valid:
    for i in range(len(characters)):
        if ord(characters[i]) in range(97, 123):  
            success += 1
        else:
            
            print("ERROR")
            fail += 1
    if fail == 0:
        valid = True 
        print("There are", success,"characters in the alphabet")
        fail=0
        success=0
        characters=input("input another word to check")
    else:
        print("The word has", fail, "Unavailable characters, this could be a capital letter, number, or a special character")
        characters=input("Input another word to check \n")
        fail=0
        success=0
