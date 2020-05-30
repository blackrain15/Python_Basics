f_in = open("file_in.txt", "r")
f_out = open("file_out.txt", "w")

f_out.write(f_in.read())
f_out.close()

f_in = open("file_out.txt", "r")
print(f_in.read())