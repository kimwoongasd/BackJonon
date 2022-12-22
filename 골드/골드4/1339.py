n = int(input())
tem = []
for _ in range(n):
    a = list(map(str, input()))
    tem.append(a)

d = dict()

for x in tem:
    for j in range(len(x)):
        # 알파벳 자리에 대한 값을 dict에 저장
        d[x[j]] = d.get(x[j], 0) + 10 ** (len(x) - j - 1)

# 가장 값이 높은 순으로 정렬
d = sorted(d.items(), key= lambda x : -x[1])

total = 0
for i in range(len(d)):
    total += d[i][1] * (9 - i)
print(total)