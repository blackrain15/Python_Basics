c1 = int(input())
c2 = int(input())
c3 = int(input())
c4 = int(input())

c_no = int(input())

if(c_no >= (c1+c2+c3+c4)):
    print("Not Possible")
else:
    for i in range(c1+c2+c3+c4):
        if((i <= (c1-1)) and (c_no==i)):
            print("1")
            break
        if((i <= (c1+c2-1)) and (c_no==i)):
            print("2")
            break
        if((i <= (c1+c2+c3-1)) and (c_no==i)):
            print("3")
            break
        if((i <= (c1+c2+c3+c4-1)) and (c_no==i)):
            print("4")
            break