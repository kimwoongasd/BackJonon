tem = input()
stack = []

count = 0
for i in range(len(tem)):
    if tem[i] == "(":
        stack.append("(")
        
    else:
        if i > 0:
            stack.pop()
            if tem[i - 1] == ")":
                count += 1
                
            else:
                count += len(stack)
print(count)