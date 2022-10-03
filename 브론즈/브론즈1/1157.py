tem = list(map(str, input()))

num = [0] * 50

for x in tem:
    num[ord(x) - 65] += 1
    
m = max(num)
count = 0
res = 0
for y in range(50):
    if m == num[y]:
        count += 1
        res = y
    
    if count > 1:
        print("?")
        exit()
        
print(num[res])