n = int(input())

i=1
while(i<=n):
    mytext = ""
    
    for j in range(n-i):
        mytext += "#"
    
    for j in range(2*(i-1)+1):
        mytext += "*"
    
    for j in range(n-i):
        mytext += "+"
    
    print(mytext)
    i=i+1