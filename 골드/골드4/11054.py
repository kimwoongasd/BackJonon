a = int(input())
arr = list(map(int, input().split()))

# 왼쪽 값이 기준보다 작을 때 최대값 구하기
lt = [0] * a
lt[0] = 1
for i in range(1, a):
    m = 0
    for j in range(i - 1, -1, -1):
        if arr[i] > arr[j] and m < lt[j]:
            m = lt[j]
    lt[i] = m + 1

# 기준보다 오른쪽값이 작을 때 최대값 구하기
rt = [0] * a
rt[-1] = 1
for i in range(a - 1, -1, -1):
    m = 0
    for j in range(i, a):
        if arr[i] > arr[j] and m < rt[j]:
            m = rt[j]
    rt[i] = m + 1

# 두개의 리스트를 더하고 겹치는 부분이 있으니 -1
res = []
for i in range(a):
    res.append(lt[i] + rt[i])
    
print(max(res) - 1)