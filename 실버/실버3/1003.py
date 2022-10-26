def DFS(L):
    if len(x) <= L:
        for i in range(len(x), L + 1):
            x.append(x[i - 2] + x[i - 1])
            y.append(y[i - 2] + y[i - 1])
    print(x[L], y[L])

x = [1, 0, 1]
y = [0, 1, 1]
n = int(input())
for i in range(n):
    a = int(input())
    DFS(a)


# 시간초과
# def fibonacci(x):
#     global zero, one
#     if x == 0:
#         zero += 1
#         return
#     elif x == 1:
#         one += 1
#         return
#     else:
#         return fibonacci(x - 2), fibonacci(x - 1)
    
    

# n = int(input())

# for i in range(n):
#     a = int(input())
#     zero = 0
#     one = 0
#     fibonacci(a)
#     print(f"{zero} {one}")