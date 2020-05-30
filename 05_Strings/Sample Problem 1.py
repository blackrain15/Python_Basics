email_add = input()

temp = email_add.split('@')

#splitting the email address into 2 parts - username and domain address
part1 = temp[0]
temp = temp[1].split('.')

#Splitting domain address into 2 parts - server name and type of email
part2 = temp[0]
part3 = temp[1]

rules_broken = []
flag = 0

#Checking for business rule#1
if(part3 == "com" or part3 == "in" or part3 == "edu"):
    flag1 = 0
else:
    flag1 = 1
    rules_broken.append(1)

#Checking for business rule#2    
if(len(part2)>3):
    flag2 = 0
else:
    flag2 = 1
    rules_broken.append(2)

#Checking for business rule#3
    
allowed_spl_chars = ['.', '_', '-']

if((part1[0] in allowed_spl_chars) or (part1[len(part1)-1] in allowed_spl_chars)):
    flag3 = 1
    rules_broken.append(3)
else:
    for i in range(3):
        part1.replace(allowed_spl_chars[i],'')

    if((part1.isdigit() == True or part1.isalpha() == True) and part1.islower()==True):
        flag3 = 0
    else:
        flag3 = 1
        rules_broken.append(3)

#Showing final status
if(flag1+flag2+flag3 == 0):
    print("Valid")
else:
    print("Invalid")
    
    for i in range(len(rules_broken)):
        print(rules_broken[i])