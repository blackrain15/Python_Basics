f_in = open("readlines.txt", "r")
input_text = f_in.read()

input_text = input_text.split('\n')

f_in.close()

print('Enter the n value')
n = int(input())

i=n-1
while(i>=0):
    print(input_text[len(input_text)-1-i])
    i=i-1