import math

x = input()
y = input()
z = input()

x = int(x)
y = int(y)
z = int(z)

#No. of containers per row
cont_per_row = x/y

#No. of containers per stack
cont_per_stack = cont_per_row*cont_per_row

#Height of the cargo
cargo_h = math.floor((z-1)/cont_per_stack)

cont_left = z - (cargo_h)*(cont_per_stack)

cont_loc_y = math.floor((cont_left-1)/cont_per_row)
cont_loc_x = int(cont_left - (cont_loc_y * cont_per_row)-1)


output = (cont_loc_x, cont_loc_y, cargo_h)

print(output)