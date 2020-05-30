import sys

try:
    n = int(input())
    
    flag = False
    
    if(n<=0 or n>100):
        print("Invalid input")
        sys.exit(0)
    
    my_list = []
    
    for i in range(n):
        s = input()
        l = list(map(int,s.split()))
        
#        if(len(l) != 3):
#            flag = True
#           break
        
        if(l[0]<0 or l[0]>1000 or l[1]<1 or l[1]>1000 or l[2]<1 or l[2]>1000):
            flag = True
            break
        
        my_list.append(l)
    
    if(flag == True):
        print("Invalid input")
    else:
        time = 0
        for i in range(len(my_list)):
            if(i==0):
                time = my_list[i][1]
            else:
                if(time <= my_list[i][0]):
                    time = my_list[i][0]
                else:
                    time = time
                
                if(time > my_list[i][0]):
                    time = my_list[i][2]
                
                time = time + my_list[i][1]
    
        print(time)
except:
    print("Invalid input")