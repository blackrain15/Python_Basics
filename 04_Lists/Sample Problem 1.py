input_text = input()
counts = int(input())

profits = input_text.split(",")
profits.sort(reverse = True)

total_profit = 0
for i in range(counts):
    total_profit += int(profits[i])


print(total_profit)

