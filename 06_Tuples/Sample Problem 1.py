comm_weights = input()
no_of_pieces = int(input())

comm_weights = comm_weights.split()
total_weights = list(map((lambda x : int(x)*no_of_pieces),comm_weights))

print(tuple(total_weights))

