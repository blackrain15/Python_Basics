cont_weight = int(input())

counter = 0
weight_available = cont_weight

while(True):
    cargo_weight = int(input())
    weight_available -= cargo_weight
    if(weight_available <0):
        break
    counter += 1
    
print(counter)
    