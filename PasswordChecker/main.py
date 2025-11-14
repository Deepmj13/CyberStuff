import re

def checkpassword(password):
    score = 0
    if len(password)>=8:
        score+=1
    if re.search(r'[A-Z]',password) and re.search(r'[a-z]',password):
        score+=1
    if re.search(r'\d',password):
        score+=1
    if re.search(r'~`!@#$%^&*()_-+=\|*-?/>.<,:;',password):
        score+=1

    return score

def checkCommonPasswords(password):
    with open('CommonPasswords.txt','r') as file:
        for line in file:
            if line.strip() == password:
                return 1

password = input("Enter the password to check strength")
sc = checkpassword(password)
if checkCommonPasswords(password):
    print("Password is in the common list, Need to change ASAP")
else:
    if sc >= 3:
        print("It is String 💪")
    elif sc == 2:
        print("It is ok 🤞")
    else:
        print("You need to change right now")
