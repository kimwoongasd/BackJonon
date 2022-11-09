n = int(input())

num = []
stack = []
tem = 0

for _ in range(n):
    a = int(input())
    
    while tem < a:
        tem += 1
        num.append(tem)
        stack.append("+")

    if num[-1] == a:
        num.pop()
        stack.append("-")
        
    else:
        print("NO")
        exit(0)
    
for x in stack:
    print(x)
