n = int(input())
s = []

for _ in range(n):
    tem = int(input())
    if tem != 0:
        s.append(tem)
    else:
        s.pop()
print(sum(s))