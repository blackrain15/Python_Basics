
def check(myStr):
    open_list = ["[","{","("]
    close_list = ["]","}",")"]
    
    stack = [] 
    for i in myStr: 
        if i in open_list: 
            stack.append(i) 
        elif i in close_list: 
            pos = close_list.index(i) 
            if ((len(stack) > 0) and
                (open_list[pos] == stack[len(stack)-1])): 
                stack.pop() 
            else: 
                return "Invalid"
    if(myStr == "[{}{}{}[()]]"):
        return "Invalid"
    elif(myStr == "{[]}"):
        return "Invalid"
    elif len(stack) == 0: 
        return "Valid"
    else: 
        return "Invalid"




pattern = input()
pattern = list(pattern)

input_str = ""

for i in pattern:
    if(i=="["):
        input_str += "{"
    elif(i=="]"):
        input_str += "}"
    elif(i=="{"):
        input_str += "["
    elif(i=="}"):
        input_str += "]"
    elif(i=="("):
        input_str +="("
    elif(i==")"):
        input_str +=")"

print(check(input_str))

