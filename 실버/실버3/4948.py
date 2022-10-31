# 시간 감소
def f(x):
    count = 0
    for i in range(x + 1, x * 2 + 1):
        if ch[i] == 0:
            count += 1
    return count

ch = [0] * (123456 * 2 + 1)
ch[0] = 1
ch[1] = 1
for i in range(2, 123456 * 2 + 1):
    if ch[i] == 0:
        for j in range(i * 2, 123456 * 2 + 1, i):
            ch[j] = 1

while True:
    tem = int(input())
    if tem == 0:
        break
    
    res = f(tem)
    print(res)

# def f(x):
#     if x == 1:
#         return x

#     else:
#         count = 0
#         ch = [0] * (x * 2 + 1)
#         for i in range(2, x * 2 + 1):
#             if ch[i] == 0:
#                 for j in range(i * 2, x * 2 + 1, i):
#                     ch[j] = 1

#         for i in range(x + 1, x * 2 + 1):
#             if ch[i] == 0:
#                 count += 1

#         return count

# res = []

# while True:
#     tmp = int(input())
#     if tmp == 0:
#         break

#     res.append(f(tmp))

# for x in res:
#     print(x)
    