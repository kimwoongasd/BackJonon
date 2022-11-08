import sys

lt = list(map(str, sys.stdin.readline().strip()))
rt = []
n = int(input())

for i in range(n):
    a = sys.stdin.readline().strip()
    
    if a[0] == "L":
        if lt:
            rt.append(lt.pop())
        
    elif a[0] == "D":
        if rt:
            lt.append(rt.pop())
        
    elif a[0] == "B":
        if lt:
            lt.pop()
        
    elif a[0] == "P":
        lt.append(a[2])

rt.reverse()
lt.extend(rt)
print("".join(lt))

# 시간초과
# import sys

# lt = list(map(str, sys.stdin.readline()))
# rt = []
# n = int(input())

# for i in range(n):
#     a = sys.stdin.readline().strip()
    
#     if a[0] == "L":
#         if lt:
#             rt.insert(0, lt.pop())
        
#     elif a[0] == "D":
#         if rt:
#             lt.append(rt.pop(0))
        
#     elif a[0] == "B":
#         if lt:
#             lt.pop()
        
#     else:
#         lt.append(a[2])