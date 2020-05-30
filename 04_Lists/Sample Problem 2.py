my_text = input()
input_status = input()

package_statuses = my_text.split(",")

counter = 0
flag = 0

for item in package_statuses:
    if(item == input_status):
        counter+=1
        flag = 1
        print(counter)
    else:
        counter+=1

if(flag==0):
    print(flag)