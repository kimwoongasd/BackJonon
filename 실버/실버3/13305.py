n = int(input())
d = list(map(int, input().split()))
sity = list(map(int, input().split()))

res = 0
tem = sity[0]

# 맨 마지막 도시는 셀 필요없음
for i in range(n - 1):
    # 도시의 기름값이 전 기름값보다 싸다면 값을 바꾼다.
    if sity[i] < tem:
        tem = sity[i]
        
    res += tem * d[i]
    
print(res)