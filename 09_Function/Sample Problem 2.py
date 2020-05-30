str = input()

str = str.lower()

new_str = ""

for i in range(len(str)):
    if(str[i].isalpha()):
        new_str+=str[i]

flag = 0
for i in range(int(len(new_str)/2)):
    if(new_str[i] != new_str[len(new_str)-i-1]):
        flag = 1

if(flag ==0):
    print("Yes")
else:
    print("No")