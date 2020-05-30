s = input()

if((s[0].isalpha()==False) or (s[-1].isdigit() == False)):
    print("Invalid input")

else:
    source = ""
    target = ""
    
    source_flag = True
    target_flag = False
    
    for i in range(len(s)):
        if(s[i].isalpha()==True and source_flag==True):
            source = source + s[i]
        else:
            source_flag = False
            target_flag = True
        
        if(s[i].isalpha()==True and target_flag==True):
            target = target + s[i]
        else:
            target_flag = False

    if(source != "" and target != ""):
        print("{} to {}".format(source,target))
    else:
        print("Invalid Input")